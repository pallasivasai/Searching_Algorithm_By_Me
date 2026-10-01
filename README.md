# SAI Search Algorithm

### A Secure, Two-Level Hashing Search System
### Implemented in Python by P. Siva Sai

> **Repository correction:** The older README described this project as a Java HashMap program. The current repository implementation is **Python**. The main algorithm is in `SAI_Search_Algorithm.py`, and the interactive web UI is in `app.py`.

## What the repository contains

The project has two connected parts:

1. **SAI Search Algorithm** — the `SAISearch` Python class in `SAI_Search_Algorithm.py`.
2. **Streamlit search application** — `app.py`, which loads CSV data from GitHub or a local upload and searches it using `SAISearch`.

The repository also contains `Reasearch_Paper_Topic.MD`, which documents the algorithm design and theoretical motivation.

## How the Python algorithm works

### Add data

Records are added with:

```python
search.add_input(key, value)
```

Both key and value are converted to strings and stored in `self.items`.

### Build the index

Calling `build()` creates:

- prime modulus `P = 2^61 - 1`
- `m` first-level buckets
- random first-level hash parameters
- one second-level table per bucket

A key is transformed with a secret-based SHA-256 calculation:

```text
SHA-256(secret + key)
       |
       v
integer
       |
       v
mod P
```

The default secret is generated using `secrets.token_bytes(16)`.

### First-level bucket

The implementation calculates:

```text
((a1 * x + b1) mod P) mod m
```

to choose a bucket.

### Second-level table

For a bucket with `b` items, the code creates a table of size:

```text
b²
```

It repeatedly chooses second-level hash parameters until the keys in that bucket occupy different slots.

### Key search

`search(q)` first treats the query as a key.

The key-search path:

1. hashes the query
2. calculates the first-level bucket
3. retrieves the bucket's second-level parameters
4. calculates the second-level slot
5. checks the slot
6. verifies the stored key
7. returns the associated value

### Value search

During `build()`, the code also creates `self.reverse`, a Python dictionary mapping each value to a list of keys.

So if the query is not found as a key, `search(q)` checks the reverse dictionary and then searches using the first associated key.

## Complexity

The research note describes the key lookup design as worst-case O(1). The code itself performs a fixed number of hash/index calculations after the structure has been built.

| Operation | Current implementation |
|---|---|
| Add input | O(1) append before build |
| Build | Repeated bucket/secondary-table construction |
| Key lookup after build | Constant number of hash/index operations |
| Reverse value lookup | Python dictionary lookup, expected O(1) |
| Storage | Secondary tables + reverse dictionary |

The build phase is separate from lookup and is performed before user searches.

## Streamlit application

`app.py` turns the algorithm into an interactive web application.

### Data source

The UI offers:

- **GitHub CSV**
- **Upload CSV**

For GitHub mode, the app calls the GitHub repository tree API, finds files ending in `.csv`, and loads the selected file from its raw GitHub URL.

For upload mode, Streamlit reads the uploaded CSV bytes.

### CSV mapping

The current application uses:

- first CSV column → key
- second CSV column → value

Each usable row is added to `SAISearch`, then `build()` creates the searchable structure.

### Search UI

After loading data, the app shows:

- row count
- column count
- CSV preview
- search input
- Search button

A successful lookup displays:

```text
✅ Your search is found
```

A missing lookup displays:

```text
No result found.
```

## Application flow

```text
GitHub CSV / Uploaded CSV
            |
            v
       pandas DataFrame
            |
            v
 First column = key
 Second column = value
            |
            v
     SAISearch.add_input()
            |
            v
        SAISearch.build()
            |
            v
        search(query)
          /      \
       key       value
        |          |
        +-----> result
```

## Repository files

| File | Purpose |
|---|---|
| `SAI_Search_Algorithm.py` | Core `SAISearch` implementation |
| `app.py` | Streamlit CSV loader, preview and search UI |
| `requirements.txt` | Streamlit and pandas dependencies |
| `Reasearch_Paper_Topic.MD` | Research description and algorithm diagram |
| `New_README.md` | Earlier README draft |

## Technology stack

- Python
- Streamlit
- pandas
- hashlib
- secrets
- urllib / GitHub API
- CSV

## Dependencies

The current `requirements.txt` contains:

```text
streamlit>=1.40
pandas>=2.0
```

## Run the command-line algorithm

```bash
git clone https://github.com/pallasivasai/Searching_Algorithm_By_Me.git
cd Searching_Algorithm_By_Me
python SAI_Search_Algorithm.py
```

The program asks for the number of key-value pairs, reads the key/value entries, builds the index, and then repeatedly accepts key/value search queries until `exit`.

## Run the Streamlit application

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Example command-line flow

```text
Your Using SAI Search Algorithm by P. Siva Sai
How many key-value pairs: 3
Enter key: A
Enter value: APPLE
Enter key: B
Enter value: BANANA
Enter key: C
Enter value: CHERRY
Search key or value (or 'exit'): B
Your search is found: BANANA
Search key or value (or 'exit'): BANANA
Your search is found: APPLE
Search key or value (or 'exit'): exit
```

## Current-code notes

- The executable implementation is **Python**, not Java.
- The repository currently contains no CSV file, so the GitHub CSV option will show no available CSV until one is added; the Upload CSV path remains available.
- Duplicate values are supported by storing a list of matching keys in `self.reverse`.
- The research note contains theoretical/security claims; this README separates those claims from what the current Python code directly implements.

## Links

- [GitHub Repository](https://github.com/pallasivasai/Searching_Algorithm_By_Me)
- [Research Note](https://github.com/pallasivasai/Searching_Algorithm_By_Me/blob/main/Reasearch_Paper_Topic.MD)
