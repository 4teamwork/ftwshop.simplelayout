from ftw.builder import Builder
from ftw.builder import create
from ftw.shop.interfaces import IShopRoot
from ftwshop.simplelayout.interfaces import IShopRootStartUpDir
from ftwshop.simplelayout.startupdir import DefaultStartUpDirectory
from ftwshop.simplelayout.testing import (
    FTWSHOP_SIMPLELAYOUT_INTEGRATION_TESTING)
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID, TEST_USER_NAME
from unittest2 import TestCase
from zope.component import queryMultiAdapter
from zope.interface import alsoProvides
from zope.interface.verify import verifyClass


class TestShopItemBlock(TestCase):

    layer = FTWSHOP_SIMPLELAYOUT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)

        shopitemblock_fti = getattr(self.portal.portal_types, 'ShopItemBlock')
        shopitemblock_fti.global_allow = True
        shopitem_fti = getattr(self.portal.portal_types, 'ShopItem')
        shopitem_fti.global_allow = True

    def test_implements_interface(self):
        self.assertTrue(
            IShopRootStartUpDir.implementedBy(DefaultStartUpDirectory))

        verifyClass(IShopRootStartUpDir, DefaultStartUpDirectory)

    def test_component_registered(self):
        self.assertTrue(
            self._get_adapter(self.portal),
            'Default shop directory adapter is not registered correctly.')

    def test_return_plone_root_as_shop_root_by_default(self):
        self.assertEquals(
            '/plone',
            self._get_adapter(self.portal).get_startup_directory())

    def test_return_shop_root_defined_by_marker_interface(self):
        structure = self._setup_structure()
        folder = structure[0]
        self._set_shop_root(folder)

        self.assertEquals(
            '/'.join(folder.getPhysicalPath()),
            self._get_adapter(self.portal).get_startup_directory())

    def test_get_startup_directory_on_shopitemblock(self):
        structure = self._setup_structure()
        folder = structure[0]
        self._set_shop_root(folder)

        shopitemblock = create(Builder('shopitem block')
                               .with_shop_item(structure[2]))

        self.assertEquals('/'.join(folder.getPhysicalPath()),
                          shopitemblock.get_startup_directory())

    def _set_shop_root(self, obj):
        alsoProvides(obj, IShopRoot)
        obj.reindexObject()

    def _setup_structure(self):
        folder = create(Builder('folder'))
        category = create(Builder('shop category').within(folder))
        shopitem = create(Builder('shopitem').within(category))

        return folder, category, shopitem

    def _get_adapter(self, obj):
        return queryMultiAdapter((obj, obj.REQUEST), IShopRootStartUpDir)
