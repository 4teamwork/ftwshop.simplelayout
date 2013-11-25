from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from ftw.shop.browser.shopitem import ShopCompactItemView
from simplelayout.base.interfaces import IBlockConfig
from zope.component import queryMultiAdapter


class ShopItemBlockView(ShopCompactItemView):
    """Default view for a shop item block
    """

    __call__ = ViewPageTemplateFile('shopitemblock.pt')

    def getBlockHeight(self):
        blockconf = IBlockConfig(self.context)
        return blockconf.block_height or ''

    def get_item(self):
        """
        Return the actual ShopItem object that the reference field `item`
        points to.
        """
        item = self.context.getField('item').get(self.context)
        return item

    def getItems(self):
        """
        Returns a list with this item as its only element,
        so the listing viewlet can treat it like a list of items
        """
        context = self.get_item()
        return [context]


    def shop_js_loaded(self, loaded=False):
        """
        Make sure the shop.js only gets loaded once, so events
        don't get registered multiple times.
        """
        if loaded:
            self.request.set('shop_js_loaded', True)
        return self.request.get('shop_js_loaded', False)

    def get_image_tag(self):
        obj = self.get_item()
        if not obj.getField('image').get(obj):
            return ''
        scales = queryMultiAdapter((obj, self.request), name="images")
        return scales.scale(
            'image',
            width=200,
            height=200).tag()

    def get_image_url(self):
        return self.get_item().absolute_url() + '/image'
