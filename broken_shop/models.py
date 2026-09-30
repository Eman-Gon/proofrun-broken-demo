from typing import Optional
from pydantic import BaseModel


class Customer(BaseModel):
    name: str
    nickname: Optional[str]
    phone: Optional[str]


class Address(BaseModel):
    street: str
    apartment: Optional[str]
    instructions: Optional[str]


class Product(BaseModel):
    sku: str
    description: Optional[str]
    category: Optional[str]


class Order(BaseModel):
    order_id: str
    coupon: Optional[str]
    notes: Optional[str]
