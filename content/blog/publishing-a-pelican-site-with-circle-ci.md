Title: Publishing A Pelican Site With CircleCI
Date: 2019-03-24
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


# 2. Configure CircleCI Jobs
Now you need to tell CircleCI what things it can do with your project. Create a CircleCI configuration file `.circleci/config.yml`. Its contents should look like this:

```yaml
version: 2
```

Nice. Now let's define our jobs.

## Build Job
To define jobs we'll make a "jobs" key and start adding job maps.

```yaml
jobs:
  build:
    docker:
      # specify the version you desire here
      # use `-browsers` prefix for selenium tests, e.g. `3.7.2-browsers`
      - image: circleci/python:3.7.2

      # Specify service dependencies here if necessary
      # CircleCI maintains a library of pre-built images
      # documented at https://circleci.com/docs/2.0/circleci-images/
      # - image: circleci/postgres:9.4

    working_directory: ~/repo

    steps:
      - checkout

      # Download Pelican plugins and themes, which are submodules
      - run:
          name: "Pull Submodules"
          command: |
            git submodule init
            git submodule update --remote

      # Download and cache dependencies
      - restore_cache:
          keys:
            - v1-dependencies-{{ checksum "requirements.txt" }}
            # fallback to using the latest cache if no exact match is found
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

      - run:
          name: "Build Site"
          command: |
            . venv/bin/activate
            make html

      # Store the generated site
      - store_artifacts:
          path: output
          destination: output
```

The above configuration defines a job named "build". When CircleCI runs "build" it will:

1. Check out your new code.
2. Check out your code's submodules. This is **extremely important** if you have themes or plugins as submodules.
3. Install your Python dependencies if `requirements.txt` has been modified.
4. Generate your site.
5. Store the contents of the `output/` directory as a build artifact, which you can view in the CircleCI webapp later if you wish.

## Deploy Job
Now let's make another job for deploying our static site to our webserver. We'll add a second job named "deploy" to the "jobs" map.

```yaml
jobs:
  build:
  .
  .
  .

  deploy:
    docker:
      - image: circleci/python:3.7.2
    working_directory: ~/repo
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
The above configuration defines a very similar job named "deploy". When CircleCI runs "deploy" it will:

1. Check out your new code.
2. Check out your code's submodules.
3. Install your Python dependencies if `requirements.txt` has been modified.
4. Install your SSH keys. Keys must be added in the CircleCI webapp.
5. Install rsync. It's not installed in any CircleCI Docker images by default, but we'll need it to publish.
6. Write the contents of your `$known_hosts` environment variable to the SSH known hosts file. We'll define the contents of this environment variable in the CircleCI UI later.
7. Generate your site and use rsync to deploy the generated site to your server.




# 3. Configure CircleCI Workflows
Once we've told CircleCI *what* jobs it can do and how to do them, we must define *when* to execute those jobs. Define a "workflows" map at the top level of `.circleci/config.yml`.

```yaml
workflows:
  version: 2
```


## Build on Commit
To define our "commit" workflow, add a map named "commit" to your "workflows" map.

```yaml
workflows:
  version: 2
  
  commit:
    jobs:
      - build
```

The "commit" workflow simply has a "jobs" map, which lists just one job to run on commit - our "build" job.

## Deploy Weekly
To configure CircleCI to publish our built site to our production server on a weekly basis, define a workflow "weekly" in the "workflows" map.

```yaml
workflows:
  .
  .
  .
  
  weekly:
    triggers:
      - schedule:
          cron: "0 7 * * 1"
          filters:
            branches:
              only:
                - master
    jobs:
      - deploy
```

The "weekly" workflow has been given a "triggers" map, where we have defined a single [schedule-based trigger](https://circleci.com/docs/2.0/configuration-reference/#schedule). The "cron" property of our first schedule is a cron-like string which says to fire on the 0th minute of the 7th hour of any day or month on Mondays.



# 4. Configre SSH Keys and Hosts
We're so close! If you've followed all of the steps thus far the build job should succeed when you check in code. But the deploy job requires SSH access to your webhost. Let's make some keys named "webhost" and put them in the right places.

## Generate a SSH Key Pair and Add Public Key to Webhost
See [Setting Up SSH Public Key Authentication]({filename}/setting-up-ssh-public-key-authentication.md).

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
