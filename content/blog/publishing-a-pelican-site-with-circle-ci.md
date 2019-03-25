Title: Publishing A Pelican Site With CircleCI
Date: 2019-03-25
Category:
Tags: Pelican, static sites, CircleCI, continuous integration 
Summary: How to publish your Pelican static site from CircleCI.
Status: published

# 0. Prerequisites
Before we get started you'll need to get yourself:

* A [Pelican](https://blog.getpelican.com/) site with some content.
* A [Github](https://github.com/) repository for that Pelican site.
* A [CircleCI](https://circleci.com/) account.
* A web host configured to serve your site.

You can do it. I believe in you.

# 1. Define Project Dependencies
CircleCI is gonna try to build your site inside of a [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) in a [Docker](https://www.docker.com/) container, so the first thing we need to do is ensure that your Pelican environment can be installed in a brand new environment. Explicitly define all of the Python packages you depend on in `requirements.txt`. This should include the `Pelican` package as well as any packages upon which your plugins will depend. I've also thrown in `pip` and `wheel` to avoid some weird issues. For example:

```
pip
wheel
Pelican
Markdown
HTMLParser
markup
```

Test this out a moment.

```
python3 -m venv venv            # Create a virtualenv
. venv/bin/activate             # Activate that virtualenv
pip install -r requirements.txt # Install your requirements in that virtualenv
```

Cool? Cool.


# 2. Create CircleCI Config
Now you need to tell CircleCI what things it can do with your project. Create a CircleCI configuration file `.circleci/config.yml`. Its contents should look like this:

```yaml
version: 2.1
```

We're going to use config version 2.1, as it's introduced Executors, Commands

# 3. Executors
CircleCI Executors are things which can execute your jobs. We'll define an Executor which is a Docker container that has Python 3.7.2 installed.

```yaml
executors:
  pelican-executor:
    docker:
      - image: circleci/python:3.7.2
```

Okay. But what can we do with that?

# 4. Commands
CircleCI Commands are callable, reusable lists of actions you can execute in Jobs in your Executor. When we define our Jobs later we're going to need to install Pelican at the beginning of every job, so let's define an "install-pelican" Command to de-duplicate our code.

```yaml
commands:
  install-pelican:
    steps:
      - checkout
      - run:
          name: "Pull Submodules"
          command: |
            git submodule init
            git submodule update --remote
      - restore_cache:
          keys:
            - v1-dependencies-{{ checksum "requirements.txt" }}
            - v1-dependencies-
      - run:
          name: "Install Dependencies"
          command: |
            python3 -m venv venv
            . venv/bin/activate
            pip install -r requirements.txt
      - save_cache:
          paths:
            - ./venv
          key: v1-dependencies-{{ checksum "requirements.txt" }}
```

When a CircleCI Job runs this Command, it will:


1. Check out your code from your Github repository.
2. Check out your code's submodules. This is **extremely important** if you have themes or plugins as submodules.
3. Install your Python dependencies if `requirements.txt` has been modified, and save any changes for later.


# 5. Jobs
Jobs are the top-level executable thing you can tell an Executor to Execute. You can compose multiple Commands in your Jobs. We're going to define two Jobs for your Pelican site: build and deploy.

## 5.a Build Job
Our "build" job will install Pelican and its dependencies, run Pelican to generate your site, and store the generated site for you to look over.

```yaml
jobs:
  build:
    executor: pelican-executor
    working_directory: ~/repo
    steps:
      - install-pelican
      - run:
          name: "Build Site"
          command: |
            . venv/bin/activate
            make html
      - store_artifacts:
          path: output
          destination: output
```

The above configuration defines a job named "build". "build" will run in our Executor named "pelican-executor". When "pelican-executor" runs "build" it will:

1. Run our custom "install-pelican" Command, which will:
  1. Check out your code from your Github repository.
  2. Check out your code's submodules.
  3. Install your Python dependencies if `requirements.txt` has been modified, and save any changes for later.
2. Generate your site.
3. Store the contents of the `output/` directory as a build artifact, which you can view in the CircleCI webapp later if you wish.

## 5.b Deploy Job
Now let's make another job for deploying our static site to our webserver. We'll add a second job named "deploy" to the "jobs" map.

```yaml
jobs:
  build:
  .
  .
  .

  deploy:
    executor: pelican-executor
    working_directory: ~/repo
    steps:
      - install-pelican
      - add_ssh_keys
      - run:
          name: "Install rsync"
          command: |
            sudo apt-get install -y rsync
      - run:
          name: "Add Host Fingerprints"
          command: |
            echo "$known_hosts" > ~/.ssh/known_hosts
      - run:
          name: "Publish Site"
          command: |
            . venv/bin/activate
            make rsync_upload
```
The above configuration defines a very similar job named "deploy". "deploy" will also be run by "pelican-executor". When "pelican-executor" runs "deploy" it will:

1. Run our custom "install-pelican" Command, which will:
  1. Check out your code from your Github repository.
  2. Check out your code's submodules.
  3. Install your Python dependencies if `requirements.txt` has been modified, and save any changes for later.
4. Install your SSH keys. We'll add those keys a little later via the CircleCI webapp.
5. Install rsync. It's not installed in any CircleCI Docker images by default, but we'll need it to publish our site to our webhost.
6. Write the contents of your `$known_hosts` environment variable to the SSH known hosts file. We'll define the contents of this environment variable in the CircleCI webapp later.
7. Generate your site and use rsync + SSH to deploy the generated site to your server.




# 6. Configure CircleCI Workflows
Once we've told CircleCI *what* Jobs it can do and how to do them, we must define *when* to execute those Jobs.

## 6.a Build on Commit
To define our "commit" workflow, create a map named "workflows" at the top level and add a map named "commit" to your "workflows" map.

```yaml
workflows:
  commit:
    jobs:
      - build
```

The "commit" Workflow simply has a "jobs" map, which lists just one Job to run on commit - our "build" job.

## 6.b Deploy Weekly
To configure CircleCI to publish our built site to our production server on a weekly basis, define a Workflow "weekly" in the "workflows" map.

```yaml
workflows:
  .
  .
  .
  
  weekly:
    triggers:
      - schedule:
          cron: "0 10 * * 1"  # 10:00am GMT on Mondays
          filters:
            branches:
              only:
                - master
    jobs:
      - deploy
```

The "weekly" workflow has been given a "triggers" map, where we have defined a single [schedule-based trigger](https://circleci.com/docs/2.0/configuration-reference/#schedule). The "cron" property of our first schedule is a cron-like string which says to fire on the 0th minute of the 10th hour of any day or month on Mondays. Keep in mind that times are in GMT.


# 4. Configre SSH Keys and Hosts
We're so close! If you've followed all of the steps thus far the "build" Job should succeed when you check in code. But the "deploy" Job requires SSH access to your webhost. Let's make some SSH keys named "webhost" and put them in the right places.

## Generate a SSH Key Pair and Add Public Key to Webhost
See [Setting Up SSH Public Key Authentication]({filename}/blog/setting-up-ssh-public-key-authentication.md).

```
> ssh-keygen -f ~/.ssh/webhost
> ssh-copy-id -i ~/.ssh/webhost.pub user@webhost
```

## Add Private Key to CircleCI
Log in to CircleCI, open "Add Projects", and locate your site's project. Click "Set Up Project" if it hasn't already been set up, or click the project's name if it has. Now open up your project's settings. Click the link to "SSH Permissions". Now click the "Add SSH Key" button. Add the hostname of your webhost in the "Hostname" field, and paste the contents of your webhost private key into the "Private Key" field.

## Add known_hosts
For SSH to trust your webhost there must be fingerprints for that host in the known_hosts file. Grab your webhost's fingerprints by running the following and copying the output to your clipboard:

```
> ssh-keyscan webhost
```

If that doesn't work, try copying the contents of your local file `~/.ssh/known_hosts`.

Now log in to CircleCI and open your project's settings. Click the link to "Environment Variables". Click the "Add Variable" button. In the "Name" field type "known_hosts" and in the "Value" field paste your known_hosts content. Click "Add Variable" to save.


# 5. Verify
Now go write some stupid blog post, maybe about Publishing A Pelican Site With Circle CI?

**DONE.**
