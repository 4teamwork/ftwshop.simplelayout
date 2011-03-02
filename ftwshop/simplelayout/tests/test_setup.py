import unittest

from plone.browserlayer.utils import registered_layers

from ftwshop.simplelayout.tests.base import FtwShopSimplelayoutTestCase
from ftwshop.simplelayout.interfaces import IFtwShopSimplelayoutSpecific


class TestSetup(FtwShopSimplelayoutTestCase):

    def afterSetUp(self):
        super(TestSetup, self).afterSetUp()

    def test_browser_layer_installed(self):
        self.assertTrue(IFtwShopSimplelayoutSpecific in registered_layers())

    def test_add_shopitemblock_type_permissisons(self):
        # The API of the permissionsOfRole() function sucks - it is bound too
        # closely up in the permission management screen's user interface
        roles = ['Manager', 'Contributor']
        for r in roles:
            selected_permissions = [p['name'] for p in
                                    self.portal.permissionsOfRole(r) if p['selected']]
            self.failUnless('ftwshop.simplelayout: Add Shop Item Block' in selected_permissions)

    def test_shopitemblock_types_installed(self):
        self.failUnless('ShopItemBlock' in self.types.objectIds())

    def test_shop_category_fti(self):
        document_fti = getattr(self.types, 'ShopItemBlock')
        self.failUnless(document_fti.global_allow)

    def test_shop_item_block_creation(self):
        self.setRoles(('Manager', ))
        self.portal.invokeFactory('ShopItemBlock', 'test-shopitemblock')
        self.setRoles(('Member', ))
        self.failUnless(self.portal['test-shopitemblock'].id == 'test-shopitemblock')


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
