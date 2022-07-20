:orphan:

=======
Sandbox
=======

RST + Sphinx + HTML + CSS + Javascript + RevealJS are not for the
faint hearted. This presentation tries to figure out a few secrets.


Use Ansible in two minutes
--------------------------

.. list-table::
   :widths: 60 40
   :header-rows: 0

   * - * **playbooks** (in YAML)
       * **tasks** describe the desired state
       * **modules** for everything: users, packages, config entries in files, etc.
       * modules are grouped, structured and reused: **plays** and **roles**
       * the top-level entities are in a static or dynamic **inventory**
       * multiple (and sometimes confusing) options for parameterization
     - .. code-block:: yaml

         ---
         - name: Update web servers
           hosts: webservers
           remote_user: root
         
           tasks:
           - name: Ensure apache is at the latest version
             ansible.builtin.yum:
               name: httpd
               state: latest
           - name: Write the apache config file
             ansible.builtin.template:
               src: /srv/httpd.j2
               dest: /etc/httpd.conf

More
----

haha
