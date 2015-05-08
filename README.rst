ftwshop.simplelayout
====================

Integrates `ftw.shop <https://github.com/4teamwork/ftw.shop>`_ into
`simplelayout <https://github.com/4teamwork/simplelayout.base>`_.


The package provides a simplelayout block ``ShopItemBlock`` which
represents and references a normal ftw.shop ``ShopItem``. The Block
shows the price of the shop item, the image and a button for adding it to the
shopping cart.

To set the ShopItem reference easily, the startup directory is set to the IShopRoot
marked content.
You can change this by implementing your own IShopRootStartUpDir adapter.


Usage
-----

- Add ``ftwshop.simplelayout`` to your buildout configuration:

::

    [instance]
    eggs +=
        ftwshop.simplelayout

- Install the generic import profile.



Compatibility
-------------

Runs with `Plone <http://www.plone.org/>`_ `4.1`, `4.2` or `4.3`.



Links
-----

- Github: https://github.com/4teamwork/ftwshop.simplelayout
- Issues: https://github.com/4teamwork/ftwshop.simplelayout/issues
- Pypi: http://pypi.python.org/pypi/ftwshop.simplelayout
- Continuous integration: https://jenkins.4teamwork.ch/search?q=ftwshop.simplelayout


Copyright
---------

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftwshop.simplelayout`` is licensed under GNU General Public License, version 2.
