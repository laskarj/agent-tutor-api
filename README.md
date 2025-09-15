# Agent Tutor API

## Installation

1.  Make sure you have Python 3.13 or higher installed.
2.  Install [`uv`](https://docs.astral.sh/uv):

### Quickstart:
```
uv sync
```

## Configuration

1.  Create a `config.toml` file in the `config` directory by copying the `config.template.toml` file.
2.  Fill in the required secrets in `config.toml`.

## Usage


### Running the agent in development mode

To run the agent in development mode with hot-reloading, use the `dev-mode` script:

```bash
uv run agent-dev 
```

This will start the agent and automatically reload it when you make changes to the code.

### Using the development console

The `dev-console` script provides a development console:

```bash
uv run agent-console
```

### Linting

To format and lint the code, run:

```bash
uv run lint
```