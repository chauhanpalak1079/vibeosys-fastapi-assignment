from pydantic import BaseModel
from typing import Optional
import enum

class CategoryEnum(str, enum.Enum):
    finished = "finished"
    semi_finished = "semi-finished"
    raw = "raw"

class UnitEnum(str, enum.Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    ml = "ml"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    pack = "pack"

class ProductBase(BaseModel):
    name: str
    category: CategoryEnum
    description: Optional[str]
    product_image: Optional[str]
    sku: Optional[str]
    unit: UnitEnum
    lead_time: Optional[int]

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    created_date: Optional[str]
    updated_date: Optional[str]

    class Config:
        orm_mode = True
