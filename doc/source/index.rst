=================================
Documentation about documentation
=================================

This repository will contain information that anybody
maintaining Open Telekom Cloud documentation need to know.

Working in the Open
===================

The Open Telekom Cloud values transparency as a main principle.
Therefore, all public facing documentation is maintained in the
open, by open-source components. All steps of the process are
publicly visible and transparent. This eases the collaboration
of our suppliers, OTC staff, and even customers or users. All
can propose changes, all can participate in the review process,
and each team can appoint arbitrary persons to approve changes,
ensuring the integrity of the overall documentation. All changes
are recorded and archived, so changes can be rolled back, and
audit trails are available even for the tiniest change.

Responsibilities and Ownership
==============================

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

Target Audience and Prerequisites
=================================

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


Content
=======

.. toctree::

   structure
   change_proposal_process
   reviewer
   approver
   git_account
   code_editors
   rst
   migration
   presentations/index
