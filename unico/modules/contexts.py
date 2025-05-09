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
    def __init__(self, client, agent_id: int = None):
        self.client = client
        self.agent_id = agent_id

    def create(self, contexts: []):
        if not self.agent_id:
            raise UnicoAPIClientError("agent_id is required. Be sure to use agent(id) for this method")

        url = f"{self.client.base_url}/agents/{self.agent_id}/contexts/create"
        payload = {
            "contexts": contexts
        }
        response = requests.post(url, headers=self.client.headers(), json=payload)
        return _handle_response(response)
