import  os
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['DEBUG'] = True
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = 'kaniket7209@gmail.com'
    app.config['MAIL_PASSWORD'] = os.environ.get("pass")
    app.config['MAIL_DEFAULT_SENDER'] = "kaniket7209@gmail.com"
    app.config['MAIL_MAX_EMAILS'] = None

    mail = Mail(app)


    @app.route('/')
    def index():
        return render_template("home.html")

    @app.route('/send_message', methods = ['GET', 'POST'])
    def send_message():
        if(request.method == 'POST'):
            email = request.form['email']
            subject = request.form['subject']
            msg = request.form['message']

            message = Message(subject, sender="kaniket7209@gmail.com", recipients=[email])

            message.body = msg # .html will make it in html format 
            with app.open_resource('hii.jpg') as hii:
                message.attach('hii.jpg', 'image/jpg', hii.read())
                
            mail.send(message)
            success = "Message sent"
            return render_template("result.html",success=success)

    return app