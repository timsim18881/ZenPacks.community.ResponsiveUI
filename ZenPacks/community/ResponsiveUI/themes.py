import os

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile


def here(fn):
    return os.path.join(os.path.dirname(__file__), fn)


class ThemesView(BrowserView):
    """
    Themes list
    http://dev.zenoss.org/trac/ticket/3142
    """

    __call__ = ZopeTwoPageTemplateFile(here('themes.pt'))

    # def __call__(self):
    #     with open(here('themes.pt')) as f:
    #         t = f.read()
    #     return t % dict(themes="")
