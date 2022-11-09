from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from sql.database import SessionLocal
from controllers import categoryController
from schemas.category import Category

category = APIRouter()  # se define la ruta


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@category.get("/category/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = categoryController.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="category not found")
    return db_category


@category.get("/categories", response_model=list[Category])
def read_all_categories(db: Session = Depends(get_db)):
    db_categories = categoryController.get_all_categories(db)
    if db_categories is None:
        raise HTTPException(status_code=404, detail="category not found")
    return db_categories


@category.get("/categories-only", response_model=list[Category])
def read_categories(db: Session = Depends(get_db)):
    db_categories = categoryController.get_categories(db)
    if db_categories is None:
        raise HTTPException(status_code=404, detail="category not found")
    return db_categories
