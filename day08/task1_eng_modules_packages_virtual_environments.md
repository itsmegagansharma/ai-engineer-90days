# Day 08 · Task 1 · Engineering: Modules, packages & virtual environments

> Split notes app into storage.py and main.py. Add an __init__.py folder package. Use if __name__ == '__main__': Then: python -m venv .venv, activate it, pip install requests, pip freeze > requirements.txt.

## Part 1: Modules and packages

## Target layout
```
day08/notes_app/
    __init__.py
    storage.py      # load_notes(), save_notes()
    main.py         # menu loop, imports from storage
```
- [ ] Move file code from day 5 into `storage.py`
- [ ] `main.py` uses `from notes_app.storage import load_notes, save_notes`
- [ ] Add `if __name__ == "__main__":` to main.py
- [ ] Run with `python -m notes_app.main` from inside `day08/`

What does `if __name__ == "__main__":` do?
>

## Part 2: Virtual environments

## Commands
```
python -m venv .venv
# Windows:      .venv\Scripts\activate
# Mac/Linux:    source .venv/bin/activate
pip install requests
pip freeze > requirements.txt
```
- [ ] Your terminal prompt shows `(.venv)`
- [ ] `requirements.txt` contains `requests`

Why use a virtual environment instead of installing everything globally?
>
