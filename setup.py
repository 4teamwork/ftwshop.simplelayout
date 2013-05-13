import os
from setuptools import setup, find_packages


version = '1.0'


tests_require = [
    'Products.PloneTestCase',
    'plone.browserlayer',
    ]


setup(name='ftwshop.simplelayout',
      version=version,
      description="Extension to ftw.shop adding SimpleLayout support",

      long_description=open('README.rst').read() + '\n' + \
          open(os.path.join('docs', 'HISTORY.txt')).read(),

      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.1',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],

      keywords='ftw shop simplelayout',
      author='4teamwork GmbH',
      author_email='mailto:info@4teamwork.ch',
      url='https://github.com/4teamwork/ftwshop.simplelayout',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftwshop'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'Products.ATContentTypes',
        'Products.Archetypes',
        'Products.CMFCore',
        'Products.GenericSetup',
        'Products.LinguaPlone',
        'Zope2',
        'archetypes.referencebrowserwidget',
        'ftw.shop',
        'plone.app.contentmenu',
        'plone.app.layout',
        'plone.theme',
        'setuptools',
        'simplejson',
        'simplelayout.base',
        'zope.component',
        'zope.i18nmessageid',
        'zope.interface',
        ],

      tests_require=tests_require,
      extras_require=dict(tests=tests_require),

      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
