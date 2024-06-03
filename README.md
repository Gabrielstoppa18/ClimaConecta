# ClimaConecta

**ClimaConecta** é um projeto inovador que monitora e registra a temperatura e umidade ambiente em tempo real, utilizando um sensor conectado ao ESP8266. Os dados coletados são enviados automaticamente para uma planilha do Google Sheets a cada hora e disponibilizados em uma interface web interativa, criada com Streamlit. Ideal para quem deseja acompanhar as condições climáticas de um local específico, seja em casa, no trabalho ou em um ambiente de pesquisa.

## Recursos

- **Monitoramento Contínuo:** Leitura de temperatura e umidade a cada hora.
- **Armazenamento em Nuvem:** Dados registrados em uma planilha do Google Sheets.
- **Interface Web Interativa:** Visualização dos dados atualizados em tempo real através de um site criado com Streamlit.
- **Atualização Automática:** Site atualizado automaticamente com os novos dados coletados.

## Benefícios

- **Fácil Acesso:** Consulte os dados de qualquer lugar, a qualquer hora.
- **Visualização Clara:** Gráficos e tabelas interativos para facilitar a análise dos dados.
- **Confiabilidade:** Dados armazenados de forma segura na nuvem.

## Implementação

### Hardware

- ESP8266
- Sensor de temperatura e umidade DHT11

### Software

- Arduino IDE para programação do ESP8266
- Google Sheets para armazenamento de dados
- Streamlit para a criação da interface web
