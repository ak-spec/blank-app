import streamlit as st

st.set_page_config(page_title="FYP App", page_icon="🎓")

st.title("FYP App")
st.write("Deployed on Streamlit Community Cloud. Replace this with your app.")

name = st.text_input("Your name")
if name:
    st.success(f"Hello, {name}!")
