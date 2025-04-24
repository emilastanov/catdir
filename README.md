# catdir

`catdir` is a simple CLI utility that traverses directories and concatenates the contents of all files within a folder and its subfolders, similar to the Unix `cat` command — but for entire directory trees.

This tool is particularly useful for diagnostics, debugging, packaging, or reviewing all source files in a project at once.

## Installation

Install using `pip`:

```bash
pip install catdir
```

---

## Usage

```bash
catdir [OPTIONS] PATH
```

### Example

```bash
catdir ./my_project --exclude .env --exclude-noise
catdir ./my_project -e .env -en
catdir ./my_project -e .env -en >> dump.txt
```

These commands output the contents of all readable files under ./my_project, excluding .env and commonly ignored development artifacts such as .git, node_modules, .venv, and others.
The last example redirects the output to a file named dump.txt.

---

## Options

| Option                  | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `-e`, `--exclude`       | Manually exclude specific files or folders by name (can be used multiple times). |
| `-en`, `--exclude-noise`| Automatically exclude common development artifacts (e.g., `.git`, `.venv`, etc.). |
| `-h`, `--help`          | Show usage instructions.                                                    |

---

## Output Format

Each file is prefixed and suffixed with a marker to identify its contents:

```text
# relative/path/to/file.py start file content
<file content here>
# end file content
```

If a file or directory cannot be read, the tool will emit an inline error comment with the reason.

---

## What Is Excluded with `--exclude-noise`?

The `--exclude-noise` flag excludes the following by default:

```text
.venv, venv, .git, .idea, __pycache__, node_modules, dist, build,
.pytest_cache, .mypy_cache, .cache, .eggs, .coverage, coverage.xml,
.tox, .DS_Store, Thumbs.db, .env
```

---

## Development

To install and run locally:

```bash
git clone https://github.com/yourname/catdir.git
cd catdir
pip install -e .
catdir ./example_project --exclude-noise
```

---

## License

MIT License. See [LICENSE](LICENSE) for details.
