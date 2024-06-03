import streamlit as st
import os

# Interface do Streamlit
st.title("Aplicação de Cálculo")

# Entrada de dados
a = st.number_input("Digite o valor de A", value=0)
b = st.number_input("Digite o valor de B", value=0)

# Campo de entrada para o caminho da pasta
caminho_pasta = st.text_input("Digite o caminho da pasta para salvar o arquivo")

if st.button("Calcular"):
    soma = a + b  # Cálculo da soma
    resultado_texto = f"A soma {a} + {b} é igual a: {soma}"
    st.write(resultado_texto)

    # Verificar se o caminho da pasta é válido
    if os.path.isdir(caminho_pasta):
        # Salvar resultado em um arquivo
        nome_arquivo = os.path.join(caminho_pasta, "resultado.txt")
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write(resultado_texto)

        st.success(f"Resultado salvo no arquivo: {nome_arquivo}")
    else:
        st.error("Caminho da pasta inválido. Por favor, insira um caminho válido.")
