import streamlit as st

if st.button("say hello",key="myButton"):
    st.write("why hello there")
else:
    st.write("Goodbye")
 