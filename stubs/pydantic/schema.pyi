# TODO: Add stubs here
from decimal import Decimal
from typing import Sequence, Type, Optional, Dict, Any, Tuple, Set

default_prefix: str
numeric_types: Tuple[int, float, Decimal]
json_scheme: Dict[str, str]


def schema(
        models: Sequence[Type['BaseModel']],
        *,
        by_alias: bool = True,
        title: Optional[str] = None,
        description: Optional[str] = None,
        ref_prefix: Optional[str] = None,
) -> Dict[str, Any]:
    ...


def model_schema(model: Type['BaseModel'], by_alias: bool = True,
                 ref_prefix: Optional[str] = None) -> Dict[str, Any]:
    ...


def field_schema(
        field: 'ModelField',
        *,
        by_alias: bool = True,
        model_name_map: Dict[Type['BaseModel'], str],
        ref_prefix: Optional[str] = None,
        known_models: Set[Type['BaseModel']] = None,
) -> Tuple[Dict[str, Any], Dict[str, Any], Set[str]]:
    ...


def get_annotation_from_field_info(annotation: Any, field_info: 'FieldInfo',
                                   field_name: str) -> Type[Any]:
    ...


class SkipField(Exception):
    def __init__(self, message: str) -> None:
        ...
