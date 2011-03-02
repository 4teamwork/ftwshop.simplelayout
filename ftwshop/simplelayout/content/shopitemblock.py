"""Definition of the Shop Item Block content type
"""

from Products.ATContentTypes.content.document import ATDocument
from Products.ATContentTypes.content.document import ATDocumentSchema
from zope.interface import implements
from Products.Archetypes import atapi

from simplelayout.base.interfaces import ISimpleLayoutBlock

from Products.ATContentTypes.config import HAS_LINGUA_PLONE
if HAS_LINGUA_PLONE:
    from Products.LinguaPlone.public import registerType
else:
    from Products.Archetypes.atapi import registerType

from ftwshop.simplelayout.interfaces import IShopItemBlock
from ftwshop.simplelayout.config import PROJECTNAME
from ftwshop.simplelayout import shopMessageFactory as _

ShopItemBlockSchema = ATDocumentSchema.copy() + atapi.Schema((

    atapi.ReferenceField('item',
        required = 1,
        languageIndependent=True,
        relationship = 'itemblock_item',
        allowed_types = ['ShopItem'],
        widget = atapi.ReferenceWidget(
            label = _(u"label_item", default=u"Shop Item"),
            description = _(u"desc_item", default=u""),
            checkbox_bound = 10,
        ),
    ),
))


class ShopItemBlock(ATDocument):
    """A simple shop item block"""
    implements(IShopItemBlock, ISimpleLayoutBlock)

    meta_type = "ShopItemBlock"
    schema = ShopItemBlockSchema


#ShopItemBlockSchema['title'].widget.visible = {'view': 'invisible', 'edit': 'invisible'}
ShopItemBlockSchema['text'].widget.visible = {'view': 'invisible', 'edit': 'invisible'}
ShopItemBlockSchema['description'].widget.visible = {'view': 'invisible', 'edit': 'invisible'}
ShopItemBlockSchema['excludeFromNav'].default = True


registerType(ShopItemBlock, PROJECTNAME)
