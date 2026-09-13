import io
import json
import urllib.request
from pathlib import Path

import pandas as pd
import streamlit as st

from SAI_Search_Algorithm import SAISearch

st.set_page_config(
    page_title="SAI Search Algorithm",
    page_icon="🔎",
    layout="wide",
)

st.title("🔎 SAI Search Algorithm")
st.caption("Searching Algorithm by P. Siva Sai")

OWNER = "pallasivasai"
REPO = "Searching_Algorithm_By_Me"
BRANCH = "main"


def github_csv_files():
    """Find CSV files directly from the public GitHub repository."""
    try:
        url = f"https://api.github.com/repos/{OWNER}/{REPO}/git/trees/{BRANCH}?recursive=1"
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "SAI-Search-Algorithm-App"},
        )
        with urllib.request.urlopen(request, timeout=15) as response:
            data = json.loads(response.read().decode("utf-8"))

        return [
            item["path"]
            for item in data.get("tree", [])
            if item.get("type") == "blob"
            and item.get("path", "").lower().endswith(".csv")
        ]
    except Exception:
        return []


def github_csv_url(path):
    return f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}/{path}"


@st.cache_data(show_spinner=False)
def read_csv_url(url):
    return pd.read_csv(url)


@st.cache_data(show_spinner=False)
def read_csv_bytes(data):
    return pd.read_csv(io.BytesIO(data))


def build_from_dataframe(df):
    search = SAISearch()
    columns = list(df.columns)

    if not columns:
        return None, columns

    key_col = columns[0]
    value_col = columns[1] if len(columns) >= 2 else columns[0]

    for _, row in df.iterrows():
        key = str(row[key_col])
        value = str(row[value_col])
        if key.strip() and key.lower() != "nan":
            search.add_input(key, value)

    search.build()
    return search, columns


# ============================================================
# DATA SOURCE
# ============================================================

st.subheader("📂 Data Source")

source = st.radio(
    "Choose CSV source",
    ["GitHub CSV", "Upload CSV"],
    horizontal=True,
)

df = None
source_name = None

if source == "GitHub CSV":
    csv_files = github_csv_files()

    if csv_files:
        selected = st.selectbox(
            "CSV file from GitHub",
            csv_files,
        )

        if st.button("Load GitHub CSV", type="primary"):
            try:
                df = read_csv_url(github_csv_url(selected))
                st.session_state["sai_df"] = df
                st.session_state["sai_source"] = selected
            except Exception as exc:
                st.error(f"Could not read GitHub CSV: {exc}")

    else:
        st.warning(
            "No .csv file is currently present in the GitHub repository. "
            "Add a CSV to this repository and refresh the app."
        )

else:
    uploaded = st.file_uploader(
        "Upload CSV",
        type=["csv"],
    )

    if uploaded is not None:
        try:
            st.session_state["sai_df"] = read_csv_bytes(uploaded.getvalue())
            st.session_state["sai_source"] = uploaded.name
        except Exception as exc:
            st.error(f"Could not read CSV: {exc}")


# Keep loaded data across Streamlit reruns.
df = st.session_state.get("sai_df")
source_name = st.session_state.get("sai_source")

if df is None:
    st.info(
        "Select a GitHub CSV or upload a CSV to start searching."
    )
    st.stop()


# ============================================================
# DATA PREVIEW
# ============================================================

st.success(
    f"Loaded: {source_name} | Rows: {len(df)} | Columns: {len(df.columns)}"
)

with st.expander("Preview CSV", expanded=True):
    st.dataframe(
        df,
        use_container_width=True,
        height=350,
    )


# ============================================================
# SAI SEARCH
# ============================================================

search_engine, columns = build_from_dataframe(df)

if search_engine is None:
    st.error("CSV does not contain usable columns.")
    st.stop()

st.subheader("🔎 Search")

query = st.text_input(
    "Search key or value",
    placeholder="Enter a key or value...",
)

if st.button(
    "Search",
    type="primary",
    use_container_width=True,
):
    if not query.strip():
        st.warning("Please enter a search term.")
    else:
        result = search_engine.search(query.strip())

        if result is None:
            st.warning("No result found.")
        else:
            st.success("✅ Your search is found")
            st.write(result)


st.divider()

st.subheader("⚙️ How this app works")
st.write(
    "The first CSV column is treated as the search key and the second "
    "column as its value. The actual search is performed by the "
    "SAI_Search_Algorithm.py implementation."
)

st.caption(
    "GitHub repository: pallasivasai/Searching_Algorithm_By_Me"
)
