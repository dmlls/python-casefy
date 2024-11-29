__version__ = "1.0.0"

from .casefy import (
    camelcase,
    pascalcase,
    snakecase,
    constcase,
    kebabcase,
    upperkebabcase,
    separatorcase,
    sentencecase,
    titlecase,
    alphanumcase,
    lowercase,
    uppercase,
    capitalcase
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
    "capitalcase"
]
