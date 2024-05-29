from amis.event import (
    AjaxAction,
    CopyAction,
    DialogAction,
    DrawerAction,
    EventAction as EventAction,
)

from .data_input import *
from .data_presentation import *
from .feature import *
from .feedback import *
from .layout import *
from .other import *
from .types import *

# update forward refs
# CRUD.update_forward_refs(Form=Form, Action=Action, AmisAPI=AmisAPI, Tpl=Tpl)
CRUD.model_rebuild()
# Table.update_forward_refs(Action=Action, PopOver=PopOver, Badge=Badge)
Table.model_rebuild()
# Calendar.update_forward_refs(Action=Action)
Calendar.model_rebuild()
# Card.update_forward_refs(Action=Action)
Card.model_rebuild()
# GridNav.update_forward_refs(Action=Action, Badge=Badge)
GridNav.model_rebuild()
# AmisList.update_forward_refs(Action=Action, AmisAPI=AmisAPI)
AmisList.model_rebuild()
# Panel.update_forward_refs(Action=Action, Tpl=Tpl)
Panel.model_rebuild()

# PageSchema.update_forward_refs(Iframe=Iframe, Page=Page, AmisAPI=AmisAPI, Tpl=Tpl)
PageSchema.model_rebuild()
# Action.update_forward_refs(Badge=Badge, Tpl=Tpl)
Action.model_rebuild()
# Nav.update_forward_refs(Badge=Badge, AmisAPI=AmisAPI, Tpl=Tpl)
Nav.model_rebuild()
# Icon.update_forward_refs(Badge=Badge)
Icon.model_rebuild()

# Tabs.update_forward_refs(Icon=Icon, Tpl=Tpl)
Tabs.model_rebuild()
# Portlet.update_forward_refs(Icon=Icon, Tpl=Tpl)
Portlet.model_rebuild()

# Page.update_forward_refs(Remark=Remark, AmisAPI=AmisAPI, Tpl=Tpl)
Page.model_rebuild()

# AjaxAction.update_forward_refs(API=API, AmisAPI=AmisAPI)
AjaxAction.model_rebuild()
# DialogAction.update_forward_refs(Dialog=Dialog)
DialogAction.model_rebuild()
# DrawerAction.update_forward_refs(Drawer=Drawer)
DrawerAction.model_rebuild()
# CopyAction.update_forward_refs(Tpl=Tpl)
CopyAction.model_rebuild()
