import streamlit as st
import json

# Lee los datos generados por chasky.py
with open("resumen.json", "r") as f:
    data = json.load(f)

st.title("Dashboard de Chasky")
st.write("Resumen de correos:")
st.json(data)