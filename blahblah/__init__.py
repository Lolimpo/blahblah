from typing import Any

from district42 import GenericSchema

from ._generator import Generator
from ._random import Random
from ._version import version

__version__ = version
__all__ = ("fake", "Generator", "Random",)

_generator = Generator(Random())


def fake(schema: GenericSchema, **kwargs: Any) -> Any:
    return schema.__accept__(_generator, **kwargs)
