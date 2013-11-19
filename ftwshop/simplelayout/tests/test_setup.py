import unittest2 as unittest
from plone.browserlayer.utils import registered_layers
from ftwshop.simplelayout.interfaces import IFtwShopSimplelayoutSpecific
from ftwshop.simplelayout.testing import FTWSHOP_SIMPLELAYOUT_INTEGRATION_TESTING
from plone.app.testing import TEST_USER_ID, TEST_USER_NAME
from plone.app.testing import setRoles
from plone.app.testing import login

class TestSetup(unittest.TestCase):

    layer = FTWSHOP_SIMPLELAYOUT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)
        
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
        self.failUnless('ShopItemBlock' in self.portal.portal_types.objectIds())

    def test_shop_category_fti(self):
        document_fti = getattr(self.portal.portal_types, 'ShopItemBlock')
        self.assertFalse(document_fti.global_allow)

    def test_shop_item_block_creation(self):
        document_fti = getattr(self.portal.portal_types, 'ShopItemBlock')
        document_fti.global_allow = True
        self.portal.invokeFactory('ShopItemBlock', 'test-shopitemblock')
        document_fti.global_allow = False
        self.failUnless(self.portal['test-shopitemblock'].id == 'test-shopitemblock')

