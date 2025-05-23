# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Wind & Ocean Engineering empowered by AI'
copyright = '2025, Wind & Ocean Engineering empowered by AI Group'
author = '李朝 lichaosz@hit.edu.cn'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# Add custom CSS file
html_static_path = ['../_static']
html_css_files = ['custom.css']

html_logo = "../_static/logoGroup.png"  # Logo 文件需放置于 _static 目录
html_title = "Wind & Ocean Engineering<br><span style='color: #666;'>empowered by</span><br><span style='color: #666;'>AI</span>"

# -- Options for EPUB output
# epub_show_urls = 'footnote'

# 关闭“查看页面源代码”链接
html_show_sourcelink = False

