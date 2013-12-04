from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.testing import z2
from zope.configuration import xmlconfig
import os


class FtwshopSimplelayoutLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUp(self):
        super(FtwshopSimplelayoutLayer, self).setUp()
        os.environ['disable-publisher-for-testing'] = 'True'

    def tearDown(self):
        del os.environ['disable-publisher-for-testing']
        super(FtwshopSimplelayoutLayer, self).tearDown()

    def setUpZope(self, app, configurationContext):

        xmlconfig.string(
            '<configure xmlns="http://namespaces.zope.org/zope">'
            '  <include package="z3c.autoinclude" file="meta.zcml" />'
            '  <includePlugins package="plone" />'
            '  <includePluginsOverrides package="plone" />'
            '</configure>',
            context=configurationContext)
        import Products.CMFCore
        xmlconfig.file('permissions.zcml',
                       Products.CMFCore,
                       context=configurationContext)
        # Load packages

        z2.installProduct(app, 'ftw.shop')
        z2.installProduct(app, 'ftwshop.simplelayout')

    def setUpPloneSite(self, portal):
        applyProfile(portal, "ftwshop.simplelayout:default")

FTWSHOP_SIMPLELAYOUT_FIXTURE = FtwshopSimplelayoutLayer()
FTWSHOP_SIMPLELAYOUT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(FTWSHOP_SIMPLELAYOUT_FIXTURE, ),
    name="ftwshop.simplelayout:integration")
