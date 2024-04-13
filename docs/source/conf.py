"""
Module conf.py

Notes
------

Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

Project information:
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

"""


'''
Basic
'''
project = 'Questions and notes for potential business machine learning projects<br><br>'
project_copyright = '2023, greyhypotheses'
author = 'The Artificial Intelligence Unit'
release = 'v0.1.2'


'''
General configuration
https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

Sphinx extension modules. Extensions are either Sphinx extensions, named 'sphinx.ext.*', 
or custom ones.  Note, myst_enable_extensions excludes 'linkify'
'''
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx_design',
    'sphinxcontrib.mermaid',
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
    'attrs_block',
    'attrs_inline'
]

'''
Mathematics
'''
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'
myst_dmath_double_inline = True


'''
Templates
'''
templates_path = ['_templates']
exclude_patterns = []


'''
Options for HTML output
https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

'''

html_theme = 'sphinx_book_theme'

html_static_path: list[str] = ['_static']

html_css_files: list[str] = [
    'css/generic.css',
    'css/figures.css',
    'https://fonts.googleapis.com/css?family=Vollkorn',
    'https://fonts.googleapis.com/css?family=Tangerine',
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
                            'https://unpkg.com/tabulator-tables/dist/js/tabulator.min.js'
                            ]

html_theme_options = {
    "repository_url": "https://github.com/thereferences/systems",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "repository_branch": "master",
    "path_to_docs": "docs",
    "home_page_in_toc": False
}

html_logo = ''

html_context = {
    'landing_page': {
        'menu': [
            {'title': 'Introduction',
             'url': 'introduction/introduction.html'},
            {'title': 'Search',
             'url': 'search.html'}
        ]
    }
}
