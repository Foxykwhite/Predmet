# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath('../../djangotutorial'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django
django.setup()
     
project = 'djangotutorial'
copyright = '2025, alekseyf'
author = 'alekseyf'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    'sphinxcontrib_django'
]

autodoc_member_order = 'bysource'  # Порядок следования членов по исходному коду
autodoc_default_options = {
    'members': True,  # Включает все члены класса
    'undoc-members': True,  # Включает даже не задокументированные члены
    'show-inheritance': True,  # Показывает наследование классов
}

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
# html_static_path = ['_static']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
