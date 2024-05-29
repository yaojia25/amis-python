"""基于百度amis框架的python pydantic模型封装，
详细文档请看https://aisuda.bce.baidu.com/amis/zh-CN/docs/index
"""
from importlib.metadata import version

from .base import (
    AmisNode as AmisNode,
    APIResponse as APIResponse,
    BaseAmisModel as BaseAmisModel,
)
from .render import render_as_html as render_as_html

__version__ = version("amis-python")
