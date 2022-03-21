import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

def app():
    st.title('Prediksi sederhana')
    #cetak header
    st.write("""
    #
    Memprediksi jenis dataset yang sudah ada!
    """)

    st.sidebar.header('Parameter Masukan dari Pengguna')

    def user_input_features():
        sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
        sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
        petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
        petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
        data = {'sepal_length': sepal_length,
                'sepal_width': sepal_width,
                'petal_length': petal_length,
                'petal_width': petal_width}
        features = pd.DataFrame(data, index=[0])
        return features

    df = user_input_features()

    st.subheader('Data dari Pengguna')
    st.write(df)

    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target

    clf = RandomForestClassifier()
    clf.fit(X, Y)

    prediction = clf.predict(df)
    prediction_proba = clf.predict_proba(df)

    st.subheader('Label kelas dan nomor indeks yang sesuai')
    st.write(iris.target_names)

    st.subheader('Prediksi')
    st.write(iris.target_names[prediction])
    #st.write(prediction)

    st.subheader('Kemungkinan prediksi')
    st.write(prediction_proba)

    #tentukan simbol
    tickerSymbol = 'GOOGL'
    #bisa ambil salah satu
    #tickerSymbol = 'MSFT' / 'GOOGL' / 'AAPL'

    #dapatkan data tentang ticker 
    tickerData = yf.Ticker(tickerSymbol)
    #harga historis untuk tiket
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits

    st.write("""
    ## Harga penutup
    """)
    st.line_chart(tickerDf.Close)

    st.write("""
        ### Harga volume 
    """)
    st.line_chart(tickerDf.Volume)
