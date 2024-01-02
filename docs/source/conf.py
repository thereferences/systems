"""
conf.py

Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

Project information
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""

import sphinx_rtd_theme
import sphinx_design
import furo


'''
Basic
'''
project = 'Mathematical Systems'
copyright = '2023, greyhypotheses'
author = 'greyhypotheses'
release = '0.1'


'''
General configuration
https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

Sphinx extension modules. Extensions are either Sphinx extensions, named 'sphinx.ext.*', 
or custom ones.  Note, myst_enable_extensions excludes 'linkify'
'''
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.githubpages',
    'sphinx_design',
    'myst_parser'
]

myst_enable_extensions = [
    'amsmath',
    'attrs_inline',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'html_admonition',
    'html_image',
    'replacements',
    'smartquotes',
    'strikethrough',
    'substitution',
    'tasklist',
]


'''
Templates
'''
templates_path = ['_templates']
exclude_patterns = []


'''
Options for HTML output
https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

'''

html_theme = 'sphinx_rtd_theme'

html_static_path: list[str] = ['_static']

html_css_files: list[str] = [
    'css/style.css',
    'https://unpkg.com/tabulator-tables/dist/css/tabulator.min.css'
]

html_js_files: list[str] = ['https://code.jquery.com/jquery-3.7.0.min.js',
                            'https://code.highcharts.com/stock/highstock.js',
                            'https://code.highcharts.com/stock/modules/data.js',
                            'https://code.highcharts.com/stock/modules/exporting.js',
                            'https://code.highcharts.com/stock/modules/export-data.js',
                            'https://code.highcharts.com/stock/modules/accessibility.js',
                            'https://code.highcharts.com/highcharts.js',
                            'https://code.highcharts.com/modules/networkgraph.js',
                            'js/latex.js',
                            'https://unpkg.com/tabulator-tables/dist/js/tabulator.min.js'
                            ]

html_theme_options = {
    'canonical_url': 'https://membranes.github.io/systems',
    'analytics_id': '',
    'style_external_links': False,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_logo = ''

html_context = {
    'landing_page': {
        'menu': [
            {'title': 'Introduction',
             'url': 'introduction/introduction.html'},
            {'title': 'Project',
             'url': 'project/project.html'},
            {'title': 'Search',
             'url': 'search.html'}
        ]
    }
}
