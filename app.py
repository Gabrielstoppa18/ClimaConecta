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
    try:
        sheet = client.open("ClimaConecta").sheet1
        data = sheet.get_all_records()
        df = pd.DataFrame(data)
        return df, sheet.col_values(1)  # Retorna também os cabeçalhos das colunas
    except gspread.SpreadsheetNotFound:
        st.error("Planilha não encontrada. Verifique o nome da planilha e se ela foi compartilhada com a conta de serviço.")
        return pd.DataFrame(), []

# Título do aplicativo
st.title("Dados de Temperatura e Umidade")

# Carregar dados
df, headers = get_data()

if not df.empty:
    # Mostrar dados
    st.write("Última atualização: ", time.ctime())
    st.write(df)

    # Verificar se as colunas "Temperatura" e "Umidade" existem
    if 'Temperatura (°C)' in df.columns and 'Umidade (%) ' in df.columns:
        # Adicionar um gráfico interativo
        st.line_chart(df.set_index('Data')[['Temperatura (°C)', 'Umidade (%) ']])
    else:
        st.error("As colunas 'Temperatura' e/ou 'Umidade' não foram encontradas.")
else:
    st.error("Erro ao carregar os dados. Verifique a configuração da planilha.")