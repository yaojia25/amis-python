from typing import Any, Dict, List, Union
from typing_extensions import TypeAlias, TypedDict


class OptionDict(TypedDict, total=False):
    label: str
    value: str


DictStrAny: TypeAlias = Dict[str, Any]
DictStr: TypeAlias = Dict[str, str]
Expression: TypeAlias = str
OptionsType: TypeAlias = List[Union[OptionDict, str, DictStr]]
DataMapping: TypeAlias = str
