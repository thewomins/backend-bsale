from sqlalchemy import and_, text
from sqlalchemy.orm import Session
from typing import List
from typing import Union

from sql.models import Product


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def get_products(db: Session, product_id: List[int]):
    return db.query(Product).filter(Product.id == product_id).all()


def search_product(db: Session, product_name: List[str]):
    likeQuery = []
    for key in product_name:
        likeQuery.append(text("product.name like('%{}%')".format(key.capitalize())))
    return db.query(Product).filter(and_(*likeQuery)).limit(13).all()


def get_all_products(
    db: Session, product_id: Union[List[int], None], skip: int = 0, limit: int = 20
):
    if product_id != None:
        return db.query(Product).filter(Product.id.in_(product_id)).all()
    return db.query(Product).offset(skip).limit(limit).all()
