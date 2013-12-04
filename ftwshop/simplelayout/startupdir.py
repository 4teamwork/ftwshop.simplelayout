from ftw.shop.interfaces import IShopRoot
from ftwshop.simplelayout.interfaces import IShopRootStartUpDir
from Products.CMFCore.utils import getToolByName
from zope.component import adapts
from zope.interface import implements
from zope.interface import Interface


class DefaultStartUpDirectory(object):

    implements(IShopRootStartUpDir)
    adapts(Interface, Interface)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_startup_directory(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        portal = self.context.restrictedTraverse(
            '@@plone_portal_state').portal()

        shoproots = catalog(
            {'object_provides': IShopRoot.__identifier__,
             'sort_on': 'path'})

        if shoproots:
            return shoproots[0].getPath()
        else:
            return '/'.join(portal.getPhysicalPath())
