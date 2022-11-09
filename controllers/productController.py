from sqlalchemy.orm import Session
from sqlalchemy import or_, text, and_

from sql.models import Product


def get_product(db: Session, product_id: int):
    a = db.query(Product).filter(Product.id == product_id).first()
    return a


def search_product(db: Session, product_name: list[str]):
    likeQuery = []
    for key in product_name:
        likeQuery.append(text("product.name like('%{}%')".format(key.capitalize())))
    return db.query(Product).filter(and_(*likeQuery)).limit(13).all()


def get_all_products(db: Session, skip: int = 0, limit: int = 20):
    return db.query(Product).offset(skip).limit(limit).all()
