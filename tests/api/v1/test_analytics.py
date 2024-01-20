import pytest

from tests.conftest import client


class TestAnalytics:
    url = "/v1/analytics"
    history_url = f"{url}/history"

    @pytest.mark.asyncio
    async def test_analytics_list_ok(self, fill_assets_collection):
        response = client.get(self.url)

        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert isinstance(response.json()[0], dict)

    @pytest.mark.asyncio
    async def test_analytics_retrieve_ok(self, fill_assets_collection):
        list_response = client.get(self.url)
        document_id = list_response.json()[0]["_id"]

        response = client.get(f"{self.url}/{document_id}")

        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    @pytest.mark.asyncio
    async def test_analytics_history_ok(self, fill_assets_collection):
        response = client.get(self.history_url)

        data = response.json()

        assert response.status_code == 200
        assert isinstance(data, list)
        assert isinstance(data[0], dict)
        assert isinstance(data[0]["best_bid_price"], list)
