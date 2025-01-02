from typing import (
    TypedDict,
    List,
    get_type_hints,
    Optional,
    Union,
    get_origin,
    get_args,
    Type,
    Any,
)
from pydantic import BaseModel, Field
from enum import Enum

def typed_dict_to_basemodel(
        name: str, typed_dict: Type[TypedDict], created_models: dict = None
) -> Type[BaseModel]:
    if created_models is None:
        created_models = {}

    # Check if this TypedDict has already been converted to avoid circular references
    if name in created_models:
        return created_models[name]

    # Retrieve type hints (field types) from the TypedDict
    hints = get_type_hints(typed_dict)
    attributes = {}

    # Determine required and optional fields
    required_keys = getattr(typed_dict, '__required_keys__', set())
    optional_keys = getattr(typed_dict, '__optional_keys__', set())

    for field, hint in hints.items():
        origin = get_origin(hint)
        args = get_args(hint)

        # Function to process each type hint recursively
        def process_hint(hint_type):
            origin_inner = get_origin(hint_type)
            args_inner = get_args(hint_type)

            if isinstance(hint_type, type) and issubclass(hint_type, TypedDict):
                nested_model_name = f"{hint_type.__name__}Model"
                return typed_dict_to_basemodel(nested_model_name, hint_type, created_models)
            elif origin_inner in {List, list} and len(args_inner) == 1:
                elem_type = args_inner[0]
                if isinstance(elem_type, type) and issubclass(elem_type, TypedDict):
                    nested_model = typed_dict_to_basemodel(
                        f"{elem_type.__name__}Model", elem_type, created_models
                    )
                    return List[nested_model]
                else:
                    return List[elem_type]
            elif origin_inner is Union:
                # Handle Optional (Union[..., NoneType])
                non_none_args = [arg for arg in args_inner if arg is not type(None)]
                if len(non_none_args) == 1:
                    return Optional[process_hint(non_none_args[0])]
                else:
                    return hint_type
            else:
                return hint_type

        # Process the current hint
        processed_hint = process_hint(hint)

        # Determine if the field is required
        if field in required_keys:
            attributes[field] = (processed_hint, ...)
        else:
            # If the field is optional, set default to None
            if get_origin(processed_hint) is Optional:
                attributes[field] = (processed_hint, None)
            else:
                attributes[field] = (Optional[processed_hint], None)

    # Dynamically create a Pydantic BaseModel
    model = type(name, (BaseModel,), attributes)
    created_models[name] = model
    return model

