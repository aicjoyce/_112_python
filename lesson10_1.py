import streamlit as st


def button_click():
    st.write(st.session_state)
if st.button("say hello",key="myButton",on_click=button_click):
    st.write("why hello there")
else:
    st.write("Goodbye")
 