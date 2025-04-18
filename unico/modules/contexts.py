import requests
from ..exceptions import UnicoAPIClientError


def _handle_response(response):
    if response.status_code >= 400:
        raise UnicoAPIClientError(
            f"Error {response.status_code}: {response.text}",
            status_code=response.status_code
        )
    return response.json()


class Contexts:
    def __init__(self, client):
        self.client = client

    def create(self, agent: str, contexts: []):
        url = f"{self.client.base_url}/contexts/create"
        payload = {
            "agent": agent,
            "contexts": contexts
        }
        response = requests.post(url, headers=self.client.headers(), json=payload)
        return _handle_response(response)
