"""Test hardware supervisor client."""

from aiointercept import aiointercept

from aiohasupervisor import SupervisorClient

from . import load_fixture
from .const import SUPERVISOR_URL


async def test_hardware_gpu(
    responses: aiointercept, supervisor_client: SupervisorClient
) -> None:
    """Test hardware GPU API."""
    responses.get(
        f"{SUPERVISOR_URL}/hardware/gpu",
        status=200,
        body=load_fixture("hardware_gpu.json"),
    )
    result = await supervisor_client.hardware.gpu()

    assert len(result.gpus) == 2
    nvidia = result.gpus[0]
    assert nvidia.name == "NVIDIA GeForce RTX 3090"
    assert nvidia.vendor == "nvidia"
    assert nvidia.driver_version == "615.78.08"
    assert nvidia.utilization == 7.0
    assert nvidia.memory_used == 2982150144
    assert nvidia.memory_total == 25769803776
    assert nvidia.temperature == 34.0
    assert nvidia.power == 16.37

    intel = result.gpus[1]
    assert intel.driver == "i915"
    assert intel.utilization is None
    assert intel.memory_total is None
    assert intel.temperature is None
