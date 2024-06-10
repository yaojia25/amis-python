from typing import Optional

from amis.typing import DictStrAny, Expression

from pydantic import BaseModel, ConfigDict


class BaseAmisModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        extra="allow",
    )

    def to_json(self):
        return self.model_dump_json(exclude_none=True, by_alias=True)

    def to_dict(self):
        return self.model_dump(exclude_none=True, by_alias=True)

    def update_from_dict(self, kwargs: DictStrAny):
        for k, v in kwargs.items():
            setattr(self, k, v)
        return self

    def update_from_kwargs(self, **kwargs):
        return self.update_from_dict(kwargs)


class AmisNode(BaseAmisModel):
    """组件配置"""

    type: Optional[str] = None
    """组件类型"""
    visible: Optional[bool] = None
    """是否显示，True为显示,False为隐藏，默认为True"""
    hidden: Optional[bool] = None
    """是否隐藏，True为隐藏,false为显示，默认为False"""
    visibleOn: Optional[Expression] = None
    """显示表达式"""
    hiddenOn: Optional[Expression] = None
    """隐藏表达式"""
    id: Optional[str] = None
    """组件ID"""
    name: Optional[str] = None
    """组件字段名"""
    value: Optional[str] = None
    """组件字段值"""
    mobile: Optional[DictStrAny] = None
    """移动端定制配置"""


class APIResponse(BaseModel):
    status: int
    msg: str = ""
    data: DictStrAny
