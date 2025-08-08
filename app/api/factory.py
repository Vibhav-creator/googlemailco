from __future__ import annotations

from typing import Type

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.database import get_db
from .auth import get_current_user


def generate_router(
    model_name: str,
    crud: CRUDBase,
    schema_read: Type,
    schema_create: Type,
    schema_update: Type,
) -> APIRouter:
    """Create an APIRouter with standard CRUD endpoints for a model."""

    router = APIRouter(
        prefix=f"/{model_name.lower()}",
        tags=[model_name],
        dependencies=[Depends(get_current_user)],
    )

    @router.get("/", response_model=list[schema_read])
    def read_items(db: Session = Depends(get_db)):
        return crud.get_multi(db)

    @router.post("/", response_model=schema_read)
    def create_item(item: schema_create, db: Session = Depends(get_db)):
        return crud.create(db, item)

    @router.get("/{item_id}", response_model=schema_read)
    def read_item(item_id: int, db: Session = Depends(get_db)):
        obj = crud.get(db, item_id)
        if obj is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return obj

    @router.put("/{item_id}", response_model=schema_read)
    def update_item(
        item_id: int, item: schema_update, db: Session = Depends(get_db)
    ):
        db_obj = crud.get(db, item_id)
        if db_obj is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return crud.update(db, db_obj, item)

    @router.delete("/{item_id}", response_model=schema_read)
    def delete_item(item_id: int, db: Session = Depends(get_db)):
        obj = crud.remove(db, item_id)
        if obj is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return obj

    return router
