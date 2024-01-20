import asyncio
from unittest.mock import Mock

import pytest

from application.use_case.coins import CoinUseCase
from tests.conftest import client


class TestCoinsUpdate:
    url = "/v1/coins/update"

    @pytest.mark.asyncio
    async def test_coins_update_with_exception(self):
        response = client.get(self.url)

        assert response.status_code == 400
        assert isinstance(response.json(), dict)

    @pytest.mark.asyncio
    async def test_coins_update_ok(self):
        future = asyncio.Future()
        future.set_result(True)

        mock_object = CoinUseCase
        mock_object.get_data_and_send = Mock(return_value=future)

        response = client.get(self.url)

        assert response.status_code == 200
        assert response.content == b"successfully"
