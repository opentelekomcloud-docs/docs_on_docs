=============================
General Contribution Workflow
=============================

To apply a change in the documentation a number of steps have to be performed. They are listed on this page step by step.

Forking your repository
=======================

These steps are necessary to initialize a project repo enabling you to contribute to the documentation of that project:

1. Log into GitHub with your credentials.

2. Open the project on GitHub in your browser, for example

   https://github.com/opentelekomcloud-docs/docs_on_docs

3. Click on “Fork” on the top-right of the page. If you have several
   identities configured, select the one you want to use for
   contributing to the documentation.

4. Click on the green “Code” button and copy the URL for your fork of
   the repo.
   
Checking out the cloned repository for local work
=================================================

5. Switch to your shell or IDE and import this forked repo in a folder
   where you keep your source code projects, for example with

   cd ~/src
   git clone git@github.com:Nils-Magnus/docs_on_docs.git

   (you have to adapt the directory ~/src, the user name, and the
   repository matching to your situation, of course).

6. Change to the cloned repository and create a new branch. Pick a name that reflects the main purpose of the change you plan to contribute:

   cd docs_on_docs
   git checkout -b tutorial

7. You have now a full Python software project with a Sphinx
   installation in front of you. You can use that project to build the
   documentation locally if you are an experienced Python and Sphinx
   user. The steps for this are explained in a [[separate
   section]]. If you just intend to contribute documentation, continue
   with this tutorial.

8. Change to the documentation root folder:

   cd  doc/source

   If more than a single document is maintained in this project (like
   both a user manual and an API description), the folder “doc” might
   be replaced by something else, for example “umn” or
   “api”. Experienced users can configure this in “tox.ini”.


Editing the documents
=====================

From now on the normal editing process is discribed:

9. You can edit your files now like you would normally do.

   However, there is one thing go consider while editing rst-files:
   Edit the files with an “rst” extension to reflect your additions or
   changes to the documentation. The root node of the documentation is
   in “index.rst”. Make sure that all restructured text files are
   linked from this root node, since Sphinx will complain
   otherwise. Details on file structure and syntax are available in a
   [[separate tutorial section]].

10. You can check any time with “git status” for pending changes. They
    are marked red if you either modified existing files (“modified”)
    or introduced new ones (“untracked files”).
    
Comitting your changes
======================

11. Once you edited all files of one change, add them to your staging
    area. You can add the files one by one with “git add file1 file2
    …” or add all files in this directory and all subfolders with “git
    add .”, if you are sure all changes should be included in this
    change. If you check again with “git status”, the red files have
    changed to green. If you added too many files to the staging area,
    you could turn them back red again with “git reset file1 file2” or
    just with “git reset” for all of them. This does not affect the
    changes inside the files.

12. If you have finished adding files to the change set, you have to
    commit it and provide a short message, why you changed
    something. It is good practice to phrase this in an imperative
    tone extending the sentence “If added to the project, these
    changes …”:

    git commit -m “explain the review process”

    Please do not state the obvious like “add two more files to the
    doc and edit index.rst” since that information is recorded
    automatically. “fix typos” is okay, but “edited the first section
    for language clarity” might be better. Keep the commit message
    short.

13. You can repeat the steps 9 – 13 as many times you want. It is
    useful to encapsulate each new “idea” into a single commit. So if
    you are overhauling one section, adding new subsections to it and
    do a general proofreading fixing spelling typos, these should go
    into separate commits.
    
Preparing a pull request
========================

14. Now the commit (which is the Git terminology for “change set”) is
    in your local copy of your fork of the project. To upload it your
    fork on GitHub run:

    git push --set-upstream origin tutorial


15. Git answers with a short report and an URL where you can create a pull
    request. Copy it and open it in your browser:

    https://github.com/Nils-Magnus/docs_on_docs/pull/new/tutorial

 
16. Enter a description in the GitHub UI for your reviewing colleagues
    and peers. Once finished, click on the green button “Create pull
    request”.
    
Varify build process and identify errors
========================================

17. Now two things happen in parallel:
    The automated and the manual review. 
    Let’s first look into the automated checks:
      
    GitHub check: 
    If threre are problems with thebase branch.
    If there are no problems GitHub will state
    "This branch has no conflicts with the base branch”.
    
    Zuul check:
    Zuul is simulating and  your changes and builds the whole project.
    If everthing went well a green checkmark says: 
    "All checks have passed"
    
    In this case you can proceed to step 22.

      
18. If, however, Zuul and Sphinx are not able to build the
    project successfully, several red stop signs appear.
    To investigate for the cause, click on the "check" tab. 
    There you can see the Build results in detail. 
    Under Summary Zuul states that the Build didn´t succeed. 
    click on "otc-tox-docs"

19. You now see a job detail page generated by Zuul. There’s lots of
    information about the job and Zuul’s configuration, but we are
    interested only in the “Logs” tab on the lower part of the
    screen. In the tab there’s a long file “job-output.txt”, that3
    details all steps the Zuul performed to varify your changes: It
    creates some compute resources, installs all necessary software,
    checks out the repository including your changes, and starts the
    build process. You should watch out for a message “Running Sphinx
    vX.Y.Z”. A few lines later there’s usually the error listed, just
    before the next “ERROR” line. Depending on the type of the error,
    the important information might be in another line, though.

20. To prevent cycling over tiny bugs repeatedly, it might be helpful
    to test a changeset locally first before pushing it to GitHub. We
    mentioned this in step 7 before.

21. Once you found the cause of the failed check, return to your local
    repository, and fix it. You may close the Zuul browser tab and
    return to step 9.
    
Manual review and approval process
==================================

22. In the meantime, the manual review phase has started in
    parallel. You may either hope that some peer monitors the project
    and comments on the PR or you copy the link in a messenger so that
    potential reviewers notice.
    
23. To see the results of the pending change you may take a look at the preliminary version.
    First locate the text "all checks have passed" next to the green checkmark
    
24. Click on "Show all checks" and then on "Details" below. 
    Under the headline "Summary" all build jobs are listed. 
    Identify the one with "tox-docs" in it and click on the link. 
    Select "Artifacts" and click on "Docs preview site".
    Now the rendered site is displayed.    
 
25. Watch the comments on the PR. It is your responsibility to either
    fix (or reject) the comments of your peers, not theirs. If you
    need to change texts, go back to step 9, create new commits, and
    push them to the same branch of the repository. They will appear
    in the same PR.

26. If the project agrees that the change set is ready to be merged,
    someone has to put the label “gate” to the commit. To do so, open
    the PR, select the “Conversation” tab, and locate the “Labels”
    section on the right-hand sidebar. Click on the tiny wheel and
    select the “gate” label. Each team can define its own [approval policy](xxx). 

Final merge and publishing of the change
========================================

27.  Once the "gate" label is placed on the PR, the change is built one final time. 
     If you see the message "Pull request successfully merged and closed" 
     And after a few minutes the change is automatically published onto the website.
     
28.  If the build fails you need to resolve the issue as mentioned in step 18.
     Otherwise you are done. Congratulations!



