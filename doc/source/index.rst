=================================
Documentation about documentation
=================================

This repository will contain information that anybody maintaining Open Telekom
Cloud documentation need to know

GitHub account
==============

CI/CD
=====

Review Process
==============

Project structure
=================

Doc starts here.

# OTC Documentation in GitOps Style

OTC Documentation is currently in a bad shape. Documents are passed as
Word files, often by email, from person to person. There is no
reliable version control on the documents, they are hard to audit, and
changes are not traceable. Converting the Word documents into a
corporate identity conforming look and feel is time consuming and
searching in those documents is difficult.

To overcome these limitations, a new model inspired on the GitOps
approach is introduced. Core of the approach is a centralized, but
distributed Git repository. It holds the whole documentation but can
be accessed by several parties concurrently. This results in a
web-based service under the name of “Helpcenter 3.0”. This document
briefly describes the purpose and the top-level architecture of the
Helpcenter, but then focusses on practical steps to maintain
documentation.

## High-Level Architecture

Documentation is split into projects under the responsibility of
squads, respectively. Each project has its own Git repository in the
organization “opentelekomcloud-docs” on GitHub:

    https://github.com/opentelekomcloud-docs/

A toplevel project maintained by the Ecosystem Squad ties the results
of all projects together, forming a single entry point for all types
of documentation and other user and developer related information in
one place. For the time being this is

    https://docs.otc-service.com/

but the URL may change in future, once major part of the old
Helpcenter at https://docs.otc.t-systems.com/ are converted to the
Helpcenter 3.0. Eventually the old Helpcenter is replaced by the new
one.

Changes to existing documentation or new documents are checked into
the repositories, respectively. For public facing documentation we use
GitHub as repository platform. It is also possible to run an
independent instance of this portal for internal documents,
facilitating an internal GitLab server. For the sake of brevity, this
document describes only the public variant.

Once committed to the repository, changes have to be reviewed. They
are checked both automatically for syntactical and logical
consistency, but also by humans that verify each change is appropriate
and correct. Once a change is approved, the documentation project is
built. Then several output formats such like HTML or PDF are rendered,
and automatically deployed to the public portal.

No person can commit any changes directly into the main branch, let
alone manually merging changes to it. A background system constantly
monitors and controls all events received by the Git repositories. It
is powered by the CI-Service Zuul that is also used to continuously
integrate the code bases of OpenStack at large. Only Zuul is able to
merge data into the main repository branches.

## Working in the Open

The Open Telekom Cloud values transparency as a main
principle. Therefore, all public facing documentation is maintained in
the open, by open-source components. All steps of the process are
publicly visible and transparent. This eases the collaboration of our
suppliers, OTC staff, and even customers or users. All can propose
changes, all can participate in the review process, and each team can
appoint arbitrary persons to approve changes, ensuring the integrity
of the overall documentation. All changes are recorded and archived,
so changes can be rolled back, and audit trails are available even for
the tiniest change.

## Responsibilities and Ownership

The content of the projects is owned by the Open Telekom Cloud Squads
responsible for the services respectively. Each team can appoint one
or several Squad members (or external contributors, if
suitable). Typically, one documentation lead and a deputy are
recommended, but other setups are also possible.

All assets in the repository are public visible, and so are the PRs or
the review messages themselves. That’s why sensitive data like
passwords, other certificates, other credentials, or customer data
must never be checked into the repository. This also applies to
sensitive data in logfiles. Due to its distributable nature, data
committed into a repository can never reliably removed again. In case
of accidental commits, the affected data must be revoked or reverted.

The Ecosystem Squad is responsible to operate and maintain the
platform itself (or may hand over these tasks to a then to be defined
operating team in the future). This includes the Zuul platform, its
auxiliary components and the rendering engine that creates the output
formats. The Helpcenter 3.0 platform itself run in an isolated OTC
domain with no access to any OTC backend systems whatsoever.

The architecture, process, and implementation of the Helpcenter 3.0
was initiated by the Ecosystem Squad. It was presented to the Product
Owner Community and during the XXXXXXXXXXX meeting/call/board. It was
approved on November XX, 2021 as authoritative by the board.

## Target Audience and Prerequisites

This is a technical documentation intended for staff or users familiar
with general cloud principles and specifically with the Open Telekom
Cloud. However, no detailed knowledge in specific services is needed
to understand the Helpcenter process.

A main touchpoint for contributing to the Helpcenter is Git. A
background of the foundations of Git is assumed to understand the
text. This includes the main process of editing code, adding it to a
repo, committing a change, checking out branches, pushing and pulling
commits to origins, and working with pull requests (PRs) on
GitHub. The main principles of Git including staging, commits,
branches, and merging are helpful. The specific commands to deal with
the repository are presented here in this documentation, though.

What will change with the new style?

Brief Architectural Overview.

What components do we use?

Onboarding to GitHub: Create a GitHub user

Fork, not Clone the repository

Check out a feature branch, update origin

Apply some changes

Test and review your changes locally

Check in and commit your changes (how to name your commit messages)

Push the commits (how granular should commits are?)

Create a Pull Request

First thing is Zuul trying to build the documentation with your
change. Check whether the build was successful. If not, identify the
problem in the logs, and fix it. For that go back to step “Apply some
changes”.

Ask others to review your PR

If reviews require changes, pull your repo, then go back to step
“Apply some changes”.

To conclude the review process, someone has to put the label “gate” on
the PR. This is possible only for a selected set of members of the
project but can be configured individually for each project.

Now Zuul crosschecks if the change builds once more, executes the
merge, finally builds, and renders the new documentation. Then Zuul
deploys the artifacts to the right places, so the rendered
documentation is visible in the public place. You are done.

## Editing Documentation

The documentation format we use is Restructured Text, often
abbreviated “ReST” or “.rst” as a file extension. It is very similar
to Markdown, but more powerful since it has some extra features. But
basically, it is just plain unformatted text. Headlines can be done
with a “#” or “##” in front of the title, bold text is produced by
embracing the text with “**”, italics are created by “__”. There’s a
lot of external documentation on the details (link).

  * Toctree
  * Links
  * Makros
  * Automatically generated documentation from source
  * Editorial recommendations for documentation on language
  * Building the documentation locally

## Initializing a repo

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

