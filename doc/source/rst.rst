=====================
Understanding the RST
=====================

Introduction
============

**reStructuredText** (**RST**, **ReST** or **reST** ) is a file format for textual data commonly used for technical documentation, for example, in documentation of Python libraries, however it is suitable for a wide range of complex texts. Since 2008, reST has been a core component of Python's Sphinx document generation system. **reST** as markup language is being used in all documentation project of the OTC Helpcenter as source file which are subsequently used to generate **HTML** using **Sphinx**.

**reST** stands out in three main aspects:

* **It's fully-featured.** It comes with many built-in features for writing more complex documents, like using footnotes, tables, citations, table of contents, etc. 
* **It's standardized and uniform.** It has a fairly `comprehensive spec <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`_ and a single canonical implementation that is still being actively developed - the `docutils <http://docutils.sourceforge.net/>`_ project.
* **It has built-in support for extensions.** Extension is a core design principle, and both custom roles (for inline elements) and directives (for block elements) can be easily added. It's therefore straightforward to add extensions for commonly-needed stuff like syntax-highlighted code blocks, math equations for Latex rendering and so on.
* **reST** is the default plaintext markup language used by `Sphinx <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_, the Python Documentation Generator used by OTC Helpcenter projects.

The following page will show how to work with commonly used syntax of **reST** in OTC Helpcenter projects, more comprehensive documentation can be found:

* `Docutils RST`_
* `Sphinx RST`_
* `Create Documentation with RST, Sphinx, Sublime and GitHub`_

Paragraphs
==========

The paragraph is the most basic block in a reST document. Paragraphs are simply chunks of text separated by one or more blank lines. As in Python, indentation is significant in reST, so all lines of the same paragraph must be left-aligned to the same level of indentation.

Inline markup
=============

The standard reST inline markup is quite simple to use:

.. code-block:: rst

   one asterisk: *text* for emphasis (italics),

   two asterisks: **text** for strong emphasis (boldface), and

   backquotes: ``text`` for code samples.

Lists and Quote-like blocks
===========================

List markup is natural, just place an asterisk at the start of a paragraph and indent properly. The same goes for numbered lists; they can also be autonumbered using a # sign:

.. code-block:: rst

   * This is a bulleted list.
   * It has two items, the second
     item uses two lines.
   
   1. This is a numbered list.
   2. It has two items too.
   
   #. This is a numbered list.
   #. It has two items too.

.. Note:: It is also possible to nest these types of lists in another. 

Headings, Sections, Subsections
===============================

Headings are created by underlining and overlining the title with a **=** character, at least as long as the text:

.. code-block:: rst

   =================
   This is a Heading
   =================

Sections are created by underlining the title with a **=** character, at least as long as the text:

.. code-block:: rst

   This is a Section
   =================

Subsections are created by underlining the title with a **-** character, at least as long as the text:

.. code-block:: rst

   This is a Subsection
   --------------------


Tables
======

There are multiple ways of implementing tables in **reST**

1. **Simple tables** are easier to write, but limited: they must contain more than one row, and the first column cells cannot contain multiple lines. They look like this:


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

2. For **grid tables**, the cell grid has to be "painted". They look like this:


    .. code-block:: rst

        +------------------------+------------+----------+----------+
        | Header row, column 1   | Header 2   | Header 3 | Header 4 |
        | (header rows optional) |            |          |          |
        +========================+============+==========+==========+
        | body row 1, column 1   | column 2   | column 3 | column 4 |
        +------------------------+------------+----------+----------+
        | body row 2             | ...        | ...      |          |
        +------------------------+------------+----------+----------+

    

3. The **csv-table** directive is used to create a table from CSV (comma-separated values) data. They look like this:


    .. code-block:: rst
        
        .. csv-table:: Frozen Delights!
        :header: "Header 1", "Header 2", "Description"
        :widths: 15, 10, 30

        "content", 2.99, "content"
        "content", 1.49, "a text that streches across two columns
        which is totally necceariy due to the imptance of this table"
        "content", 1.99, "content"


Usage of table-directive
------------------------

Table directive serves as optional wrapper of the *grid* and *simple* syntaxes. Additional meta information can be defined for the table, like alignment, caption or width.

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

.. note:: 

   Cell merging within the tables is not supported. 

Code block
==========

The **.. code-block::** directive constructs a literal block. If the code language is specified, the content is parsed by the `Pygments <https://pygments.org/>`_ syntax highlighter.

Example:

.. code-block:: rst

   .. code-block:: bash
      
      $ echo "Hello world!"


.. _Images:

Images
======

There are multiple ways to use images in the documents.

* Add images to **reST** text  with the **.. image::** directive:

    .. code-block:: rst 

        .. image:: /_static/images/filename.png
           :alt: optinal alternative text 

    .. note:: 
       Default image location of most documentation projects is /_static/images`. This directory is in each documentation type of the project, for example  `/umn/source/_static/images`


- Define a **substitution** to reference an image:

    .. code-block:: rst
        
       .. |imagexx| image:: /_static/images/filename.png


       The image referenced above goes here |imagexx|

    .. note:: 
       This is useful if you are using the image multiple times in a project and want to manage it in one location.


- Use **figures**, image with capation and optional legend: 

    .. code-block:: rst 

        .. figure:: /_static/images/filename.png
           :alt: This is the alt text visible if you hover over the picture
           
           This is the caption of the figure (a simple paragraph).


Admonitions 
===========

Admonitions are specially marked "topics" that can appear anywhere an ordinary body element can. Typically, an admonition is rendered as an offset block in a document, sometimes outlined or shaded, with a title matching the admonition type. For example:

.. code-block:: rst

   .. danger::
      Beware killer rabbits!

The above definition would be rendered like:

.. danger::
   Beware killer rabbits!

Admonition types: **"attention", "caution", "danger", "error", "hint", "important", "note", "tip", "warning", "seealso", "admonition"**

Rendered adminitions will look like: 

    .. attention::      This is an attention admonition

    .. caution::        This is a caution admonition 

    .. danger::         This is a danger admonition

    .. error::          This is an error admonition
    
    .. hint::           This is a hint admonition

    .. important::      This is an important admonition
    
    .. note::           This is a note admonition

    .. tip::            This is a tip admonition

    .. warning::        This is a warning admonition

    .. seealso::        This is a seealso admonition

    .. admonition::     Generic admonition

       This is a generic admonition


Hyperlinks
==========

There are two types of hyperlinks:

* Which point to external targets, outside of the **reST** document
* Which point to internal targets, inside of the **reST** document using labels to figures, tables, sections, etc

External hyperlink targets
--------------------------

External hyperlink targets, like `OTC <https://www.open-telekom-cloud.com/>`_ 

.. code-block:: rst 

   External hyperlinks, like `OTC <https://www.open-telekom-cloud.com/>`_

.. important::
   There must be a space between the link text and the opening < for the URL.

It as also possible to separate the link and the target definition, like this:

.. code-block:: rst
   
   This is a paragraph that contains link to `OTC`_.

   .. _OTC: https://www.open-telekom-cloud.com/


Separating the link and the target definition is useful, when you intend to use the same link on different location of the same document. 

Internal hyperlink targets
--------------------------

Internal hyperlink targets allow to connect one place to another within the document. To support cross-referencing to arbitrary locations in any document, the standard reST labels are used. For this to work label names must be unique throughout the entire documentation. There are two ways in which labels can be referred to:

* Place the label directly before the section title, table or figure and it can be referenced with **:ref:`label-name`**. For example:

  .. code-block:: rst
  
      .. _RST Overview:
  
      Overview
      ********
  
      RST Overview content
  
  
      For Overview of RST, see :ref:`RST Overview`
  

* Labels that aren’t placed before a section title can still be referenced, but the link must get an explicit title, using this syntax: **:ref:`Link title <label-name>`**.


.. note::

   Reference labels must start with an underscore. When referencing a label, the underscore must be omitted (see examples above).


Table of contents - toctree
===========================

Since reST does not have facilities to interconnect several documents, or split documents into multiple output files, Sphinx uses a custom directive to add relations between the single files the documentation is made of, as well as tables of contents. The toctree directive is the central element.

A numeric maxdepth option may be given to indicate the depth of the tree; by default, all levels are included.

Each directory of the documentation project contains an index.html file in which all available pages/files are listed under **..toctree::** directive. A toctree entry can also point to another directory index page like in the example below **presentations/index**. 

As an example the index.rst file of this document: 

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


Useful Links
============

* `Docutils RST`_
* `Sphinx RST`_
* `Create Documentation with RST, Sphinx, Sublime and GitHub`_
* `Guide to reStructuredText and Sphinx`_
* `RST vs Markdown`_


.. _Docutils RST: https://docutils.sourceforge.io/rst.html
.. _Sphinx RST: https://www.sphinx-doc.org/en/master/usage/restructuredtext/
.. _Create Documentation with RST, Sphinx, Sublime and Github: https://sublime-and-sphinx-guide.readthedocs.io/en/latest/
.. _Guide to reStructuredText and Sphinx: https://restructuredtext.documatt.com/
.. _RST vs Markdown: https://www.zverovich.net/2016/06/16/rst-vs-markdown.html
