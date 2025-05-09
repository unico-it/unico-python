# UNICO Python package

A Python package to interact with the UNICO API. This package allows developers to easily integrate their applications
with the UNICO platform by providing a simple and
Pythonic interface to the available API endpoints. With just an API key, users can authenticate and start interacting
with UNICO services, including retrieving available agents, add contexts and generating completions via intelligent
agents.

## Get Started (Development)

1. **Install [pipenv](https://pipenv.pypa.io/en/latest/installation.html)**:
   Pipenv is used to handle the virtual environment and the necessary packages.

2. **Install necessary packages from `Pipfile`**

   ```bash
   pipenv install
   ```

## Installation from GitHub

In your `Pipfile`:

```toml
[packages]
unico = { git = "https://github.com/unico-it/unico-python.git", ref = "main" }
```

Then run:

```bash
pipenv install
```

## Example

```python
from unico import Client

client = Client(api_key="YOUR_API_KEY", base_url="OPTIONAL_UNICO_API_BASE_URL")

# Retrieve agents
agents = client.agents.retrieve()
print(agents)

# Add some contexts
result = client.agent(id).contexts.create(["New fantastic context"])
print(result)

# Create completions
result = client.agent(id).completions.create("Hello World!")
print(result)
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
