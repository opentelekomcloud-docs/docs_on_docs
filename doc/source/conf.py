# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'otcdocstheme'
]

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Documentation about documentation'
copyright = u'2021, Various members of the OpenTelekomCloud'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Locations to exclude when looking for source files.
exclude_patterns = ['_build']

# Options for HTML output
html_theme = 'otcdocs'
html_theme_options = {
    "sidebar_mode": "toctree"
}
otcdocs_auto_name = False

html_static_path = []

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [
    ('index',
     '%s.tex' % project,
     u'%s Documentation' % project,
     u'OpenTelekomCloud', 'manual'),
]
