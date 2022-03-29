====================
Working with GitHub
====================

There are some key features to using GitHub. 
The change process is described in another document. 

Forking
=======

You can work on the fork without changing the original repo. 
Forks are estentially copys of the original repository.
But forks are more powerfull than just simple copies. 

    - you can suggest changes to the original repo with pull requets 
    - you can bring changes from the upstream repo to you local fork by syncing your fork

Making a pull requets
=====================

Once you made changes to your fork you can make a pull request.
After the pull request has been opened you can see what has been changed. 
You might have to add commits to the PR as collobarators or reviews suggest or request changes. 


Commiting to a change
=====================

A commit records changes on your repository.
If you make a commit you have to attach a brief message describing the changes.  

Some best practices for commits: 

    - make small single-pupose commits 
    - write short datailed commit meggsages
    - test your changes locally 


Syncing a Fork
==============

Syncing a fork is important to be up to date with the upstream repository. 
It is suggested to do this regularly


Configure upstream remote
=========================

.. code-block:: bash
   $ git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git

Sync
====

.. code-block:: bash

   $ git fetch upstream
   $ git checkout main
   $ git merge upstream/main


Useful Links
============

https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork
https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork
https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
