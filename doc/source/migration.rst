=================
Migration process
=================

  
1. Cone docs-exports repository 

  To start the Migration Process you have to clone the Docs-Exports
  This can be achived with the following command 

  git clone https://github.com/opentelekomcloud-docs/doc-exports


2. Run the Conversion Script

  In the Doc-Export Repository is a Script which is used to convert the HTML files to the new format. 

  The script can be run with the following comand:

  python3 process.py xxx/umn/

  Note: you have to change the file dirctory xxx/umn/ to your dirctive. 


3. Create a new Repository


4. Choose a License 

  Apache 2.0 License


5. Choose a Template. 

  **Which?**


6. Clone your new Repository.

  The script can be run with the following comand
  
  git clone https://github.com/opentelekomcloud-docs/xxx


7. Run conversion script 

  For the next step you need to know where you saved the Doc Doc-Export Repository. 

  The file path to the Doc Export is needed for the following command

  cp -av file_path/doc-exports/xxx/umn/result umn/source

   Note: Depending on your Documentation you will use /umn/ or /api-ref/

   umn is for usermanuals 

   api-ref is for API Reference

   xxx would stand for your service
    
