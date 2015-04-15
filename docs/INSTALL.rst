makina.githubscripts Installation
=================================================================================

To install makina.githubscripts into the global Python environment (or a workingenv),
using a traditional Zope 2 instance, you can do this:

 * When you're reading this you have probably already run ::

   ``easy_install makina.githubscripts``.

   Find out how to install setuptools (and EasyInstall) here: http://peak.telecommunity.com/DevCenter/EasyInstall

 * If you are using Zope 2.9 (not 2.10), get `pythonproducts`_ and install it
   via::

       python setup.py install --home /path/to/instance

   into your Zope instance.

 * Create a file called ``makina.githubscripts-configure.zcml`` in the
   ``/path/to/instance/etc/package-includes`` directory.  The file
   should only contain this::

       <include package="makina.githubscripts" />

.. _pythonproducts: http://plone.org/products/pythonproducts


Alternatively, if you are using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

 * Add ``makina.githubscripts`` to the list of eggs to install, e.g.::

    [buildout]
    ...
    eggs =
        ...
        makina.githubscripts

 * Tell the plone.recipe.zope2instance recipe to install a ZCML slug::

    [instance]
    recipe = plone.recipe.zope2instance
    ...
    zcml =
        makina.githubscripts

 * Re-run buildout, e.g. with::

    $ ./bin/buildout

You can skip the ZCML slug if you are going to explicitly include the package
from another package's configure.zcml file.
