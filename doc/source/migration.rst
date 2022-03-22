=================
Migration process
=================

  
#. Clone docs-exports repository 

    * To start the Migration Process you have to clone the Docs-Exports


     This can be achived with the following command:
  
      .. code-block:: bash

      git clone https://github.com/opentelekomcloud-docs/doc-exports


#. Run the Conversion Script

    * In the Doc-Export Repository is a Script which is used to convert the HTML files to the new format. 

     The script can be run with the following comand:
  
      .. code-block:: bash

      python3 process.py xxx/umn/
  
    * Note: you have to change the file directory xxx/umn/ to your directory. 


#. Contact Ecosystem Squad
 
    * Ecosystem Squad will gladly assist you with the next step:
  
     They handle creating a repoitory for your spefic service for a ready to use Environment. 


#. Clone your new Repository.

    * After your repoistory was created you have to clone it. 
  
     The script can be run with the following comand:
  
      .. code-block::

      git clone https://github.com/opentelekomcloud-docs/xxx


#. Import conversion results 

    * For the next step you need to know where you saved the Doc Doc-Export Repository. 

       The file path to the Doc Export is needed for the following command:
  
      .. code-block:: python 

      cp -av file_path/doc-exports/xxx/umn/result umn/source

      cp -av file_path/doc-exports/xxx/umn/\*.{png,gif,svg} umn/source/_static/images 

    * Note: Depending on your Documentation you will use /umn/ or /api-ref/

      - umn is for usermanuals 

      - api-ref is for API Reference

      - xxx would stand for your service
    
#. Try to build imported files locally

    * To ensure the conversion build is not broken you have to build them locally. 
     
     Depening on the type of documents you can use following commands: 

      .. code-block:: bash

      tox -e umn 

      tox -e api-ref
