# UNICO Python package

A Python package to interact with the UNICO API. This package allows developers to easily integrate their applications
with the UNICO platform by providing a simple and
Pythonic interface to the available API endpoints. With just an API key, users can authenticate and start interacting
with UNICO services, including retrieving available agents, add contexts and generating completions via intelligent
agents.

## Getting Started

```
pip install unico-python
```

## Usage

```python
from unico import Client

client = Client(api_key="YOUR_API_KEY", base_url="OPTIONAL_UNICO_API_BASE_URL")

# Retrieve agents
agents = client.agents.retrieve()
print(agents)

# Add some contexts
result = client.agents.contexts.create(id, ["New fantastic context"])
print(result)

# Create completions
result = client.agents.completions.create(id, "Hello World!")
print(result)
```

## Development

1. **Install [uv](https://docs.astral.sh/uv/getting-started/installation/#pypi)**:
   uv is used to manage the virtual environment and necessary packages.

2. **Create virtual environment**:
   uv will automatically read the `.python-version` file and install the correct Python version:

   ```bash
   uv venv
   ```

3. **Install necessary packages**

   ```bash
   uv sync
   ```

## Before pushing

**See if you have any rebase to do** (you must have the updated commits history before pushing to avoid conflicts
between main and your branch):

```sh
git fetch
git pull origin main --rebase
```

## Contributing

If you want to contribute to **UNICO Python package**, follow these steps:

1. Create a new branch for your changes (`git checkout -b your-branch-name`).
2. Make your changes and commit them (`git commit -m 'Changed something'`).
3. Push your branch (`git push origin your-branch-name`).
4. Open a pull request.

## Contact

For more information, contact the **UNICO** support team at: info@theunico.it
