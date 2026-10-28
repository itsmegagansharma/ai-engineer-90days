# Day 06 · Task 1: Modules and packages

> Split notes app into storage.py and main.py. Add an __init__.py folder package. Use if __name__ == '__main__':

## Target layout
```
day06/notes_app/
    __init__.py
    storage.py      # load_notes(), save_notes()
    main.py         # menu loop, imports from storage
```
- [ ] Move file code from day 5 into `storage.py`
- [ ] `main.py` uses `from notes_app.storage import load_notes, save_notes`
- [ ] Add `if __name__ == "__main__":` to main.py
- [ ] Run with `python -m notes_app.main` from inside `day06/`

What does `if __name__ == "__main__":` do?
>
