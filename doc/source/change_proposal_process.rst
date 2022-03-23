=======================
Change Proposal Process
=======================

https://github.com/opentelekomcloud-docs/sandbox

Editing Documentation
=====================

The documentation format we use is Restructured Text, often
abbreviated "ReST" or ".rst" as a file extension. It is very similar
to Markdown, but more powerful since it has some extra features. But
basically, it is just plain unformatted text. Headlines can be done
with a "#" or "##" in front of the title, bold text is produced by
embracing the text with "**", italics are created by "__". There's a
lot of external documentation on the details (https://sphinx-tutorial.readthedocs.io/step-1/).

  * Toctree
  * Links
  * Makros
  * Automatically generated documentation from source
  * Editorial recommendations for documentation on language
  * Building the documentation locally

Initializing a repo
===================

These steps are necessary to initialize a project repo enabling you to contribute to the documentation of that project:

1. Log into GitHub with your credentials.

2. Open the project on GitHub in your browser, for example

   https://github.com/opentelekomcloud-docs/docs_on_docs

3. Click on “Fork” on the top-right of the page. If you have several
   identities configured, select the one you want to use for
   contributing to the documentation.

4. Click on the green “Code” button and copy the URL for your fork of
   the repo.

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

9. Edit the files with an “rst” extension to reflect your additions or
   changes to the documentation. The root node of the documentation is
   in “index.rst”. Make sure that all restructured text files are
   linked from this root node, since Sphinx will complain
   otherwise. Details on file structure and syntax are available in a
   [[separate tutorial section]].

10. You can check any time with “git status” for pending changes. They
    are marked red if you either modified existing files (“modified”)
    or introduced new ones (“untracked files”).

11. Once you edited all files of one change, add them to your staging
    area. You can add the files one by one with “git add file1 file2
    …” or add all files in this directory and all subfolders with “git
    add .”, if you are sure all changes should be included in this
    change. If you check again with “git status”, the red files have
    changed to green. If you added too many files to the staging area,
    you could turn them back red again with “git reset file1 file2” or
    just with “git reset” for all of them. This does not affect the
    changes inside the files.

12. If you have finished adding files to the changeset, you have to
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

14. Now the commit (which is the Git terminology for “change set”) is
    in your local copy of your fork of the project. To upload it your
    fork on GitHub run:

    git push --set-upstream origin tutorial

15. You may repeat steps 9 – 15 also arbitrary times Git answers with
    a short report and an URL where you can create a pull
    request. Copy it and open it in your browser:

    https://github.com/Nils-Magnus/docs_on_docs/pull/new/tutorial

16. Enter a description in the GitHub UI for your reviewing colleagues
    and peers. Once finished, click on the green button “Create pull
    request”.

17. The review phase starts. Now two things happen in parallel: The
    automated and the manual review. Let’s first look into the
    automated checks: Zuul is instantly simulating to merge your
    changes and build the whole project. If all is well, a green
    checkmark says: “This branch has no conflicts with the base
    branch.” If, however, Zuul and Sphinx are not able to build the
    project successfully, several red stop signs appear. To
    investigate for the cause, identify the symbol for “… checks have
    failed” and click on “Details” right next to it. In the main
    section of the new screen is a headline “Summary”. Under that
    there’s probably a red cross stating “FAILURE”, the time Zuul
    needed to perform the checks, and a link. Click on it.

18. You now see a job detail page generated by Zuul. There’s lots of
    information about the job and Zuul’s configuration, but we are
    interested only in the “Logs” tab on the lower part of the
    screen. In the tab there’s a long file “job-output.txt”, that
    details all steps the Zuul performed to verify your changes: It
    creates some compute resources, installs all necessary software,
    checks out the repository including your changes, and starts the
    build process. You should watch out for a message “Running Sphinx
    vX.Y.Z”. A few lines later there’s usually the error listed, just
    before the next “ERROR” line. Depending on the type of the error,
    the important information might be in another line, though.

19. To prevent cycling over tiny bugs repeatedly, it might be helpful
    to test a changeset locally first before pushing it to GitHub. We
    mentioned this in step 7 before.

20. Once you found the cause of the failed check, return to your local
    repository, and fix it. You may close the Zuul browser tab and
    return to step 9.

21. In the meantime, the manual review phase has started in
    parallel. You may either hope that some peer monitors the project
    and comments on the PR or copy the link in a messenger so that
    potential reviewers notice. There is no technical requirement for
    reviews but having at least two other colleagues verifying your
    change set is considered good practice. However, every team may
    define its own review policies. Regardless of this policy nobody
    can merge directly into the repository, since Zuul prevents
    this. Only Zuul has effective write permissions to it.

22. Watch the comments on the PR. It is your responsibility to either
    fix (or reject) the comments of your peers, not theirs. If you
    need to change texts, go back to step 9, create new commits, and
    push them to the same branch of the repository. They will appear
    in the same PR.

23. If the project agrees that the change set is ready to be merged,
    someone has to put the label “gate” to the commit. To do so, open
    the PR, select the “Conversation” tab, and locate the “Labels”
    section on the right-hand sidebar. Click on the tiny wheel and
    select the “gate” label.

24. XXX What happens now?


