import os
import json

from Products.ZenUtils.Utils import monkeypatch
from Products.Zuul.utils import ZuulMessageFactory as _t
from Products.ZenModel.UserInterfaceSettings import UserInterfaceSettings
from Products.Zuul.routers.device import DeviceRouter

try:
    from local_settings import *
except:
    DEBUG_MOBILE = False


MOBILE_USER_AGENTS = [
    'android',
    'mobile',
    'sony',
    'samsung',
    'nokia',
    'opera mini',
    'iphone',
    'ipad',
    'ipod'
]

UserInterfaceSettings.header_bg = ""

UserInterfaceSettings._properties = UserInterfaceSettings._properties + (
    {'id':'header_bg', 'type':'string', 'mode':'w'},
    {'id':'header_sub_bg', 'type':'string', 'mode':'w'},
    {'id':'sidebar_bg', 'type':'string', 'mode':'w'},
    {'id':'main_bg', 'type':'string', 'mode':'w'},
    {'id':'main_bg_alt', 'type':'string', 'mode':'w'},
    {'id':'use_mobile_ui', 'type':'boolean', 'mode':'w'},
    {'id':'always_use_mobile_ui', 'type':'boolean', 'mode':'w'},
)

UserInterfaceSettings._propertyMetaData['header_bg'] = {
    'xtype': 'textfield', 'name': _t('Main menu background (Put double quotes around a value)'), 'defaultValue': '""', 'allowBlank': False
}
UserInterfaceSettings._propertyMetaData['header_sub_bg'] = {
    'xtype': 'textfield', 'name': _t('Submenu menu background (Put double quotes around a value)'), 'defaultValue': '""', 'allowBlank': False
}
UserInterfaceSettings._propertyMetaData['sidebar_bg'] = {
    'xtype': 'textfield', 'name': _t('Sidebar background (Put double quotes around a value)'), 'defaultValue': '""', 'allowBlank': False
}
UserInterfaceSettings._propertyMetaData['main_bg'] = {
    'xtype': 'textfield', 'name': _t('Grid rows background (Put double quotes around a value)'), 'defaultValue': '""', 'allowBlank': False
}
UserInterfaceSettings._propertyMetaData['main_bg_alt'] = {
    'xtype': 'textfield', 'name': _t('Grid rows background 2 (Put double quotes around a value)'), 'defaultValue': '""', 'allowBlank': False
}
UserInterfaceSettings._propertyMetaData['use_mobile_ui'] = {
    'xtype': 'checkbox', 'name': _t('Use mobile UI when you access Zenoss from mobile device'), 'defaultValue': 'true'
}
UserInterfaceSettings._propertyMetaData['always_use_mobile_ui'] = {
    'xtype': 'checkbox', 'name': _t('ALWAYS Use mobile UI for Zenoss'), 'defaultValue': ''
}


def here(fn):
    """Shorthand to get current directory"""
    return os.path.join(os.path.dirname(__file__), fn)


def is_mobile(request, context=None):
    """
    Returns True if User Agent seems to be mobile device
    """
    if DEBUG_MOBILE: # defaults to False
        return True

    if context:
        settings = context.dmd.UserInterfaceSettings.getInterfaceSettings()
        if settings.get('always_use_mobile_ui', False):
            return True
        if not settings.get('use_mobile_ui', True):
            return False

    ua = request.environ['HTTP_USER_AGENT'].lower()
    for agent in MOBILE_USER_AGENTS:
        if agent in ua:
            return True
    return False


@monkeypatch('Products.ZenUI3.browser.pages.ITInfrastructure')
def __call__(self):
    """
    Overrides default to determine if mobile browser present
    """

    def getTrees(self):
        "Forces non-async tree load"

        router = DeviceRouter(self.context.dmd, {});
        method = router.getTree
        deviceTree = method('/zport/dmd/Devices')
        # system
        systemTree = method('/zport/dmd/Systems')
        # groups
        groupTree = method('/zport/dmd/Groups')        
        # location
        locTree = method('/zport/dmd/Locations')
        js =  """
             Zenoss.env.device_tree_data = %s;
             Zenoss.env.system_tree_data = %s;
             Zenoss.env.group_tree_data = %s;
             Zenoss.env.location_tree_data = %s;
        """ % (json.dumps(deviceTree),
               json.dumps(systemTree),
               json.dumps(groupTree),
               json.dumps(locTree))
        return js

    # For mobile browser returns lite UI
    if is_mobile(self.request, self.context):
        with open(here('resources/templates/itinfrastructure.html')) as f:
            t = f.read()
        c = dict(
            device_tree_data = getTrees(self)
        )
        return t % c

    # For desktop browser returns default Zenoss UI
    return original(self)


# @monkeypatch('Products.ZenUI3.browser.MainPageRedirect')
# def __call__(self):
#     """
#     Redirects to IT Infrastructure when on mobile
#     """
#     if is_mobile(self.request, self.context):
#         self.request.response.redirect('/zport/dmd/itinfrasructure')
#     else:
#         original(self)


@monkeypatch('Products.ZenUI3.browser.pages.DeviceDetails')
def __call__(self):
    """
    Mobile Device details page
    """
    if is_mobile(self.request, self.context):
        with open(here('resources/templates/devdetail.html')) as f:
            t = f.read()
        return t

    # For desktop browser returns default Zenoss UI
    return original(self)


@monkeypatch('Products.ZenUI3.browser.eventconsole.grid.EventConsole')
def __call__(self):
    """
    Overrides default to determine if mobile browser present
    """
    if is_mobile(self.request, self.context):
        with open(here('resources/templates/eventconsole.html')) as f:
            t = f.read()
        return t

    return original(self)
