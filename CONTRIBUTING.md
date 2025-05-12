# Contributing to catdir

Thank you for your interest in contributing to `catdir`!

We welcome all contributions — bug reports, feature ideas, documentation improvements, or pull requests.

---

## 🛠️ Getting Started

1. **Fork the repository**
2. **Clone your fork locally**  
```bash
git clone https://github.com/your-username/catdir.git
cd catdir
```

3. **Install in editable mode**  
```bash
pip install -e .
```

4. **Run tests**  
Make sure everything works:
```bash
pytest
```

---

## ✅ How to Contribute

### 🐛 Report Bugs
Please open an [issue](https://github.com/emilastanov/catdir/issues) with:
- A clear title
- Steps to reproduce
- Expected vs actual behavior

### 💡 Request Features
Use the `Feature Request` issue template. Explain the use case and motivation.

### 🔀 Submit a Pull Request
1. Create a new branch:  
   `git checkout -b feature/your-feature-name`
2. Make your changes.
3. Format your code with `black`:
   ```bash
   pip install black
   black catdir/
   ```
4. Ensure all tests pass:  
   `pytest`
5. Commit and push:  
   `git commit -m "Add feature xyz"`  
   `git push origin feature/your-feature-name`
6. Open a Pull Request and link to the related issue if applicable.

---

## 📦 Project Structure

- `catdir/` – CLI and core logic
- `tests/` – Unit tests for CLI and internals
- `README.md` – Main documentation
- `setup.py`, `pyproject.toml` – Build configuration

---

## 💬 Questions?

Feel free to open a discussion or ask in an issue.

Thank you for helping improve `catdir`! 🙌