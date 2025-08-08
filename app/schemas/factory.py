import enum
from pathlib import Path
from typing import Optional, Set

from sqlalchemy import inspect

from app.models import Base

EXCLUDE_COLUMNS = {"id", "created_at", "updated_at", "is_deleted"}


def _python_type(column):
    try:
        return column.type.python_type
    except NotImplementedError:  # fallback when type doesn't expose python_type
        return str


def _imports_and_field(column, optional: bool) -> tuple[Set[str], str]:
    col_type = _python_type(column)
    imports: Set[str] = set()
    type_name = col_type.__name__
    if isinstance(col_type, type) and issubclass(col_type, enum.Enum):
        imports.add(f"from app.models.base import {type_name}")
    elif col_type.__module__ == "datetime":
        imports.add(f"from datetime import {type_name}")
    if optional:
        imports.add("from typing import Optional")
        annotation = f"Optional[{type_name}]"
        default = "None"
    else:
        annotation = type_name
        default = "..."
    field_line = f"    {column.key}: {annotation} = {default}"
    return imports, field_line


def generate_schema(model):
    mapper = inspect(model)
    create_fields = []
    update_fields = []
    imports: Set[str] = {"from pydantic import BaseModel"}
    for column in mapper.columns:
        if column.key in EXCLUDE_COLUMNS:
            continue
        required = (
            not column.nullable
            and column.default is None
            and column.server_default is None
            and not column.autoincrement
            and not column.primary_key
        )
        imp, line = _imports_and_field(column, optional=not required)
        imports.update(imp)
        create_fields.append(line)
        # Update models always optional
        imp_u, line_u = _imports_and_field(column, optional=True)
        imports.update(imp_u)
        update_fields.append(line_u)
    imports_block = "\n".join(sorted(imports)) + "\n\n"
    create_block = [f"class {model.__name__}Create(BaseModel):"]
    create_block.extend(create_fields or ["    pass"])
    create_block.append("")
    update_block = [f"class {model.__name__}Update(BaseModel):"]
    update_block.extend(update_fields or ["    pass"])
    update_block.append("")
    return imports_block + "\n".join(create_block + update_block)


def main():
    base_path = Path(__file__).parent
    for model in Base.__subclasses__():
        code = generate_schema(model)
        file_path = base_path / f"{model.__name__.lower()}.py"
        file_path.write_text(
            "# This file is auto-generated. Do not edit manually.\n" + code
        )
    # regenerate __init__.py
    init_lines = []
    names = []
    for model in Base.__subclasses__():
        name = model.__name__.lower()
        init_lines.append(
            f"from .{name} import {model.__name__}Create, {model.__name__}Update"
        )
        names.extend([f"{model.__name__}Create", f"{model.__name__}Update"])
    init_lines.append("\n__all__ = [" + ", ".join(f'\"{n}\"' for n in names) + "]\n")
    (base_path / "__init__.py").write_text("\n".join(init_lines))


if __name__ == "__main__":
    main()
