from __future__ import annotations

from typing import Any, Dict, Optional, Tuple, Type

from pydantic import BaseModel, ConfigDict, create_model
from sqlalchemy.orm import DeclarativeMeta


def create_schemas(
    model: Type[DeclarativeMeta],
) -> Tuple[Type[BaseModel], Type[BaseModel], Type[BaseModel]]:
    """Generate Pydantic schemas for the given SQLAlchemy model.

    Returns a tuple of (CreateSchema, ReadSchema, UpdateSchema).
    """

    def _schema(exclude_pk: bool, partial: bool) -> Type[BaseModel]:
        fields: Dict[str, tuple[type[Any], Any]] = {}
        for column in model.__table__.columns:
            if exclude_pk and column.primary_key:
                continue
            python_type = getattr(column.type, "python_type", Any)
            default = None
            if column.default is not None and column.default.is_scalar:
                default = column.default.arg
            if not partial and not column.nullable and default is None and not column.primary_key:
                fields[column.name] = (python_type, ...)
            else:
                fields[column.name] = (Optional[python_type], default)
        schema = create_model(
            f"{model.__name__}{'Update' if partial else ('Create' if exclude_pk else 'Read')}",
            **fields,  # type: ignore[arg-type]
        )
        schema.model_config = ConfigDict(from_attributes=True)
        return schema

    return _schema(True, False), _schema(False, False), _schema(True, True)
