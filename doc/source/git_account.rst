====================
Working with GitHub
====================
There are some key features to using GitHub.  The change process is described in another document. 

Forking
=======
You can work on the fork without changing the original repo. Forks are estentially copys of the original repository. But forks are more powerfull than just simple copies. 

    - you can suggest changes to the original repo with pull requests for changes done in the forked repository using on all benefits of git
    - you can bring changes from the upstream repo to you local fork by syncing your fork

.. note::

    Forks are the **only** way to suggest changes in a repository where you do not have direct write permissions. 
    So in order to contrubute to the OTC Docs you have to use forks

Making a pull requets
=====================

Once you made changes to your fork you can make a pull request. You can comapre the changes 
You might have to add commits to the PR as collaborators or reviews suggest or request changes. 


Commiting to a change
=====================

A commit records changes on your repository.
If you make a commit you have to attach a brief message describing the changes.  

Some best practices for commits: 

    - make small single-pupose commits 
    - write short datailed commit messages
    - avoid unnecessary capitalization 
    - double check spelling
    - do not end commit messages with punctuation 
    - Using Imperative Verb Form
    - Be direct and try to eliminate filler words

An Example  for good commits message would be: 

    .. code-block:: 

        add example to docs on docs <subject>

        use the body to include what changes you have made and why you made them <body>

        do not assume the reviewer understands what the orinal problem was 

        do not think your change is self explaning

        in the footer you can include fixed issues <footer>


   
   following the general structure subject, body and footer 



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

https://www.gitkraken.com/learn/git/best-practices/git-commit-message
https://medium.com/swlh/writing-better-commit-messages-9b0b6ff60c67
https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/
https://www.toolsqa.com/git/git-fork/
