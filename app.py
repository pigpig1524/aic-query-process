import streamlit as st
from agent import Agent

client = Agent()

with st.form("form"):
    query = st.text_input(label="**Input your query**")
    submit = st.form_submit_button("Process")

if submit:
    st.write(client.run(input=query))