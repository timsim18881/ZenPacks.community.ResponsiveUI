"""
Responsive UI zenpack
"""

import logging
log = logging.getLogger('zen.ResponsiveUI')

import Globals
import os
import re
from Products.ZenUtils.Utils import unused
from Products.ZenModel.ZenPack import ZenPackBase

import ZenPacks.community.ResponsiveUI.patches

unused(Globals)

META_RESPONSIVE = '<meta name="viewport" content="width=device-width, user-scalable=yes"> <meta responsiveuimarker="true">'


# Patches login form by adding responsive CSS into it
login_form = os.path.join(
    os.environ.get('ZENHOME'), "Products/ZenModel/skins/zenmodel/login_form.pt"
)
if os.path.exists(login_form):
    with open(login_form, "r") as f:
        filedata = f.read()

        if not META_RESPONSIVE in filedata:
            filedata = filedata.replace(
                '<head>',
                '<head> ' + META_RESPONSIVE)
            filedata = filedata.replace(
                '</style>',
                '    @media all and (max-width: 640px) {'
                '        body, #middlebar {background-color: #f4f4f4; border: 0px none}'
                '        #topbar {height: 0%}'
                '    }'
                '</style>'
            )
            with open(login_form, "w") as f2:
                f2.write(filedata)
