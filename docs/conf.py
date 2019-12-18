# pylama:ignore=W0611
#
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sphinx_rtd_theme
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))


# -- Project information -----------------------------------------------------

project = 'labstepPy'
copyright = '2019, Barney Walker'
author = 'Barney Walker'

# The full version, including alpha/beta/rc tags
release = '2.0.0'

master_doc = 'index'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage',
              'sphinx.ext.napoleon', 'sphinx_rtd_theme',
              'sphinxcontrib.programoutput']

# Napoleon settings
napoleon_google_docstring = True
napoleon_use_param = False
napoleon_use_ivar = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# This value automatically sorts the documented members
# by alphabetical (value 'alphabetical'),
# by member type (value 'groupwise'), or
# by source order (value 'bysource').
# The default is alphabetical.
autodoc_member_order = 'bysource'

# -- Options for HTML output -------------------------------------------------

html_logo = './logo-padding.png'

# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
builtin_themes = ['alabaster',
                  'classic',
                  'sphinx_rtd_theme']
html_theme = builtin_themes[1]

if html_theme is 'classic':
    darkblue = '#000033'
    blue = '#0066cc'
    cyan = '#00ccff'

    html_theme_options = {
        # Footer
        'footerbgcolor': darkblue,
        # Sidebar
        'stickysidebar': True,
        'sidebarbgcolor': darkblue,
        'sidebarlinkcolor': 'white',
        # Relation bar
        'relbarbgcolor': '#00001a',
        'relbartextcolor': 'white',
        'relbarlinkcolor': 'white',
        # Body Text
        'textcolor': 'black',
        'linkcolor': blue,
        'visitedlinkcolor': blue,
        'externalrefs': True,
        # Headings
        'headbgcolor': '#f2f2f2',  # light grey
        'headtextcolor': darkblue,
        # Code blocks
        'codebgcolor': '#f2f2f2',  # light grey
    }

elif html_theme is 'sphinx_rtd_theme':
    # https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
    html_theme_options = {
        # 'canonical_url': '',
        # 'analytics_id': 'UA-XXXXXXX-1',
        'logo_only': False,
        'display_version': True,
        'prev_next_buttons_location': 'bottom',
        'style_external_links': True,
        'style_nav_header_background': '#2980B9',  # or 'white'
        # -----------
        # Toc options
        # -----------
        'collapse_navigation': False,
        'sticky_navigation': False,
        'navigation_depth': 3,
        'includehidden': True,
        'titles_only': False
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
