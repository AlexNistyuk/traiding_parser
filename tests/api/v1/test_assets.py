import json

import pytest

from tests.conftest import AssetFactory, client


class TestAssets:
    url = "/v1/assets"

    @pytest.mark.asyncio
    async def test_assets_list_ok(self, fill_assets_collection):
        response = client.get(self.url)

        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert isinstance(response.json()[0], dict)

    @pytest.mark.asyncio
    async def test_assets_retrieve_ok(self, fill_assets_collection):
        list_response = client.get(self.url)
        document_id = list_response.json()[0]["_id"]

        response = client.get(f"{self.url}/{document_id}")

        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    @pytest.mark.asyncio
    async def test_assets_create_ok(self, fill_assets_collection):
        response = client.post(url=self.url, content=json.dumps(AssetFactory.build()))

        data = response.json()

        assert response.status_code == 201
        assert isinstance(data, dict)
        assert "_id" in data
