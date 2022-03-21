import streamlit as st
from multiapp import MultiApp
import yfinance as yf
import pandas as pd
from PIL import Image
# impor modul aplikasi neng kene BOSS!!!
from apps import home, data, model, coba1
from part_dna import dna
from prediksi1 import penguins


app = MultiApp()

st.markdown("""
# Aplikasi Simple DataScience

berbagai macam project Data-Science.

""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("DNA", dna.app)
app.add_app("Prediksi sederhana dengan data Iris", coba1.app)
app.add_app("Prediksi dengan input dari user", penguins.app)
app.add_app("Model", model.app)
# The main app
app.run()
