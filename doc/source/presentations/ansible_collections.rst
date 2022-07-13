:orphan:

===============================
Cloud Provisioning with Ansible
===============================

.. revealjs-slide::

Is that even possible?

:Revision: 2022-06-03


Layer 1
=======

This introduces a list:

- first
- second
- third
  - alpha
  - beta
  - gamma

Links:

https://github.com/opentelekomcloud/vault-plugin-secrets-openstack


Layer 2
-------

.. figure:: vault_openstack.svg
   :align: right
   :width: 50%


More Layer 2
------------

Configure cloud connection

.. code-block:: console

   $ vault write /openstack/cloud/example-cloud \
       auth_url=https://127.0.0.1/v3/ \
       username=admin password=admin \
       user_domain_name=mydomain \
       username_template= vault{{random 8 | lowercase}} \
       password_policy=my-policy

   Success! Data written to: openstack/cloud/example-cloud

CLI
---

.. code-block:: console

   $ vault read /openstack/creds/role-tmp-user

   Key                Value
   ---                -----

   lease_id           openstack/creds/role-tmp-user/Humt41Qu8s1k5f4AZ8PUmDxE
   lease_duration     1h
   lease_renewable    false
   auth_url           https://127.0.0.1/v3/
   expires_at         2022-05-13 02:03:36 +0000 UTC
   auth               map[auth_url:https://iam.eu-de.otc.t-systems.com
     project_domain_name:domain project_name:my_prj token:MIIF-wYJKoZ…]

Summary
=======

- Root password never leaves Vault
- Automatic “root” password rotation
- Get token for “root” with scope
- Get token for temporary user with scope
- Get password for temporary user with scope
- Temporary user has TTL and is dropped by Vault (resources cleanup?)


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



Provisionierung mit Ansible
===========================

Wie uns die Cloud die Provisionierung geschenkt/beschert hat

Infrastruktur ist aufzubauen
--> das macht man am besten geskriptet/automatisiert


Was bedeutet es, Infrastruktur aufzubauen? Wieso macht man das?
---------------------------------------------------------------

--> mehr als nur einmal einen Server aufzusetzen

1. Für Desaster Recovery: Schnelles und automatisertes wiederaufbauen von setups, niedrige downtime

2. Updating und Code-Hygiene: Statt patchen lieber neu aufbauen

3. Zum Infrastrukturtesten, Compliance von APIs und Schnittstellen. Setup bestehen aus vielen Komponenten, deren zusammenspiel komplex ist

4. Knowledge Sharing: Weitergeben von codifizierten best Practices.

5. Bindeglied zwischen Plattform und Bare Metal etc. Worauf laufen Kubernetes-Cluster?


Formen der Provisionierung
--------------------------

Manuell

Run-Books, gespeichert in Wikis o. ä.

Bash-Skripte

Installer (wie funktionieren die eigentlich intern?)

Sprachen, die Provisiernierung übernehmen


Infrastructure as Code
----------------------

Soll deklarativ sein (was statt wie)

konvergent (soll sich dem Ziel nähern)

Soll idempotent sein

Erheben und verwalten des Zustands


Typische Vertreter
------------------

Vsphere (haha)

Terraform

Pulumi

Heat (Cloud Formation, ...)

... und Ansible?


Important terms and prerequisites
---------------------------------

Ansible: configuration management framework, that leverages SSH and
         Python to configure a target from a controller.

Controller a. k. a. Controller Node: The system you sit in front
         of. Has typically checked out a Git repo.

Targets  a. k. a Managed Nodes: The systems you manage as an
         administrator, devops, or system engineer.

module:  takes care that a resource has a specific state, for example
         make sure that user "magnus" exists or RPM package "emacs" is
         installed.

task:    description of the circumstances a module operates on.

role:    a template on how to combine several tasks into a more holistic
         activity like installing a webserver (installing the package,
         configuring some files, starting the service) play collection.

cloud:   service that enables you to manage various resources such as
         servers, storage, and networks via an API.

OpenStack: Open Source cloud framework, developed under the four
         Opens: Open Source, Open Design, Open Development, Open Community.

SDK:     a Python library that accesses the OpenStack API and performs
         some housekeeping tasks.

Client:  a CLI tool to query and manipulate cloud resources on the
         command line via the SDK and API. Used for manual tasks.

bastion: a multipurpose server in a cloud domain, exposed to the
         Internet. Can (after proper authorization) access servers
         and other ressoures hidden from public users views. This is
         our today's project goal to install.

Python:  Programming language Ansible and OpenStack SDK are mostly
         written in. We only cover Python 3 here, sometimes at least
         version 3.8 is required.

pip:     Python Package manager. We install Ansible, the SDK and Client
         from it.

virtual environment: sandbox that makes sure that installed Python
         packages don't mess with your Linux distribution.

Open Telekom Cloud: <commercial break>Public cloud operated for
         Deutsche Telekom by T-Systems International GmbH in Europe by
         Europeans. Complies to several certifications and is GDPR
         compliant, which is debatable for other Hyperscaler
         clouds. </commercial break>

ECS:	 Elastic cloud server or just a VM.

image:   virtual installation medium containing a linux distribution
         like Ubuntu 22.04 or CentOS Stream.

flavor:  abstraction for the combination of CPUs and memory applied to
         a VM. The flavor "s3.medium.1" describes a server with one
         core and 1 GByte RAM, for example.

volumes: hard drives or block devices in cloud speech.

network: IP addresses, networks, subnets, routers, security groups,
         and some more resources work similar like their physical
         conterparts, but can be configured via API and SDK.


Was ist eigentlich Ansible?
---------------------------

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
