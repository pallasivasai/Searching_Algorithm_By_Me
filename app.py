import io
from pathlib import Path

import pandas as pd
import streamlit as st

from SAI_Search_Algorithm import SAISearch

st.set_page_config(page_title="SAI Search Algorithm", page_icon="🔎", layout="wide")

st.title("🔎 SAI Search Algorithm")
st.caption("Searching Algorithm by P. Siva Sai")

DEFAULT_CSV_NAME = "data.csv"


def build_from_dataframe(df):
    search = SAISearch()
    columns = list(df.columns)
    if len(columns) >= 2:
        key_col, value_col = columns[0], columns[1]
    elif len(columns) == 1:
        key_col, value_col = columns[0], columns[0]
    else:
        return None, columns

    for _, row in df.iterrows():
        key = str(row[key_col])
        value = str(row[value_col])
        if key.strip():
            search.add_input(key, value)
    search.build()
    return search, columns


@st.cache_data(show_spinner=False)
def read_csv_bytes(data):
    return pd.read_csv(io.BytesIO(data))


uploaded = st.file_uploader("Upload CSV", type=["csv"])

if uploaded is not None:
    df = read_csv_bytes(uploaded.getvalue())
    source_name = uploaded.name
else:
    repo_csv = Path(DEFAULT_CSV_NAME)
    if repo_csv.exists():
        df = pd.read_csv(repo_csv)
        source_name = DEFAULT_CSV_NAME
    else:
        df = None
        source_name = None

if df is None:
    st.info("No CSV found. Add data.csv to the repository or upload a CSV.")
    st.stop()

st.success(f"Loaded: {source_name} | Rows: {len(df)} | Columns: {len(df.columns)}")
st.dataframe(df, use_container_width=True)

search_engine, columns = build_from_dataframe(df)

if search_engine is None:
    st.error("CSV must contain at least one column.")
    st.stop()

st.subheader("Search")
query = st.text_input("Enter a key or value")

if st.button("Search", type="primary", use_container_width=True):
    if not query.strip():
        st.warning("Enter a search term.")
    else:
        result = search_engine.search(query.strip())
        if result is None:
            st.warning("No result found.")
        else:
            st.success("Your search is found")
            st.write(result)

st.divider()
st.subheader("Supported input")
st.write("The SAI algorithm uses the first CSV column as the key and the second CSV column as the value.")
st.write("The original SAI_Search_Algorithm.py remains the core search implementation.")
