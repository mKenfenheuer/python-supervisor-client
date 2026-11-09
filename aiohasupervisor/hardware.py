"""Hardware client for supervisor."""

from .client import _SupervisorComponentClient
from .models.hardware import HardwareGPU


class HardwareClient(_SupervisorComponentClient):
    """Handles hardware access in supervisor."""

    async def gpu(self) -> HardwareGPU:
        """Get GPUs of the host with current statistics."""
        result = await self._client.get("hardware/gpu")
        return HardwareGPU.from_dict(result.data)
