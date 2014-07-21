from Products.Zuul.utils import ZuulMessageFactory as _t
from Products.ZenModel.UserInterfaceSettings import UserInterfaceSettings


UserInterfaceSettings.header_bg = ""

UserInterfaceSettings._properties = UserInterfaceSettings._properties + (
    {'id':'header_bg', 'type':'string', 'mode':'w'},
    {'id':'header_sub_bg', 'type':'string', 'mode':'w'},
    {'id':'sidebar_bg', 'type':'string', 'mode':'w'},
    {'id':'main_bg', 'type':'string', 'mode':'w'},
    {'id':'main_bg_alt', 'type':'string', 'mode':'w'},
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
