# Day 2 Lab: Team Bug Bash & Test-Aware Git Workflow 🚀

Welcome to the **Day 2 Collaborative Mini-Project**!

Today, your team inherits a modular **Library Management and Analytics System** composed of four distinct modules. However, the codebase is in a **messy, broken state**: multiple bugs have been introduced, and automated tests are failing across all four modules!

---

## 🎯 The Mission

Your team's objective:
1. **Divide and Conquer**: Each teammate takes responsibility for **one** module and works in an isolated Git feature branch.
2. **Test-Driven Fixes**: Run the unit test suite to clearly see what is broken, fix your module's bug, and get your module's tests to turn 100% green.
3. **Collaborative Integration**: Merge all feature branches into `main`. Because each member worked strictly in their own module, the merges will be clean and conflict-free.
4. **The Magic Moment**: Run the full test suite (`python3 -m unittest -v`). Watch the integration tests pass **magically through the combined effort of the team**!
5. **Publish to GitHub**: Change the Git remote to your personal GitHub repository and push your finished project to GitHub.

---

## 📁 System Architecture

```text
starter-code/
├── sample_data.json         # 4-book JSON database
├── library_app.py           # Application coordinator CLI
├── library_system/          # Core package with 4 modules
│   ├── __init__.py
│   ├── catalog.py           # Module 1 (Dev 1): Book validation, search, average year
│   ├── storage.py           # Module 2 (Dev 2): JSON file I/O & validation
│   ├── borrowing.py         # Module 3 (Dev 3): Checkouts, returns, availability status
│   └── reporting.py         # Module 4 (Dev 4): Inventory metrics & summary report
├── test_catalog.py          # Unit tests for catalog.py
├── test_storage.py          # Unit tests for storage.py
├── test_borrowing.py        # Unit tests for borrowing.py
├── test_reporting.py        # Unit tests for reporting.py
└── test_integration.py      # End-to-end team integration workflow test
```

---

## 🐛 Bug Manifest & Module Assignments

| Teammate | Assigned Module | File to Fix | Failing Tests to Check |
| :--- | :--- | :--- | :--- |
| **Developer 1** | Catalog | `library_system/catalog.py` | `test_catalog.py` (`test_find_books_by_genre_case_insensitive`, `test_calculate_average_year`) |
| **Developer 2** | Storage | `library_system/storage.py` | `test_storage.py` (`test_load_books_invalid_schema_raises_value_error`, `test_storage_utf8_encoding`) |
| **Developer 3** | Borrowing | `library_system/borrowing.py` | `test_borrowing.py` (`test_checkout_book_updates_availability`) |
| **Developer 4** | Reporting | `library_system/reporting.py` | `test_reporting.py` (`test_generate_library_summary_counts`, `test_format_summary_report`) |

---

## 🛠️ Step-by-Step Instructions

### Step 1: Check Out & Inspect the Broken Code

First, verify that you are in the project folder and run the test suite to observe the messy state:

```bash
# Check git status
git status

# Run all tests to observe failures
python3 -m unittest -v
```

Notice how `test_catalog.py`, `test_storage.py`, `test_borrowing.py`, `test_reporting.py`, and `test_integration.py` all report failures!

---

### Step 2: Create Your Feature Branch

Each teammate creates an isolated branch to work on their assigned module:

```bash
# Developer 1:
git checkout -b fix/catalog

# Developer 2:
git checkout -b fix/storage

# Developer 3:
git checkout -b fix/borrowing

# Developer 4:
git checkout -b fix/reporting
```

---

### Step 3: Fix Your Module & Verify with Tests

Open your assigned file in `library_system/` and resolve the bugs marked with `# TODO`:

- **Developer 1 (`library_system/catalog.py`)**:
  - Update `find_books_by_genre` to perform case-insensitive comparisons: `g.strip().lower() == genre.strip().lower()`.
  - Fix `calculate_average_year`: safely return `0.0` when `books` is empty, and calculate `float(total / len(books))`.
  - Verify with: `python3 -m unittest test_catalog.py -v` (All tests must pass!).

- **Developer 2 (`library_system/storage.py`)**:
  - In `load_books`: open files with `encoding="utf-8"`, and check `if not isinstance(data, list): raise ValueError(...)`.
  - In `save_books`: open files with `encoding="utf-8"` and use `ensure_ascii=False`.
  - Verify with: `python3 -m unittest test_storage.py -v` (All tests must pass!).

- **Developer 3 (`library_system/borrowing.py`)**:
  - In `checkout_book`: set `target_book["is_available"] = False` when a book is checked out.
  - Verify with: `python3 -m unittest test_borrowing.py -v` (All tests must pass!).

- **Developer 4 (`library_system/reporting.py`)**:
  - In `generate_library_summary`: fix the inverted count logic. Count books with `b.get("is_available") is True` as available, and `False` as borrowed.
  - Verify with: `python3 -m unittest test_reporting.py -v` (All tests must pass!).

---

### Step 4: Stage & Commit Your Changes

Once your module tests pass, stage your modified file and record a clean, descriptive commit:

```bash
# Check which files you touched (should only be your module!)
git status

# Stage only your module
git add library_system/<your_module>.py

# Commit with a meaningful message
git commit -m "Fix: resolve case-insensitivity and average year bugs in catalog"
```

---

### Step 5: Merge All Fixes into `main`

Switch back to `main` and merge each feature branch:

```bash
git checkout main

# Merge each branch (or submit PRs on GitHub)
git merge fix/catalog
git merge fix/storage
git merge fix/borrowing
git merge fix/reporting
```

Because each developer worked on a separate file, Git merges them cleanly without any merge conflicts!

---

### Step 6: The Magic Moment — Run the Entire Test Suite!

Now that all individual fixes have been assembled:

```bash
python3 -m unittest -v
```

🎉 **100% OK!** All unit tests and the integration test `test_integration.py` pass automatically!

Run the application CLI to see the full system in action:

```bash
python3 library_app.py
```

---

### Step 7: Push to Your Personal GitHub Repository

Now connect your local repository to your personal GitHub account:

1. Go to [github.com](https://github.com) and click **New Repository**.
2. Name it `python-day2-library-system` (set it to Public or Private). Do **not** check "Initialize with README".
3. Copy the repository URL (HTTPS or SSH).
4. Update your local git remote:

```bash
# View existing remote (if any)
git remote -v

# Change remote URL to your personal repository:
git remote set-url origin https://github.com/<your-username>/python-day2-library-system.git

# (Or if no origin exists, add it):
# git remote add origin https://github.com/<your-username>/python-day2-library-system.git

# Ensure your default branch is main
git branch -M main

# Push all commits and branches to GitHub
git push -u origin main
```

Verify your repository on GitHub! You should see your commit history, clean branches, and passing code.
