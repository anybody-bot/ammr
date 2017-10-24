#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# AMMR documentation build configuration file, created by
# sphinx-quickstart on Wed Aug 23 14:56:19 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------




import os
import sys
import subprocess
import cloud_sptheme


sys.path.insert(0, os.path.abspath('exts'))


try: 
    import pygments_anyscript
except ImportError:
    raise ImportError('Please install pygments_anyscript to get AnyScript highlighting')


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',

    
    # 3rd party extensions

    'cloud_sptheme.ext.index_styling',
    'cloud_sptheme.ext.relbar_toc',
    'cloud_sptheme.ext.escaped_samp_literals',
    'cloud_sptheme.ext.issue_tracker',
    'cloud_sptheme.ext.table_styling',
    'ammr-directives',
    
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'AMMR'
copyright = '2017, AnyBody Technology'
author = 'AnyBody Technology'

github_doc_root = 'https://github.com/anybody-research-group/anypytools/tree/master/docs/'


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '2.0'
# The full version, including alpha/beta/rc tags.
release = '2.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'README.rst', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
highlight_language = 'none'
pygments_style = 'AnyScript'

rst_prolog = """
.. role:: anyscript(code)
   :language: AnyScriptDoc

.. include:: /BM_Config/Substitutions.txt

.. |AMS_VERSION_X| replace:: 7.1.x
.. |AMS_VERSION_FULL| replace:: 7.1.0
.. |AMS_VERSION_SHORT| replace:: 7.1
.. |AMMR_VERSION_FULL| replace:: 2.0.0
.. |AMMR_VERSION_SHORT| replace:: 2.0
.. |AMMR_DEMO_INST_DIR| replace:: ``~/Documents/AnyBody.7.1.x/AMMR.v2.0.0-Demo``

"""


# If true, `todo` and `todoList` produce output, else they produce nothing.
try: 
    subprocess.check_call(['git', 'describe', '--exact-match', 'HEAD'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL )
except subprocess.CalledProcessError:
    # We are not a on a tagged commit
    todo_include_todos = True
else:
    # Tagged commit, e.g. release version. Hide todos.
    todo_include_todos = False



# -- Options for HTML output ----------------------------------------------


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "cloud"

html_theme_path = [cloud_sptheme.get_theme_dir()]


html_title = "%s v%s Documentation" % (project, release)

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme = "redcloud"
# html_theme_options = {
#     'roottarget': index_doc,
#     'max_width': '1100px',
#     'minimal_width': '700px',
#     'borderless_decor': True,
#     'lighter_header_decor': False,
#     'sidebarwidth': "3.8in",
#     'fontcssurl': 'https://fonts.googleapis.com/css?family=Noticia+Text|Open+Sans|Droid+Sans+Mono',
#     'relbarbgcolor': '#999999',
#     'footerbgcolor': '#953337',
#     'sidebarlinkcolor': '#953337',
#     'headtextcolor': '#953337',
#     'headlinkcolor': '#953337',
# }

html_theme_options = {
    'roottarget': master_doc,
    'max_width': '1100px',
    'minimal_width': '700px',
    'borderless_decor': True,
    'lighter_header_decor': False,
    'sidebarwidth': "3.8in",
    'fontcssurl': 'https://fonts.googleapis.com/css?family=Noticia+Text|Open+Sans|Droid+Sans+Mono',
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = '_static/ammr_logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', 'BodyModels/_static']

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {'**': ['searchbox.html', 'globaltoc.html']}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = project

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'AMMR.tex', 'AMMR Documentation',
     'AnyBody Technology', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ammr', 'AMMR Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'AMMR', 'AMMR Documentation',
     author, 'AMMR', 'One line description of project.',
     'Miscellaneous'),
]




# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}