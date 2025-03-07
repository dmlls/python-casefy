__version__ = "1.1.0"

from .casefy import (
    alphanumcase,
    camelcase,
    capitalcase,
    constcase,
    kebabcase,
    lowercase,
    pascalcase,
    sentencecase,
    separatorcase,
    snakecase,
    titlecase,
    uppercase,
    upperkebabcase,
)

# Don't expose the submodule itself
del globals()["casefy"]

__all__ = [
    "camelcase",
    "pascalcase",
    "snakecase",
    "constcase",
    "kebabcase",
    "upperkebabcase",
    "separatorcase",
    "sentencecase",
    "titlecase",
    "alphanumcase",
    "lowercase",
    "uppercase",
    "capitalcase",
]
