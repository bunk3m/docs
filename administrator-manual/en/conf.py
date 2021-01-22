# -*- coding: utf-8 -*-
#
# NethServer documentation build configuration file, created by
# sphinx-quickstart on Sun Jan 19 10:47:03 2014.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os, datetime
import sphinx_rtd_theme

copyright = u'%d, Nethesis Srl and the NethServer project contributors' % datetime.date.today().year

if not tags.has('nscom') and 'READTHEDOCS_PROJECT' in os.environ and 'enterprise' in os.environ['READTHEDOCS_PROJECT']:
    tags.add('nsent')
elif not tags.has('nsent'):
    tags.add('nscom')

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = []

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# The short X.Y version.
version = '7'
# The full version, including alpha/beta/rc tags.
release = '7 Final'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

locale_dirs = ['locale/'] 

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    '_build',
    '.tx',
    'locale',
    'nsent',
    'nscom'
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
highlight_language = 'none'

htmlhelp_basename = 'NethServer_enterprisedoc'

if tags.has('nsent'):
    smartquotes = False
    project = u'NethServer Enterprise'
    html_title = "%s %s" % (project, release)
    html_theme = "sphinx_rtd_theme"
    html_logo = 'nsent/_static/nethesis_enterprise_yellow.png'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    html_favicon = 'nsent/_static/favicon.ico' 
    html_static_path = ['nsent/_static']
    html_extra_path = ['nsent/robots.txt']
    html_css_files = ['nethesis.css']
    exclude_patterns.extend([
        'webvirtmgr.rst',
        'nscom_*.rst'
    ])
    rst_prolog = """
.. |product| replace:: NethServer Enterprise
.. |product_voice| replace:: NethVoice
.. |product_cti| replace:: NethCTI
.. |download_site| replace:: `helpdesk.nethesis.it <http://helpdesk.nethesis.it/solution/articles/3000073996-download-iso-nethserver-enterprise>`__
.. |ks_keyboard| replace:: :samp:`us`
.. |ks_timezone| replace:: :samp:`UTC`
.. |ks_language| replace:: :samp:`en_US`
.. |register_link| replace:: `my.nethesis.it <https://my.nethesis.it/>`__
"""
    latex_elements = {}
    latex_documents = [
      ('index', 'NethServer_enterprise.tex', u'Documentazione NethServer Enterprise',
       u'Nethesis', 'manual'),
    ]
    man_pages = [
        ('index', 'nethserver_enterprise', u'NethServer Enterprise Documentation',
         [u'Nethesis'], 1)
    ]
    texinfo_documents = [
      ('index', 'NethServer enterprise', u'NethServer Enterprise Documentation',
       u'Nethesis', 'NethServer Enterprise', '',
       'Miscellaneous'),
    ]
    html_theme_options = {
        'nosidebar': "1",
        'collapse_navigation': True,
        'navigation_depth': -1,
        'logo_only': True,
        'style_nav_header_background': '#343131',
    }

elif tags.has('nscom'):
    templates_path = ['nscom/_templates']
    project = u'NethServer'
    html_title = u"%s %s" % (project, release)
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    html_favicon = 'nscom/_static/favicon.ico' 
    html_static_path = ['nscom/_static']
    exclude_patterns.extend([
        'hotspot.rst',
        'weekly_report.rst',
        'nethvoice_intro.rst',
        'nethcti_intro.rst',
        'phonebook-mysql.rst',
        'registration.rst',
        'launcher.rst',
        'sandbox.rst'
    ])
    rst_prolog="""
.. |product| replace:: NethServer
.. |download_site| replace:: `www.nethserver.org <http://www.nethserver.org/getting-started-with-nethserver/>`__
.. |ks_keyboard| replace:: :samp:`en`
.. |ks_timezone| replace:: :samp:`Greenwich`
.. |ks_language| replace:: :samp:`en_US`
"""
    texinfo_documents = [
      ('index', 'NethServer', u'NethServer Documentation',
       u'Nethesis', 'NethServer', 'One line description of project.',
       'Miscellaneous'),
    ]
    latex_elements = {}
    latex_documents = [
      ('index', 'NethServer.tex', u'NethServer Documentation',
       u'Nethesis', 'manual'),
    ]

    man_pages = [
        ('index', 'nethserver', u'NethServer Documentation',
         [u'Nethesis'], 1)
    ]

#
# Define context default values for HTML templates
#
context = {
    'alt_languages': 'it,en,es',
    'alt_versions': 'v7,v6,dev',
    'current_version': 'def',
    'user_analytics_code': 'UA-37499928-4',
}

if 'html_context' in globals():
    for key in context:
        html_context.setdefault(k, context[k])
else:
    html_context = context
