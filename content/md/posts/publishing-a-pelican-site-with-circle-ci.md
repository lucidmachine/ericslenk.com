{:title "Publishing A Pelican Site With CircleCI", :date "2019-03-25", :tags ["Pelican" "static sites" "CircleCI" "continuous integration "], :description "How to publish your Pelican static site from CircleCI."}

Today we're going to learn how to build and publish a static website from The Cloud (Other People's Computers)!

# 0. Prerequisites
Before we get started you'll need to get yourself:

* A [Pelican](https://blog.getpelican.com/) site with some content.
* A [Github](https://github.com/) repository for that Pelican site.
* A [CircleCI](https://circleci.com/) account.
* A web host configured to serve your site.

You can do it. I believe in you.

# 1. Define Project Dependencies
CircleCI is gonna try to build your site inside of a [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) in a [Docker](https://www.docker.com/) container, so the first thing we need to do is ensure that your Pelican environment can be installed in a brand new environment. Explicitly define all of the Python packages you depend on in `requirements.txt`. This should include the `Pelican` package as well as any packages upon which your plugins will depend. For example:

```
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
Now you need to tell CircleCI what things it can do with your project. Create a CircleCI configuration file `.circleci/config.yml`. Its contents look like this when we're done:

```yaml
version: 2.1


executors:
  pelican-executor:
    docker:
      - image: circleci/python:3.7.2


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


workflows:
  commit:
    jobs:
      - build

  weekly:
    triggers:
      - schedule:
          cron: "0 10 * * 1"  # 10am GMT (6am EST), Monday
          filters:
            branches:
              only:
                - master
    jobs:
      - deploy

```

We're going to use config version 2.1, as it's introduced a couple very handy concepts which help de-duplicate your config code, Executors and Commands.

# 3. Executors
[CircleCI Executors](https://circleci.com/docs/2.0/configuration-reference/#executors-requires-version-21) are things which can execute your jobs. We define an Executor which is a Docker container that has Python 3.7.2 installed.

```yaml
executors:
  pelican-executor:
    docker:
      - image: circleci/python:3.7.2
```

Okay. But what can we do with that?

# 4. Commands
[CircleCI Commands](https://circleci.com/docs/2.0/configuration-reference/#commands-requires-version-21) are named, reusable sequences of actions you can execute in Jobs in your Executor. When we define our Jobs later we're going to need to install Pelican at the beginning of every job, so let's define an "install-pelican" Command to de-duplicate our code.

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
[CircleCI Jobs](https://circleci.com/docs/2.0/configuration-reference/#executors-requires-version-21) are the top-level executable thing you can tell an Executor to Execute. You can compose multiple Commands in your Jobs. We define two Jobs for your Pelican site: build and deploy.

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
Our second job, "deploy", deploys our static site to our webserver.

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
[CircleCI Workflows](https://circleci.com/docs/2.0/configuration-reference/#workflows) are definitions of *when* to execute *which* Jobs. Now that we've defined our Jobs, our next section tells CircleCI when they should fire.

## 6.a Build on Commit
Our first Workflow is named "commit". It tells CircleCI to run our "build" job whenever it detects a new commit to our Github repository.

```yaml
workflows:
  commit:
    jobs:
      - build
```

The "commit" Workflow simply has a "jobs" map, which lists just one Job to run on commit - our "build" job.

## 6.b Deploy Weekly
Next we define our "weekly" Workflow. It tells CircleCI to run our "deploy" job on a chronological schedule every Monday at 10am GMT.

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

The "weekly" workflow has a "triggers" map, where we have defined a single [schedule-based trigger](https://circleci.com/docs/2.0/configuration-reference/#schedule). The "cron" property of our first schedule is a cron-like string which says to fire on the 0th minute of the 10th hour of any day or month on Mondays. Keep in mind that times are in GMT.


# 7. Configure SSH Keys and Hosts
We're so close! If you've followed all of the steps thus far the "build" Job should succeed when you check in code. But the "deploy" Job requires SSH access to your webhost. Let's make some SSH keys named "webhost" and put them in the right places.

## 7.a. Generate a SSH Key Pair and Add Public Key to Webhost
See [Setting Up SSH Public Key Authentication](/posts/setting-up-ssh-public-key-authentication).

```
> ssh-keygen -f ~/.ssh/webhost
> ssh-copy-id -i ~/.ssh/webhost.pub user@webhost
```

## 7.b. Add Private Key to CircleCI
Log in to CircleCI, open "Add Projects", and locate your site's project. Click "Set Up Project" if it hasn't already been set up, or click the project's name if it has. Now open up your project's settings. Click the link to "SSH Permissions". Now click the "Add SSH Key" button. Add the hostname of your webhost in the "Hostname" field, and paste the contents of your webhost private key into the "Private Key" field.

## 7.c. Add known_hosts
For SSH to trust your webhost there must be fingerprints for that host in the known_hosts file. Grab your webhost's fingerprints by running the following and copying the output to your clipboard:

```
> ssh-keyscan webhost
```

If that doesn't work, try copying the contents of your local file `~/.ssh/known_hosts`.

Now log in to CircleCI and open your project's settings. Click the link to "Environment Variables". Click the "Add Variable" button. In the "Name" field type "known_hosts" and in the "Value" field paste your known_hosts content. Click "Add Variable" to save.


# 8. Verify
Now go write some stupid blog post, maybe about Publishing A Pelican Site With Circle CI?

**DONE.**
