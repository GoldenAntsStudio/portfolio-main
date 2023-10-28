#Импорт
from flask import Flask, render_template,request, redirect
import smtplib

from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект
from email.mime.text import MIMEText                # Текст/HTML
from email.mime.image import MIMEImage    


app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)

@app.route('/feedback')
def feedback():
    email = request.form.get('email')
    text = request.form.get('text')

    with open("otus.txt", "w") as file:
        file.write(email + text)

 

if __name__ == "__main__":
    app.run(debug=True)