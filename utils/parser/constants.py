from typing import Literal

TYPES: dict[
    str,
    Literal["string"]
    | Literal["integer"]
    | Literal["float"]
    | Literal["chr"]
    | Literal["none"],
] = {
    "STR": "string",
    "INT": "integer",
    "FLT": "float",
    "CHR": "chr",
}

TYPES_EXPECTED_FROM_LEXER = ("STR", "INT", "FLT", "CHR")
