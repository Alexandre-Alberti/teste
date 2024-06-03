import streamlit as st
import os

# Interface do Streamlit
st.title("Aplicação de Cálculo")

# Entrada de dados
a = st.number_input("Digite o valor de A", value=0)
b = st.number_input("Digite o valor de B", value=0)

# Campo de entrada para o caminho da pasta
caminho_pasta = st.text_input("Digite o caminho da pasta para salvar o arquivo")

# Campo de entrada para o nome do arquivo
nome_arquivo = st.text_input("Digite o nome do arquivo")

# Botão para calcular e salvar o resultado
if st.button("Calcular"):
    # Verificar se o caminho da pasta e o nome do arquivo foram inseridos
    if caminho_pasta.strip() != "" and nome_arquivo.strip() != "":
        # Verificar se o caminho da pasta é válido
        if os.path.isdir(caminho_pasta):
            # Cálculo da soma
            soma = a + b
            resultado_texto = f"A soma {a} + {b} é igual a: {soma}"
            st.write(resultado_texto)

            # Salvar resultado em um arquivo
            caminho_arquivo = os.path.join(caminho_pasta, f"{nome_arquivo}.txt")
            with open(caminho_arquivo, "w") as arquivo:
                arquivo.write(resultado_texto)

            st.success(f"Resultado salvo no arquivo: {caminho_arquivo}")
        else:
            st.error("Caminho da pasta inválido. Por favor, insira um caminho válido.")
