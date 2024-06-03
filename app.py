import streamlit as st

# Interface do Streamlit
st.title("Aplicação de Soma")

# Entrada de dados
a = st.number_input("Digite o valor de A", value=0)
b = st.number_input("Digite o valor de B", value=0)

# Botão para calcular a soma
if st.button("Calcular", key="calcular_button", help="Clique para calcular a soma"):
    # Cálculo da soma
    soma = a + b
    resultado_texto = f"A soma de {a} + {b} é igual a: {soma}"
    # Exibir o resultado em uma nova janela usando JavaScript
    st.write(f'<script>window.open("data:text/html,<h2>{resultado_texto}</h2>","_blank");</script>', unsafe_allow_html=True)
