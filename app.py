import streamlit as st

# Interface do Streamlit
st.title("Aplicação de Soma")

# Variável para armazenar o último resultado
ultimo_resultado = None

# Entrada de dados
a = st.number_input("Digite o valor de A", value=0)
b = st.number_input("Digite o valor de B", value=0)

# Botão para calcular a soma
if st.button("Calcular", help="Clique para calcular a soma"):
    # Cálculo da soma
    soma = a + b
    ultimo_resultado = f"A soma de {a} + {b} é igual a: {soma}"

# Exibir o último resultado
if ultimo_resultado:
    st.write(ultimo_resultado)
