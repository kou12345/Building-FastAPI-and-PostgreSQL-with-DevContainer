from enum import Enum
from typing import Optional

from app.models.core import CoreModel, IDModelMixin


class ColorType(str, Enum):
    solt_and_pepper = "SOLT & PEPPER"
    dark_grey = "DARK GREY"
    chocolate = "CHOCOLATE"


# 全リソースで共有する属性
class HedgehogBase(CoreModel):
    name: Optional[str]
    description: Optional[str]
    age: Optional[float]
    color_type: Optional[ColorType]


# 新しいリソースを作成する際に必須の属性
class HedgehogCreate(HedgehogBase):
    name: str
    color_type: ColorType


# 更新することが可能な属性
class HedgehogUpdate(HedgehogBase):
    description: str
    age: float


# データベースから取得するリソースに存在する属性
class HedgehogInDB(IDModelMixin, HedgehogBase):
    name: str
    age: float
    color_type: ColorType


# GET, POST, PUTリクエストで返されるデータに存在する属性
class HedgehogPublic(IDModelMixin, HedgehogBase):
    pass
