import requests
from ..exceptions import UnicoAPIClientError


def _handle_response(response):
    if response.status_code >= 400:
        raise UnicoAPIClientError(
            f"Error {response.status_code}: {response.text}",
            status_code=response.status_code
        )
    return response.json()


class Agents:
    def __init__(self, client):
        self.client = client

    def retrieve(self):
        url = f"{self.client.base_url}/agents"
        response = requests.get(url, headers=self.client.headers())
        return _handle_response(response)
