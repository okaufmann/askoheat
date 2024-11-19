"""Api descriptor classes."""

from __future__ import annotations

import typing
from abc import ABC
from dataclasses import dataclass, field
from enum import IntEnum, StrEnum
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from collections.abc import Callable

    import numpy as np

    from custom_components.askoheat.model import (
        AskoheatBinarySensorEntityDescription,
        AskoheatNumberEntityDescription,
        AskoheatSelectEntityDescription,
        AskoheatSensorEntityDescription,
        AskoheatSwitchEntityDescription,
        AskoheatTextEntityDescription,
        AskoheatTimeEntityDescription,
    )


class SwitchAttrKey(StrEnum):
    """Askoheat binary switch attribute keys."""


@dataclass(frozen=True)
class RegisterInputDescriptor(ABC):  # noqa: B024
    """Description of a register based input."""

    starting_register: typing.Final[int] = field()


@dataclass(frozen=True)
class FlagRegisterInputDescriptor(RegisterInputDescriptor):
    """Input register representing a a flag as a bit mask of an int value."""

    bit: int


@dataclass(frozen=True)
class ByteRegisterInputDescriptor(RegisterInputDescriptor):
    """Input register representing a byte."""


@dataclass(frozen=True)
class Float32RegisterInputDescriptor(RegisterInputDescriptor):
    """Input register representing a float32."""


@dataclass(frozen=True)
class SignedIntRegisterInputDescriptor(RegisterInputDescriptor):
    """Input register representing a signed int."""


@dataclass(frozen=True)
class UnsignedIntRegisterInputDescriptor(RegisterInputDescriptor):
    """Input register representing an unsigned int."""


@dataclass(frozen=True)
class StringRegisterInputDescriptor(RegisterInputDescriptor):
    """Input register representing a string."""

    number_of_words: int


@dataclass(frozen=True)
class TimeRegisterInputDescriptor(RegisterInputDescriptor):
    """Input register representing a time string combined of two following registers."""


E = TypeVar("E", bound=StrEnum)


@dataclass(frozen=True)
class StrEnumInputDescriptor[E](StringRegisterInputDescriptor):
    """Input register representing a string based enum value."""

    factory: Callable[[str], E]
    values: list[E]


E2 = TypeVar("E2", bound=IntEnum)


@dataclass(frozen=True)
class IntEnumInputDescriptor[E2](ByteRegisterInputDescriptor):
    """Input register representing a int based enum value."""

    factory: Callable[[np.byte], E2]
    values: list[E2]


@dataclass(frozen=True)
class RegisterBlockDescriptor:
    """Based askoheat modbus block (range of registers) descriptor."""

    starting_register: int
    number_of_registers: int

    binary_sensors: list[AskoheatBinarySensorEntityDescription] = field(
        default_factory=list
    )
    sensors: list[AskoheatSensorEntityDescription] = field(default_factory=list)
    switches: list[AskoheatSwitchEntityDescription] = field(default_factory=list)
    number_inputs: list[AskoheatNumberEntityDescription] = field(default_factory=list)
    time_inputs: list[AskoheatTimeEntityDescription] = field(default_factory=list)
    text_inputs: list[AskoheatTextEntityDescription] = field(default_factory=list)
    select_inputs: list[AskoheatSelectEntityDescription] = field(default_factory=list)

    def absolute_register_index(self, desc: RegisterInputDescriptor) -> int:
        """Return absolute index of register."""
        return self.starting_register + desc.starting_register
