# pangu-precommit

Pre-commit hooks for [pangu.py](https://github.com/vinta/pangu.py) - automatically insert whitespace between CJK (Chinese, Japanese, Korean) and half-width characters (alphabetical letters, numerical digits, and symbols) for better readability.

## Features

pangu-precommit is a pre-commit hook that automatically processes the following file types:
- Markdown files (`.md`)
- reStructuredText files (`.rst`)
- Plain text files (`.txt`)

It automatically adds appropriate spacing between CJK characters and half-width characters, making text more readable.

**中文文档 | [Chinese Documentation](README.zh-CN.md)**

## Installation

### Using uv (recommended)

```bash
uv install
```

### Using pip

```bash
pip install -e .
```

## Configuration

### 1. Install pre-commit

If you haven't installed pre-commit yet, install it first:

```bash
pip install pre-commit
```

### 2. Add the hook

Create a `.pre-commit-config.yaml` file in your project root and add the following configuration:

```yaml
repos:
  - repo: https://github.com/yourusername/pangu-precommit
    rev: v0.1.0  # Use the latest version
    hooks:
      - id: pangu
```

Or, for local development:

```yaml
repos:
  - repo: local
    hooks:
      - id: pangu
        name: pangu
        entry: pangup
        language: python
        types: [text]
        files: \.(md|rst|txt)$
```

### 3. Install the hooks

```bash
pre-commit install
```

## Usage

### Manual run

```bash
pre-commit run pangu --all-files
```

### Automatic run

When you commit your code, pre-commit will automatically run the pangu hook to format your files.

## Example

**Input:**
```
这是一个测试test，包含中文和English。
```

**Output:**
```
这是一个测试 test，包含中文和 English。
```

## Dependencies

- Python >= 3.13
- pangu >= 4.0.6.1

## Project Structure

```
pangu-precommit/
├── .pre-commit-hooks.yaml  # pre-commit hook configuration
├── pangup.py               # CLI entry point
├── pyproject.toml          # Project configuration and dependencies
└── README.md               # Project documentation
```

## Development

### Run CLI

```bash
python pangup.py filename.md
```

### Testing

```bash
pangup README.md
```

## License

This project follows the license of pangu.py.

## Related Links

- [pangu.py](https://github.com/vinta/pangu.py) - Original project
- [pre-commit](https://pre-commit.com/) - pre-commit framework