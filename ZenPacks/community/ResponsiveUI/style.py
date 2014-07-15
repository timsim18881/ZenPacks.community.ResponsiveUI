import zope.interface

from Products.Five.viewlet.viewlet import ViewletBase
from Products.ZenUI3.browser.interfaces import IJavaScriptBundleViewlet
from Products.ZenUI3.browser.javascript import getVersionedPath


STYLE_TAG_SRC_TEMPLATE = "<link rel='stylesheet' type='text/css' href='%s' />\n"


class StyleSrcBundleViewlet(ViewletBase):
    zope.interface.implements(IJavaScriptBundleViewlet)
    #space delimited string of src paths
    paths = ''

    def render(self):
        vals = []
        if self.paths:
            for path in self.paths.split():
                vals.append(STYLE_TAG_SRC_TEMPLATE % getVersionedPath(path))
        css = ''
        if vals:
            css = "".join(vals)
        return css
