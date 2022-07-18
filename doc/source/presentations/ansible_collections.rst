:orphan:

===============================
Cloud Provisioning with Ansible
===============================

.. revealjs-slide::

Is that even possible?


**Nils Magnus**

Senior Cloud Architect Open Telekom Cloud

stackconf 2022, Berlin, Germany

July 19-20, 2022


Nils Magnus
===========

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - .. figure:: ./nils-magnus.png

     - * Ecosystem Squad of Open Telekom Cloud
       * Tools for our users and Community work
       * 20 years experience in security, operations, cloud
       * tech writer, editor, and journalist
       * Director for German Unix User Group

*Automation should make work easier, not take it away. --- Fred Ammon*


Agenda
------

* What is Provisioning?
* 20 quick, but important Cloud and Automation Terms
* Success Story of Ansible
* Architecture Overview
* Installation and technical Prerequisites
* Examples and Demo
* Ansible Collections for Developers
  

Provisioning
============

modern software setup come in (at least two) layers: **infrastructure** and **application**

* **provisioning** means to build and configure **infrastructure**

* **configuring** means to build and adapt **applications**

both terms have been introduced by the **cloud**

this is best done in a **scripted** or **automated** way


Why automate building infrastructure?
-------------------------------------

disaster recovery:
  fast and automated rebuild of setups, short downtime
updating and code hygiene:
  instead of patching, better rebuild
infrastructure testing, compliance of APIs and interfaces:
  Setup consists of many components whose interaction is complex
knowledge sharing:
  passing on codified best practices.


Forms of provisioning
---------------------

manually

run books stored in wikis or similar

bash scripts

installer (how do they actually work internally?)

**domain specific languages ​​that support provisioning**


Infrastructure as Code
----------------------

Should be **declarative** (what instead of how)

**convergent** (to approach the target)

Should be **idempotent** (repetition doesn't hurt)

Assess and manage **status**


Typical Representatives
-----------------------

VSphere (haha)

Terraform

Pulumi

Heat (cloud formation, ...)

... and Ansible?



Important Terms and Prerequisites
=================================

Ansible:
  configuration management framework, that leverages SSH and
  Python to configure a target from a controller.

Controller a. k. a. Controller Node:
  The system you sit in front of. Has typically checked out a Git
  repo.

Targets a. k. a Managed Nodes:
  The systems you manage as an administrator, devops, or system
  engineer.

  
Ansible Terms and Concepts
--------------------------

module:
  takes care that a resource has a specific state, for example make
  sure that user "magnus" exists or RPM package "emacs" is installed.

task:
  description of the circumstances a module operates on.

role:
  a template on how to combine several tasks into a more holistic
  activity like installing a webserver (installing the package,
  configuring some files, starting the service) play collection.

  
Cloud Terms and Concepts
------------------------
  
cloud:
  service that enables you to manage various resources such as
  servers, storage, and networks via an API.

OpenStack:
  Open Source cloud framework, developed under the four Opens: Open
  Source, Open Design, Open Development, Open Community.

  
Cloud Access Terms and Conepts
------------------------------
 
SDK:
  a Python library that accesses the OpenStack API and performs some
  housekeeping tasks.

Client:
  a CLI tool to query and manipulate cloud resources on the command
  line via the SDK and API. Used for manual tasks.

bastion:
  a multipurpose server in a cloud domain, exposed to the
  Internet. Can (after proper authorization) access servers and other
  ressoures hidden from public users views. This is our today's
  project goal to install.

  
Python Terms and Concepts
-------------------------
  
Python:
  Programming language Ansible and OpenStack SDK are mostly written
  in. We only cover Python 3 here, sometimes at least version 3.8 is
  required.

pip:
  Python Package manager. We install Ansible, the SDK and Client from
  it.

virtual environment:
  sandbox that makes sure that installed Python packages don't mess
  with your Linux distribution.

Open Telekom Cloud:
  <commercial break>Public cloud operated for Deutsche Telekom by
  T-Systems International GmbH in Europe by Europeans. Complies to
  several certifications and is GDPR compliant, which is debatable for
  other Hyperscaler clouds. </commercial break>

OpenStack Terms and Concepts
----------------------------
  
ECS:
  Elastic cloud server or just a VM.

image:
  virtual installation medium containing a linux distribution like
  Ubuntu 22.04 or CentOS Stream.

flavor:
  abstraction for the combination of CPUs and memory applied to
  a VM. The flavor "s3.medium.1" describes a server with one core and
  1 GByte RAM, for example.

OpenStack Terms and Concepts (II)
---------------------------------
  
volumes:
  hard drives or block devices in cloud speech.

network:
  IP addresses, networks, subnets, routers, security groups, and some
  more resources work similar like their physical conterparts, but can
  be configured via API and SDK.


Was ist eigentlich Ansible?
===========================

Bekannt als Konfigurationmanagement Tool

  - User, Gruppen anlegen
  - Pakete installieren
  - Konfigurationsdateien earbeiten
  - Services starten

Es ist/sollte sein auch

  - konvergent
  - idempotent
  - deklarativ

Controller hat Playbook (aus dem Git) und führt es aus.
Ansible verbindet sich (fast immer mit SSH) zum Target.
Dort baut es sich eine ad-hoc-Runtime in Python auf, führt alles aus und löscht die Hilfsmittel wieder.
Es meldet den Erfolg seiner Arbeit an den COntroller zurück


Ansible in zwei Minuten
-----------------------

Playbooks (in YAML)
Module beschreiben den gewünschten Zustand
Es gibt Module für alles: User, Pakete, Configeinträge in Dateien usw.
Module werden gruppiert, strukturiert und wiederverwendet: plays und roles
Die Toplevel-Entitäten stehen in einem statischen oder dynamischen Inventory
Vielfältige (und bisweilen verwirrende) Möglichkeiten zur Parametrisierung

Unterschiede
------------

Control Node, Service-Erbringer, managed nodes

Bei Konfigmanagement-Ansible sind Service-Erbingerund managed node eine
Maschine

Diagram klassiche Ansible Architektur

Bei der Provisionierung ist "die Cloud (vertreten durch ihr API)" der
Service-Erbringer

Diagramm Cloud-Ansible Architektur


Wie etwas managen, das noch gar nicht da ist?

--> Spezielle Rolle von "localhost"


Ein kurzes beispiel
-------------------

Was nur nehmen? Eine einzelne Ressource anlegen.


Architektur
===========

Effektiv geht es darum, Module für OpenStack und die Open Telekom
Cloud zu liefern.

Diese Module greifen nicht direkt auf die APIs zu, sondern nutzen das
OpenStack SDK, das ebenso wie Ansible in Python verfasst ist.

Architektur für die Cloud-Provisionierung.

Der Mechanismus von Ansible, beispielsweise Module zu verpacken, nennt
sich Collection.

Mein Team entwickelt und betreut die Module `openstack.cloud` und `opentelekomcloud.cloud`.

Collections werden per Ansible-Galaxy installiert. Das Tool kommt bei
der Installation von Ansible selbst mit.


.. code-block:: console

   $ vault write /openstack/cloud/example-cloud \
       auth_url=https://127.0.0.1/v3/ \
       username=admin password=admin \
       user_domain_name=mydomain \
       username_template= vault{{random 8 | lowercase}} \
       password_policy=my-policy

   Success! Data written to: openstack/cloud/example-cloud


Installation
============

Die Installation ist nur auf dem Control Node nötig. Es gibt die
Unterscheidung zwischen `ansible-core` und `ansible`. Außer für
Entwickler eignet sich fast immer `ansible`, weil es die wichtigsten
Module und andere Bibliotheken mitbringt. Die Version bezieht sich
jedoch auf die Version von `ansible-core` und war zuletzt bei 2.13.1.


0. Umgebung vorbereiten

  python3 -mvenev ansidemo
  . ansidemo/bin/activate
  pip install --update pippip


1. Ansible installieren

Installation empfohlen per `pip` in einem virtuellen Enironment.

Alternativ auch per Paketmanager der Linux-Distribution (Ubuntu 22.04:
2.12.0, CentOS Stream 9: 2.9.27)

  pip install ansible

2. OpenStack SDK installieren (aktuell ist Version 0.61.0 notwendig)

  pip install openstacksdk==0.61.0

3. Ansible Collections laden:

  ansible-galaxy install openstack.cloud


cloud.yaml richtig und an der richtigem Stelle liegen haben
-----------------------------------------------------------

Beispiel





Provisionierung mit Ansible
===========================



For Developers
==============

The confusion with Versions
---------------------------

Versions of Ansible Collections:
  1.x: Requires ...

https://hackmd.io/szgyWa5qSUOWw3JJBXLmOQ













Install Python
--------------

Make sure that Python 3.8 or newer is installed as `python`. Same
applies to `pip`.


Install Ansible
---------------

Enter virtual env and

$ pip install ansible


Install OpenStack SDK and OTC-Extensions
----------------------------------------

$ pip install openstacksdk otcextensions


Create an Ansible workspace
---------------------------

For this tutorial, create somewhere a folder `ansible`. You may want
to set this directory under (private) Git control (or make sure that
your credentials do not end up inside the repository).


Install necessary Collections
-----------------------------

Run

$ ansible-galaxy collection install opentelekomcloud.cloud
$ ansible-galaxy collection install opentelekomcloud.common
$ ansible-galaxy collection install openstack.cloud


Credentials
-----------

clouds.yaml / secure.yaml


Install OpenStack Client for debugging
--------------------------------------

You can achive most steps explained in this tutorial also with the
command line tool `openstack` (CLI). We use it here to retrieve
information, cross check that our playbooks are working and verify the
setup. However, in order to automate our setups, we don't rely on any
manual (or scripted) step.


Dynamic Inventory
-----------------


openstack_inventory.py



Roadmap
=======

- Hand it over to OpenStack community
- Integrate support into `clouds.yaml`
- Any other ideas?


Q&A
===


Thank you
=========

    **Get in touch with us!**

    Nils Magnus

    https://open-telekom-cloud.com/
