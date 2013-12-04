from ftwshop.simplelayout.testing import (
    FTWSHOP_SIMPLELAYOUT_INTEGRATION_TESTING)
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID, TEST_USER_NAME
from StringIO import StringIO
from unittest2 import TestCase


class TestShopItemBlock(TestCase):

    layer = FTWSHOP_SIMPLELAYOUT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)
        shopitem_fti = getattr(self.portal.portal_types, 'ShopItem')
        shopitem_fti.global_allow = True

        shopitemblock_fti = getattr(self.portal.portal_types, 'ShopItemBlock')
        shopitemblock_fti.global_allow = True

        self.folder = self.portal.get(
            self.portal.invokeFactory('Folder', 'myfolder'))

        file_ = StringIO(
                    'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\x00\x00'
                    '\x00!\xf9\x04\x04\x00\x00\x00\x00,\x00\x00\x00\x00\x01'
                    '\x00\x01\x00\x00\x02\x02D\x01\x00;')

        self.item = self.folder.get(
            self.folder.invokeFactory('ShopItem', 'myshopitem', image=file_))
        self.page = self.portal.get(
            self.portal.invokeFactory('Document', 'mypage'))
        self.itemblock = self.page.get(
            self.page.invokeFactory('ShopItemBlock',
                                    'myblock',
                                    item=self.item))

    def test_get_item(self):
        view = self.itemblock.restrictedTraverse("block_view")
        self.assertEqual(self.item, view.get_item())

    def test_get_image_tag(self):
        view = self.itemblock.restrictedTraverse("block_view")
        tag = view.get_image_tag()
        self.assertIn('height="1" width="1"', tag)
        self.assertIn('@@images', tag)

    def test_get_image_tag_no_image(self):
        item2 = self.folder.get(
            self.folder.invokeFactory('ShopItem', 'myshopitem2'))
        block2 = self.page.get(
            self.page.invokeFactory('ShopItemBlock', 'myblock2', item=item2))
        view = block2.restrictedTraverse("block_view")
        self.assertEqual('', view.get_image_tag())

    def test_get_image_url(self):
        view = self.itemblock.restrictedTraverse("block_view")
        self.assertEqual("http://nohost/plone/myfolder/myshopitem/image",
                         view.get_image_url())

    def test_get_items(self):
        view = self.itemblock.restrictedTraverse("block_view")
        self.assertEqual(self.item, view.getItems()[0])
        self.assertEqual(1, len(view.getItems()))
