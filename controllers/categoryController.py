from sqlalchemy.orm import Session, noload

from sql.models import Category, Product


def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


def get_all_categories(db: Session, skip: int = 0, limit: int = 20):
    return db.query(Category).offset(skip).limit(limit).all()


def get_categories(db: Session):
    return db.query(Category).options(noload(Category.products)).all()
