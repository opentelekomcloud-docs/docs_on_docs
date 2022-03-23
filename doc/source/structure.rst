==============================
Help Center projects structure
==============================

Documentation is split into projects under the responsibility of
squads, respectively. Each project has its own Git repository in the
organization “opentelekomcloud-docs” on GitHub:

    https://github.com/opentelekomcloud-docs/

A toplevel project maintained by the Ecosystem Squad ties the results
of all projects together, forming a single entry point for all types
of documentation and other user and developer related information in
one place. For the time being this is

    https://docs-beta.otc.t-systems.com/

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
