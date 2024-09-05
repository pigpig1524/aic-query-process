import streamlit as st

query = st.text_area(label="Input your query")

st.write(f"Your query is {query}")