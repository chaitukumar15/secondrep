
import streamlit as st 
import requests as req 

st.markdown("hi i am chaitanya")

btn=st.button("submit")


if btn:
    res=req.get("https://fakestoreapi.com/products")
    data=res.json()
    st.markdown(data)