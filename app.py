import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles.csv')

st.header("Gestão de Vendas de Carros")

hist_button = st.button('Criar histograma')
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')
if scatter_button:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Criando as checkboxes
hist_checkbox = st.checkbox('Mostrar histograma')
scatter_checkbox = st.checkbox('Mostrar gráfico de dispersão')

if hist_checkbox:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if scatter_checkbox:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)