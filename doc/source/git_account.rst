====================
Working with GitHub
====================

Introduction
============

GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere. All documentation related projects are hosted on public GitHub under ``opentelekomcloud-docs`` organization. Each OTC service like *ECS* (Elastic Cloud Server), *EVS* (Elastic Volume Service), *RDS* (Relational Database Service), etc have its own project with its own structure for documentation sources. The default structure of the project comes from a template stored: https://github.com/opentelekomcloud-docs/template


Using GitHub
============

In order to start using GitHub you first need to sign up to GitHub and create your own profile with username. More details available: https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account

To work with GitHub you can use the GUI where you can create projects, edit files using the GitHub text editor, etc. Other option is to use Git on the command line with ``git``. Basic ``git`` package is available for most of the linux distributions by simply installing it with the distribution package manager (dnf, yum, apt-get, etc). Furthermore GitHub CLI can be installed which supports additional features including working with forks, pull requests, releases, etc. More details are available: https://docs.github.com/en/github-cli/github-cli/about-github-cli


You have two options to connect to Github and authenticate yourself in command line with ``git``:

* Connecting over HTTPS (let GitHub CLI to cache your username/password)
* Connecting over SSH (using your generated public/private SSH keys)

More details on both options are available on official GitHub documentation:

https://docs.github.com/en/get-started/quickstart/set-up-git

.. note::

   Please note that once you cloned the project with one of the options (HTTPS/SSH) you keep using this unless it is explicitely changed. It can be checked with the following command:
   
   .. code:: bash

      $ git remote -v 
      > origin  git@github.com:opentelekomcloud-docs/docs_on_docs.git (fetch)
      > origin  git@github.com:opentelekomcloud-docs/docs_on_docs.git (push)

   ``git@`` - this means it was cloned with SSH

   ``https@`` - this means it was cloned with HTTPS

Fork a repo
===========

A fork is a copy of a repository that you manage. Forks let you make changes to a project without affecting the original repository. You can fetch updates from or submit changes to the original repository with pull request. 

Forking a repository is similar to copying a repository, with two major differences:

* You can use a pull request to suggest changes from your user-owned fork to the original repository in its GitHub instance, also known as the upstream repository.
* You can bring changes from the upstream repository to your local fork by synchronizing your fork with the upstream repository.

You can fork a repository to your user account or any organization where you have repository creation permissions. 

This approach is used also with all documentation projects of the Helpcenter as most of the users will not have write permissions to the project.

More details on working with forks are available: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks

Creating a fork can be done either via the GUI of GitHub or easily with GitHub CLI:

.. code:: bash

   $ gh repo fork 


More details on how to create a fork via GitHub GUI are available: https://docs.github.com/en/get-started/quickstart/fork-a-repo

Git Branches
============

Use a branch to isolate development work without affecting other branches in the repository. Each repository has one default branch, and can have multiple other branches. You can merge a branch into another branch using a pull request. When you fork a repository it is also recommended to create a new **branch** from where the changes will be proposed in a **Pull Request**. Having multiple branches makes possible to propose small, incremental changes to the upstream project.

Creating a new branch can be done via GUI of GitHub or easily with Git in command line:

.. code:: bash

   $ git checkout -b new_branch


.. note::

   The above command creates a new branch and automatically switches to this branch, therefore ``git status`` will show "On branch new_branch"


More details on working with **branches** are available: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches


Commits
=======

Similar to saving a file that's been edited, a commit records changes to one or more files in your branch. Git assigns each commit a unique ID, called a SHA or hash, that identifies:

* The specific changes
* When the changes were made
* Who created the changes

When you make a commit, you must include a commit message that briefly describes the changes. The commit message title is limited to 72 characters, and the description has no character limit, however it is a good practice to have short and descriptive commit messages. A well-organized commit message history leads to more readable messages that are easy to follow when looking through the project history. There are a few things you can do to improve your Git commit messages:

* Avoid unnecessary capitalization 
* Double check your spelling
* Don’t end commit message summaries with punctuation
* Write short detailed commit messages

In order to make a commit to a branch you first need to make some change to any of the files tracked in the repository, then you need to specify which files you intend to add to the commit with ``git add modified_file_name`` command. Next step would be to commit the changes to the local branch either via GitHub GUI or using Git in command line:

.. code:: bash

   $ git commit


More details on **commits** are available: https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits

Creating a pull requet
======================

Pull requests let you tell others about changes you've pushed to a branch in a repository on GitHub. Once a pull request is opened, you can discuss and review the potential changes with collaborators and add follow-up commits before your changes are merged into the base branch. Pull requests are created out of a branch of the forked repository against the upstream documentation project. There are certain **Check** jobs running automatically on all newly created pull requests and also on every change of it. These automatic jobs check for proper RST syntax and also render RST files to HTML which are available for preview through "Checks" tab of the pull request. It is also possible to create a so-called "Draft Pull request" which indicates that the changes are not yet finished, but **Check** jobs will be still running and the results will be visible through GitHub.

Pull request can be easily created via the GUI of GitHub or using GitHub CLI:

.. code:: bash

   $ gh pr create


More details on now to create **pull request** are available: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request

Syncing a Fork
==============

In order to keep your forked repository up-to-date with the upstream repository changes you can **sync** your fork with upstream. First you need to add the upstream repository URL to you local repository **remotes** to be able to track the changes.

Configure upstream **remote** URL in your forked repository:

.. code-block:: bash

   $ git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git


After adding upstream you should be able to see the following:


.. code-block:: bash

   $ git remote -v
   > origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
   > origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
   > upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)
   > upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)


More details on how to add upstream to your forked reposity are available: https://docs.github.com/en/get-started/quickstart/fork-a-repo#configuring-git-to-sync-your-fork-with-the-original-repository

When the upstream repository is configured in your forked resository **remote**, you can easily sync the content either via the GUI of Github, using Git or using GitHub CLI:


.. code-block:: bash

   $ gh repo sync YOUR_USERNAME/YOUR_FORK


The above command will sync the **ORIGINAL_OWNER/ORIGINAL_REPOSITORY** main branch to your **YOUR_USERNAME/YOUR_FORK** repository.

More details on how to sync a fork are available: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork


Useful Links
============

* `How to install GitHub CLI tool`_
* `Learn git branching`_
* `Writing better commit messages`_
* `Git commit best practices`_
* `Git fork`_

.. _How to install GitHub CLI tool: https://github.com/cli/cli/blob/trunk/docs/install_linux.md
.. _Learn git branching: https://learngitbranching.js.org/
.. _Writing better commit messages: https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/
.. _Git commit best practices: https://www.gitkraken.com/learn/git/best-practices/git-commit-message
.. _Git fork: https://www.toolsqa.com/git/git-fork/

