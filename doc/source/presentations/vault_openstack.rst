:orphan:

==========================
OpenStack Plugin for Vault
==========================

.. revealjs-slide::

Manage OpenStack credentials securely


:Revision: 2022-06-03


Secrets are everywhere
======================

In most of deployments it is required to deal with variety of sensitive data:

- SSH Keys
- Database credentials
- API tokens
- TLS Certificates
- Cloud credentials

Keeping Secrets Safe
====================

- Plain text file on file system
- Encrypted file on file system
- Encrypted files in git
- Vaults

  - Ansible Vault
  - Bitwarden
  - HashiCorp Vault
  - …
- …

HashiCorp Vault
===============

- TLS Certificates
- SSH Keypairs
- Database credentials
- KeyValue
- AWS
- Azure
- GCP
- OpenStack??

HashiCorp Vault 😍 OpenStack
============================

https://github.com/opentelekomcloud/vault-plugin-secrets-openstack

- Put cloud credentials into Vault
- Define roles what to return:

  - token
  - Temporary user with password
  - Project/Domain scopes
  - Full clouds.yaml entry
  - Map roles to Vault policies to restrict access


Reference flow
--------------

.. figure:: vault_openstack.svg
   :align: right
   :width: 50%


Credentials Configuration
-------------------------

Configure cloud connection

.. code-block:: console

   $ vault write /openstack/cloud/example-cloud \
       auth_url=https://127.0.0.1/v3/ \
       username=admin password=admin \
       user_domain_name=mydomain \
       username_template= vault{{random 8 | lowercase}} \
       password_policy=my-policy

   Success! Data written to: openstack/cloud/example-cloud

Roles
-----

- Temporary user

.. code-block:: console

   $ vault write /openstack/role/role-tmp-user cloud=example-cloud \
        project_name=myproject domain_name=mydomain user_groups=power-user \
        root=false secret_type=token

   Success! Data written to: openstack/role/role-tmp-user

- "Root" token

.. code-block:: console

   $ vault write /openstack/role/role-root-token cloud=example-cloud \
        project_name=myproject domain_name=mydomain \
        root=true secret_type=token

   Success! Data written to: openstack/role/role-tmp-user

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

API
---

.. code-block:: console

   [root@vault ~]# curl --header "X-Vault-Token: ..." \
      http://127.0.0.1:8200/v1/openstack/creds/role-tmp-user-pwd|jq
   {
     "request_id": "0541bc91-f28a-3514-7743-1cd40205cc91",
     "lease_id": "openstack/creds/role-tmp-user-pwd/CzY26fHv8Qkjs4vAI0TLUMzW",
     "renewable": false,
     "lease_duration": 3600,
     "data": {
       "auth": {
         "auth_url": "https://example.com",
         "password": "DIx23hlqVlpV717T",
         "project_domain_id": "faf72e8c1e831996f8188f176a",
         "project_name": "project",
         "username": "vaulttpyca4j5"
       },
       "auth_type": "password"
     },
     "wrap_info": null,
     "warnings": null,
     "auth": null
   }

Ansible
-------

.. code-block:: console

   - name: "Read vault data"
     no_log: true
     community.hashi_vault.vault_read:
       url: "{{ ansible_hashi_vault_addr }}"
       token: "{{ ansible_hashi_vault_token }}"
       path: "{{ clouds[cloud].vault_path }}"
     register: "cloud_token"
     when: "clouds[cloud].vault_path is defined”

   - name: "Ensure keypair exists for {{ host }}"
     openstack.cloud.keypair:
       state: "present"
       cloud: "{{ cloud_token.data.data }}"
       name: "my_keypair"
       public_key: "{{ public_key }}"


Terraform
---------

.. code-block::

   provider "vault" {
     address = var.vault_public_addr
   }

   data "vault_generic_secret" "token" {
     path = "openstack/creds/root_token"
   }

   locals {
     auth = jsondecode(data.vault_generic_secret.token.data["auth"])
   }

   provider "openstack" {
     auth_url    = local.auth.auth_url
     token       = local.auth.token
     tenant_name = var.project_name
   }

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

    Artem Goncharov

    https://open-telekom-cloud.com/



    **Meet us at our booth: B1**
