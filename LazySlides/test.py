
#//how to add image and text in a single line streamlit in python ?
#A streamlit app with two centered texts with different seizes
import streamlit as st

st.markdown("<h1 style='text-align: center; color: grey;'>Big headline</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: black;'>Smaller headline in black </h2>", unsafe_allow_html=True)


import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.write(' ')


