"""Models for hardware APIs."""

from dataclasses import dataclass

from .base import ResponseData

# --- OBJECTS ----


@dataclass(frozen=True, slots=True)
class GPU(ResponseData):
    """GPU model.

    Statistics are None if the driver doesn't provide them.
    """

    address: str
    vendor: str
    name: str
    driver: str
    driver_version: str
    utilization: float | None
    memory_used: int | None
    memory_total: int | None
    temperature: float | None
    power: float | None


@dataclass(frozen=True, slots=True)
class HardwareGPU(ResponseData):
    """HardwareGPU model."""

    gpus: list[GPU]
