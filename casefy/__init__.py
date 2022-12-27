__version__ = "0.1.7"

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
