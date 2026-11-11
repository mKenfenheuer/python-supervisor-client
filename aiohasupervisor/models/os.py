"""Models for OS APIs."""

from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import PurePath

from .base import DEFAULT, Options, Request, ResponseData

# --- ENUMS ----


class RaucState(StrEnum):
    """RaucState type."""

    GOOD = "good"
    BAD = "bad"
    ACTIVE = "active"


class BootSlotName(StrEnum):
    """BootSlotName type."""

    A = "A"
    B = "B"


# --- OBJECTS ----


@dataclass(frozen=True, slots=True)
class BootSlot(ResponseData):
    """BootSlot model."""

    state: str
    status: RaucState | None
    version: str | None


@dataclass(frozen=True, slots=True)
class OSInfo(ResponseData):
    """OSInfo model."""

    version: str | None
    version_latest: str | None
    version_pending: str | None
    update_available: bool
    board: str | None
    boot: str | None
    data_disk: str | None
    boot_slots: dict[str, BootSlot]
    # OS variant of the running version (e.g. nvidia), None for the plain OS
    variant: str | None = None
    variants: list[str] = field(default_factory=list)


@dataclass(frozen=True, slots=True)
class OSUpdate(Request):
    """OSUpdate model.

    Without variant the update keeps the OS variant, None switches to the
    plain OS.
    """

    version: str | None = None
    variant: str | None = DEFAULT  # type: ignore[assignment]


@dataclass(frozen=True, slots=True)
class MigrateDataOptions(Request):
    """MigrateDataOptions model."""

    device: str


@dataclass(frozen=True, slots=True)
class DataDisk(ResponseData):
    """DataDisk model."""

    name: str
    vendor: str
    model: str
    serial: str
    size: int
    id: str
    dev_path: PurePath


@dataclass(frozen=True, slots=True)
class DataDiskList(ResponseData):
    """DataDiskList model."""

    disks: list[DataDisk]


@dataclass(frozen=True, slots=True)
class SetBootSlotOptions(Request):
    """SetBootSlotOptions model."""

    boot_slot: BootSlotName


@dataclass(frozen=True, slots=True)
class GreenInfo(ResponseData):
    """GreenInfo model."""

    activity_led: bool
    power_led: bool
    system_health_led: bool


@dataclass(frozen=True, slots=True)
class GreenOptions(Options):
    """GreenOptions model."""

    activity_led: bool | None = None
    power_led: bool | None = None
    system_health_led: bool | None = None


@dataclass(frozen=True, slots=True)
class YellowInfo(ResponseData):
    """YellowInfo model."""

    disk_led: bool
    heartbeat_led: bool
    power_led: bool


@dataclass(frozen=True, slots=True)
class YellowOptions(Options):
    """YellowOptions model."""

    disk_led: bool | None = None
    heartbeat_led: bool | None = None
    power_led: bool | None = None


@dataclass(frozen=True, slots=True)
class RaspberryPiFirmwareInfo(ResponseData):
    """RaspberryPiFirmwareInfo model — Raspberry Pi firmware state."""

    current_version: str | None
    latest_version: str | None
    update_available: bool
    update_blocked: bool
    update_pending: bool
    blocked_reason: str | None


@dataclass(frozen=True, slots=True)
class SwapInfo(ResponseData):
    """SwapInfo model."""

    swap_size: str | None
    swappiness: int | None


@dataclass(frozen=True, slots=True)
class SwapOptions(Options):
    """SwapOptions model."""

    swap_size: str | None = None
    swappiness: int | None = None
