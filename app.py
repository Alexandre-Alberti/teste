import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Função para enviar e-mail
def send_email(to_email, subject, body):
    from_email = "fairsis@outlook.com"  # Coloque seu e-mail aqui
    from_password = "fair4321"  # Coloque sua senha aqui
    smtp_server = "smtp.office365.com"  # Coloque o servidor SMTP aqui
    smtp_port = 587  # Porta SMTP

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        st.success('Email enviado com sucesso!')
    except Exception as e:
        st.error(f'Erro ao enviar email: {e}')

# Interface do Streamlit
st.title("Aplicação de Cálculo")

# Entrada de dados
a = st.number_input("Digite o valor de A", value=0)
b = st.number_input("Digite o valor de B", value=0)
email = st.text_input("Digite seu email")

# Botão para calcular
if st.button("Calcular"):
    soma = a + b  # Cálculo da soma
    resultado_texto = f"A soma {a} + {b} é igual a: {soma}"
    st.write(resultado_texto)

    # Enviar resultado por e-mail
    if email:
        try:
            send_email(
                to_email=email,
                subject="Resultado do Cálculo",
                body=resultado_texto
            )
        except Exception as e:
            st.error(f'Erro ao enviar email: {e}')
    else:
        st.error("Por favor, digite um email válido.")
