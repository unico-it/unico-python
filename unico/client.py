from .modules.completions import Completions
from .modules.agents import Agents
from .modules.contexts import Contexts


class UnicoApiClient:
    def __init__(self, api_key: str, base_url: str = "https://theunico.it/api"):
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')

        self.completions = Completions(self)
        self.agents = Agents(self)
        self.contexts = Contexts(self)

    def headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
