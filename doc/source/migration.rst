=================
Migration process
=================

#. Clone docs-exports repository.

   To start the Migration Process you have to clone the Docs-Exports. This can be achieved with the following command:

   .. code-block:: bash

      git clone https://github.com/opentelekomcloud-docs/doc-exports

#. Place or update required documentation when necessary.

   All documents exported from the legacy documentation system in the html
   (chm) format are placed in this repository for the reference and eventual
   synchronization. Every service documentation is placed under own folder
   named as the short service name and further structured by the type of the
   document.

#. Run the Conversion Script.

   In the Doc-Export Repository there is a script which is used to convert the
   HTML files to the desired format. It can be executed with the following comand:

   .. code-block:: bash

      python3 process.py xxx/umn/

   **Note**: you have to change the file directory xxx/umn/ to your directory.

   **Note**: it may be necessary to install locally required python libraries.

#. Contact Ecosystem Squad for repository creation when it is not yet existing.

#. Clone target Repository.

   After your repoistory was created you have to clone it. Skip this step when
   repository is already cloned locally. In this case please ensure local state
   is up2date.

   .. code-block::

      git clone https://github.com/opentelekomcloud-docs/xxx

#. Import conversion results.

   For the next step you need to know where you saved the Doc Doc-Export
   Repository. The path to the Doc Export is needed for the following command:

   .. code-block:: python

       cp -av file_path/doc-exports/xxx/umn/result umn/source

       cp -av file_path/doc-exports/xxx/umn/ \*.{png,gif,svg} umn/source/_static/images

   **Note**: Depending on your Documentation you will use /umn/ or /api-ref/:

      - umn is for usermanuals

      - api-ref is for API Reference

      - xxx would stand for your service

#. Try to build imported files locally

   To ensure the conversion build is not broken you have to build them locally.
   Depening on the type of documents you can use following commands:

   .. code-block:: bash

      tox -e umn
      tox -e api-ref
