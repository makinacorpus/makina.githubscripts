"""
Plone.testing is a testing framework, it is not related to plone
"""
from plone.testing.layer import Layer as Base


def print_contents(browser, dest='~/.browser.html'):
    """Print the browser contents somewhere for you to see its context
    in doctest pdb, type print_contents(browser) and that's it, open firefox
    with file://~/browser.html."""
    import os
    open(os.path.expanduser(dest), 'w').write(browser.contents)


class Layer(Base):

    defaultBases = tuple()


MAKINA_GITHUBSCRIPTS_FIXTURE = Layer()


class IntegrationLayer(Layer):
    """."""
    defaultBases = (MAKINA_GITHUBSCRIPTS_FIXTURE,)


class FunctionnalLayer(IntegrationLayer):
    """."""
    defaultBases = (MAKINA_GITHUBSCRIPTS_FIXTURE,)

MAKINA_GITHUBSCRIPTS_INTEGRATION_TESTING = IntegrationLayer()
MAKINA_GITHUBSCRIPTS_FUNCTIONAL_TESTING = FunctionnalLayer()
