import streamlit as st

st.set_page_config(page_title="Narrative Viz Tutorial", layout="wide")

st.title("Narrative Visualization Tutorial (Streamlit + Altair)")
st.write(
    "Use the pages in the sidebar:\n"
    "- **Story**: guided narrative (author-driven)\n"
    "- **Explore**: interactive dashboard (reader-driven)\n"
    "- **Methods**: data + limitations\n"
)
st.info("Dataset: `vega_datasets.data.seattle_weather()`")
