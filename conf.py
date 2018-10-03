# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys, os

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

sys.path.append(os.path.abspath(os.pardir))

__version__ = '1.0'

# -- General configuration -----------------------------------------------------

source_suffix = '.rst'
master_doc = 'index'
project = 'Da Google_Docs a Read_the_Docs'
copyright = '[cirospat - licenza CC-BY-SA]'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

extlinks = {}

# -- Version Control System Integration (https://docs.readthedocs.io/en/latest/vcs.html?highlight=conf_py_path) aggiunto 3_10_2018 ----
# html_context = {
#    "display_github": True, # Integrate GitHub
#    "github_user": "cirospat", # Username
#    "github_repo": "googledocs-to-readthedocs", # Repo name
#    "github_version": "master", # Version
#    "conf_py_path": "/googledocs-to-readthedocs/", # Path in the checkout to the docs root
# }


# -- Options for HTML output ---------------------------------------------------

html_theme = 'default'

html_static_path = ['static']

def setup(app):
    # overrides for wide tables in RTD theme
    app.add_stylesheet('theme_overrides.css') # path relative to static

"""
  You might want to uncomment the “latex_documents = []” if you use CKJ characters in your document.
  Because the pdflatex raises exception when generate Latex documents with CKJ characters.
"""
#latex_documents = []
latex_logo = "static/ods.png"
html_logo = "static/ods.png"

templates_path = ['_templates']
