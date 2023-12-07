import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_address, subject, message):
    from_address = "your-email@example.com"
    password = "your-password"

    # Configuración del servidor SMTP
    smtp_host = 'smtp.example.com'
    smtp_port = 587

    try:
        # Crear mensaje
        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        # Conectar al servidor SMTP y enviar el correo
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(from_address, password)
            text = msg.as_string()
            server.sendmail(from_address, to_address, text)

        print("Correo electrónico enviado con éxito.")

    except Exception as e:
        print(f"Error al enviar el correo electrónico: {e}")

# Uso de la función
# send_email('destinatario@example.com', 'Asunto del Correo', 'Cuerpo del Correo')
