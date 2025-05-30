from .modules.agents import Agents


class Client:
    def __init__(self, api_key: str, base_url: str = "https://theunico.it/api"):
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')

        self.agents = Agents(self)

    def headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
