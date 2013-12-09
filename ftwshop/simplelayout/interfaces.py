# -*- coding: utf-8 -*-
from plone.theme.interfaces import IDefaultPloneLayer
from zope.interface import Interface


class IFtwShopSimplelayoutSpecific(IDefaultPloneLayer):
    """Marker interface for a zope 3 browser layer.
    """


class IShopItemBlock(Interface):
    """A simple shop item block
    """


class IShopRootStartUpDir(Interface):
    """Gets the startup directory for the shopitemblock"""

    def __init__(context, request):
        """Adapts context and request"""

    def get_startup_directory():
        """Returns the startup directory"""
