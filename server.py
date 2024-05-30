from flask import Flask, render_template, request
from flask_mail import Mail, Message
app = Flask(__name__)

# Configuración del servidor de correo de Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'rafambravo1@gmail.com' # Escribe tu email
app.config['MAIL_PASSWORD'] = 'faxj tsit gbjo kfkp' # Contraseña de aplicación
app.config['MAIL_DEFAULT_SENDER'] = 'rafambravo1@gmail.com' # Escribe tu email

mail = Mail(app)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    usuario = request.form['username']  # Accede al campo "usuario"
    passw = request.form['pass']  # Accede al campo "pass"
    if usuario == "admin" and passw == "1234":
        return render_template("video.html")
    else:
        return render_template("index.html", error="Usuario o contraseña incorrectos.")

@app.route("/registrar_presencia", methods=["GET"])
def registrar_presencia():
    msg = Message("Alerta: Presencia detectada",
                  recipients=["rafambravo1@gmail.com"])
    msg.body = "Se ha detectado una presencia del sensor PIR. Accede aquí para ver la cámara <a href='192.168.1.123:5000/'>Ver vídeo</a>" # LA IP DE TU ORDENADOR
    try:
        mail.send(msg)
        print("Correo enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")