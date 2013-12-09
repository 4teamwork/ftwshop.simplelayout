from ftw.builder import builder_registry
from ftw.builder.archetypes import ArchetypesBuilder
from plone.uuid.interfaces import IUUID


class ShopItemBlockBuilder(ArchetypesBuilder):
    portal_type = 'ShopItemBlock'

    def with_shop_item(self, shopitem):
        assert shopitem

        self.arguments['item'] = IUUID(shopitem)
        return self


class ShopItemBuilder(ArchetypesBuilder):
    portal_type = 'ShopItem'


class ShopCategoryBuilder(ArchetypesBuilder):
    portal_type = 'ShopCategory'


builder_registry.register('shopitem block', ShopItemBlockBuilder)
builder_registry.register('shopitem', ShopItemBuilder)
builder_registry.register('shop category', ShopCategoryBuilder)
