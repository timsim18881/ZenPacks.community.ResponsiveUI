import zope.interface

from Products.Five.viewlet.viewlet import ViewletBase
from Products.ZenUI3.browser.interfaces import IJavaScriptBundleViewlet
from Products.ZenUI3.browser.javascript import getVersionedPath

from .patches import is_mobile


STYLE_TAG_SRC_TEMPLATE = "<link rel='stylesheet' type='text/css' href='%s' />\n"
SCRIPT_TAG_SRC_TEMPLATE = "<script src='%s'></script>\n"


class StyleSrcBundleViewlet(ViewletBase):
    zope.interface.implements(IJavaScriptBundleViewlet)
    #space delimited string of src paths
    paths = ''
    template = STYLE_TAG_SRC_TEMPLATE

    def can_render(self):
        return True

    def render(self):
        if not self.can_render():
            return ""
        vals = []
        if self.paths:
            for path in self.paths.split():
                vals.append(self.template % getVersionedPath(path))
        css = ''
        if vals:
            css = "".join(vals)
        return css


class MobileStyleSrcBundleViewlet(StyleSrcBundleViewlet):
    def can_render(self):
        return is_mobile(self.request)


class MobileJavaScriptSrcBundleViewlet(StyleSrcBundleViewlet):
    template = SCRIPT_TAG_SRC_TEMPLATE

    def can_render(self):
        return is_mobile(self.request)
