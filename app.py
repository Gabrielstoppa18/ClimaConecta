import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

# Configurar a conexão com a API do Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/your/credentials.json", scope)
client = gspread.authorize(creds)

# Função para obter dados do Google Sheets
@st.cache(ttl=3600)  # Cache por uma hora
def get_data():
    sheet = client.open("temp_umid").sheet1
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
    st.cache.clear()
    df = get_data()
    st.write("Última atualização: ", time.ctime())
    st.write(df)
    st.line_chart(df[['Temperatura', 'Umidade']])
