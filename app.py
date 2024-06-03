import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import time

# Configurar a conexão com a API do Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scope)
client = gspread.authorize(creds)

# Função para obter dados do Google Sheets
@st.cache_data(ttl=3600)  # Cache por uma hora
def get_data():
    sheet = client.open("ClimaConecta").sheet1
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df

# Título do aplicativo
st.title("Dados de Temperatura e Umidade")

# Carregar dados
df = get_data()

# Mostrar dados
st.write("Última atualização: ", time.ctime())
st.write(df)

# Adicionar um gráfico interativo
st.line_chart(df[['Temperatura', 'Umidade']])

# Atualizar dados manualmente
if st.button('Atualizar dados'):
    st.cache_data.clear()
    df = get_data()
    st.write("Última atualização: ", time.ctime())
    st.write(df)
    st.line_chart(df[['Temperatura', 'Umidade']])
