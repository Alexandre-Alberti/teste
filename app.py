import streamlit as st
import webbrowser

# Interface do Streamlit
st.title("Aplicação de Soma")

# Entrada de dados
a = st.number_input("Digite o valor de A", value=0)
b = st.number_input("Digite o valor de B", value=0)

# Botão para calcular a soma
if st.button("Calcular", help="Clique para calcular a soma"):
    # Cálculo da soma
    soma = a + b
    resultado_texto = f"A soma de {a} + {b} é igual a: {soma}"
    # Exibir o resultado
    st.write(resultado_texto)
    # Abrir o resultado em uma nova janela do navegador
    script = f"""
    <script>
    var myWindow = window.open("", "_blank", "width=600,height=400");
    myWindow.document.write("<p>{resultado_texto}</p>");
    </script>
    """
    st.write(script, unsafe_allow_html=True)
