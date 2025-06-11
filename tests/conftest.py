import pytest
from rich.console import Console


@pytest.fixture(scope="module")
def console():
    return Console()
