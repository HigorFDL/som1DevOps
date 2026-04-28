
import pytest
from src.main import *

def test_soma():
    assert soma(2, 3) == 5


@pytest.mark.asyncio
async def test_funcionamento_soma():
    resultado = await funcionamento_soma(2, 3)
    assert resultado["resultados"] == 5