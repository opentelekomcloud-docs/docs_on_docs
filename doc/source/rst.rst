=====================
Understanding the RST
=====================

.. _Integrating images:

Integrating images
==================

- If you simply want to implement a picture you can use following syntax:

    .. code-block:: rst
        
        |imagexx|

       .. |imagexx| image:: /_static/images/filename

   .. note:: This is an easy way to implement pictures espacially in tables. Ideally the file path would be at the bottom of your file. 

- Alternatively you can use the image-directive

    .. code-block:: rst 

        .. image:: path/filename.proposing-changes-to-your-work-with-pull-requests
            :width: 400
            :alt: optinal alternative text 


- The more elegant way is to use figures with following syntax:

    .. code-block:: rst 

        .. figure:: /_static/images/filename

            :alt: This is the alt text visible if you hover over the picture

Using lists 
===========

Ordered lists 
-------------

Use hash symbols to generate ordered lists: 

.. code-block::

    #. Step 1. 
    #. Step 2. 
    #. Step 3. 

Resulting in: 

    #. Step 1. 
    #. Step 2. 
    #. Step 3. 

Unordered lists
---------------

Use astrisks for bulleted lists: 

.. code-block:: rst

    * Item 1. 
    * Item 2. 
    * Item 3. 

Restlting in: 

    * Item 1. 
    * Item 2. 
    * Item 3.   

.. Note:: It is also possible to nest these types of lists in another. 


Integrating Admonitions 
=======================

vanilla restructuredtext has ten standard admonitions and one generic. 
If you want to raise awereness or hint to something you can use following Admonitions:

        - attention

        - caution

        - danger

        - error

        - hint

        - important

        - note

        - tip

        - warning

        - seealso
         
        - admonition

Looking like: 

    .. attention::      This is an attention admonition

    .. caution::        This is an caution admonition 

    .. danger::         This is an danger admonition

    .. error::          This is an error admonition
    
    .. hint::           This is an hint admonition

    .. important::      This is an erros admonition
    
    .. note::           This is an note admonition

    .. tip::            This is an note admonition

    .. warning::        This is an warning admonition

    .. seealso::        This is an see also admonition

    .. admonition::     generic admonition

        This is an generic admonition


    
Using following syntax these admonitions can be implemented: 

    .. code-block::

        .. note::

            This is a note


- You can use an generic admonition with following syntax:

    .. code-block::

        .. admonition:: generic admonition title

            generic admonition content 

    
    
Integrating Tables
==================

There are a few ways of implementing tables in RST: 

1. simple tables 


    .. code-block:: rst 

        ======  ======  =====
        A       B       C
        ======  ======  =====
        false   false   false
        false   false   true
        false   true    false
        false   true    true
        true    false   false
        true    true    false
        true    true    true
        =====   =====   =====

2. grid tables 


    .. code-block:: rst

        +------------------------+------------+----------+----------+
        | Header row, column 1   | Header 2   | Header 3 | Header 4 |
        | (header rows optional) |            |          |          |
        +========================+============+==========+==========+
        | body row 1, column 1   | column 2   | column 3 | column 4 |
        +------------------------+------------+----------+----------+
        | body row 2             | ...        | ...      |          |
        +------------------------+------------+----------+----------+

    

3. csv tables


    .. code-block:: rst
        
        .. csv-table:: Frozen Delights!
        :header: "Header 1", "Header 2", "Description"
        :widths: 15, 10, 30

        "content", 2.99, "content"
        "content", 1.49, "a text that streches across two columns
        which is totally necceariy due to the imptance of this table"
        "content", 1.99, "content"


4. table-directive

    you can also use the table-directive. 
    This directive has some options for specification like 

    widths: auto, grid or a list of intigres
    
    auto or grid would be to easiest to implememt depending on the content

    For example: 

    .. code-block:: 

        .. table:: Truth table for "not"
        :widths: auto

        =====  =====
            A    not A
        =====  =====
        False  True
        True   False
        =====  =====

    Resulting in: 

    .. table:: Truth table for "not"
        :widths: auto

        =====  =====
         A     not A
        =====  =====
        False  True
        True   False
        =====  =====


Integrating Links
=================

Links to sections in the same document 
You can link from text to a heading of any part of the same document using the :ref: command. 

As an example:

.. code-block::

    :ref:`heading of a diffrent part of the document`

would result in: 

    :ref:`Integrating images`

Anchors
-------

When you have two sections with the same title in a project you will get build erros 
when you have a link to either section. Sphinx does not know to which your link does refer to. 

For example: 

.. code-block:: rst

    .. _RST Overview:

    Overview
    **********

    RST Overview content


    .. _Sphinx Overview:

    Overview
    *********

    Sphinx Overview content

If you want to use the ref-command, you would use te anchor text- 
As an example: 

.. code-block:: rst

    This is a link to the RST Overview: :ref: `RST Overview`

    This is a link to the Sphinx Overview: :ref: `Sphinx Overview`


Links to external hyperlinks
----------------------------

External hyperlinks, like `OTC
<https://www.open-telekom-cloud.com/>`_ 


.. code-block:: rst 

    External hyperlinks, like `OTC
    <https://www.open-telekom-cloud.com/>`_



toctree
=======

Vanilla reST does not offer any way to interconnect multiple files or split one file up. 
Therefore, sphinx uses a custom directive called toctree to add relations between documents. 
Also toctree is used for tables of content. 

The maxdepth function is used to limit the depth. 
This helps to improve navigability of the resulting page. 
As a best practice we agreed on **x** on maxdepth. 

As an example the index.rst file of this site: 

    .. code-block:: rst

        ..toctree::

          :maxdepth: 1


          structure
          change_proposal_process
          reviewer
          approver
          git_account
          code_editors
          rst
          migration
          presentations/index

.. seealso:: `Sphiny Docs <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#table-of-contents>`_


Markdown + RST
==============

Markdown and RST both are lightweight markup languages that empathize plain text readabilty. 

Markdown is mainly used to be formated for the web and it supports inline html

Restructuredtext is used in technical documentation like this documentation. 

Useful Links
============

https://www.sphinx-doc.org/en/master/usage/restructuredtext/

https://restructuredtext.documatt.com/

https://www.sphinx-doc.org/en/1.0/markup/toctree.html

https://www.zverovich.net/2016/06/16/rst-vs-markdown.html

https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#tables

https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#links-to-sections-in-the-same-document

https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#use-a-custom-anchor

https://sublime-and-sphinx-guide.readthedocs.io/en/latest/editor_settings.html

https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#use-custom-link-text

https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#links-to-external-web-pages

https://docutils.sourceforge.io/docs/user/rst/quickref.html


