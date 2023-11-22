import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from model.senha import senha_email

def enviar_email(txt1,txt2):
    # ------------------ variaveis ---------------

    sender = 'enzzodev@gmail.com'
    password = senha_email

    receiver = 'enzzodev@gmail.com'

    host = 'smtp.gmail.com'
    port = '587'

    subject = 'PARÁGRAFOS DA WIKIPEDIA SOBRE PYTHON'
    body = f"""
        <p>{txt1}</p>
        <p>{txt2}</p>
        <img src = "cid:python_logo" alt = "Python Logo">
    """

    # ----------------- conexão ---------------------

    server = smtplib.SMTP(host,port)
    server.ehlo()
    server.starttls()
    server.login(sender,password)

    # ------------ email -----------------

    msg = MIMEMultipart()

    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

    nome_arquivo = 'C:\\Users\\enzzo.nogueira\\Desktop\\python_logo.png'
    image = open(nome_arquivo, 'rb')
    msg_image = MIMEImage(image.read())
    image.close()

    msg_image.add_header('Content-ID', '<python_logo>')
    msg.attach(msg_image)

    msg.attach(MIMEText(body, 'html'))

    # --------------- envio do email ----------------

    server.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))

    print(f'\nEMAIL ENVIADO COM SUCESSO PARA: {receiver}\n')

    file_path = 'C:\\Users\\enzzo.nogueira\\Desktop\\python_logo.png'
    os.remove(file_path)