"""Definition of the Shop Item Block content type
"""

from ftwshop.simplelayout import shopMessageFactory as _
from ftwshop.simplelayout.config import PROJECTNAME
from ftwshop.simplelayout.interfaces import IShopItemBlock
from Products.Archetypes import atapi
from Products.ATContentTypes.config import HAS_LINGUA_PLONE
from Products.ATContentTypes.content.document import ATDocument
from Products.ATContentTypes.content.document import ATDocumentSchema
from Products.CMFCore.permissions import ManagePortal
from simplelayout.base.interfaces import ISimpleLayoutBlock
from zope.interface import implements
if HAS_LINGUA_PLONE:
    from Products.LinguaPlone.public import registerType
else:
    from Products.Archetypes.atapi import registerType


# This part is taken from ftw.contentpage.
# Because we don't want a dependency on it.
DEFAULT_TO_HIDE = [
    'subject', 'relatedItems', 'location', 'language',  # Categorization
    'effectiveDate', 'expirationDate',  # Dates
    'creators', 'contributors', 'rights',  # Contributors
    'allowDiscussion', 'excludeFromNav',  # Settings
    'nextPreviousEnabled', 'presentation', 'tableContents',
    'showinsearch', 'searchwords'
    ]


def finalize(schema, show=None, hide=None):
    to_hide = DEFAULT_TO_HIDE
    if hide:
        to_hide += hide

    if show:
        for name in show:
            if name in to_hide:
                to_hide.remove(name)

    for name in to_hide:
        if name in schema:
            field = schema[name]
            schema.changeSchemataForField(name, 'default')
            field.widget.visible = {'view': 'invisible', 'edit': 'invisible'}
            field.write_permission = ManagePortal

    # Hide from navigation by default
    schema['excludeFromNav'].default = True


ShopItemBlockSchema = ATDocumentSchema.copy() + atapi.Schema((

    atapi.ReferenceField(
        'item',
        required=1,
        languageIndependent=True,
        relationship='itemblock_item',
        allowed_types=['ShopItem'],
        widget=atapi.ReferenceWidget(
            label=_(u"label_item", default=u"Shop Item"),
            description=_(u"desc_item", default=u""),
            checkbox_bound=10,
        ),
    ),
))


class ShopItemBlock(ATDocument):
    """A simple shop item block"""
    implements(IShopItemBlock, ISimpleLayoutBlock)

    meta_type = "ShopItemBlock"
    schema = ShopItemBlockSchema


ShopItemBlockSchema['text'].widget.visible = {'view': 'invisible',
                                              'edit': 'invisible'}
ShopItemBlockSchema['description'].widget.visible = {'view': 'invisible',
                                                     'edit': 'invisible'}

finalize(ShopItemBlockSchema)


registerType(ShopItemBlock, PROJECTNAME)
