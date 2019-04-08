from flask import Flask, flash, render_template, redirect
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, validators
import sys, os

#Config
MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=465
MAIL_USE_TLS=False
MAIL_USE_SSL=True
MAIL_USERNAME='example@gmail.com'
MAIL_PASSWORD='your password'
MAIL_DEFAULT_SENDER='this is optional'

app = Flask(__name__, template_folder='templates')
app.config.from_object(__name__)
mail = Mail(app)
app.secret_key = "key"

class MailForm(FlaskForm):
    recipients = StringField('Recipient(s)', [validators.InputRequired()])
    body = StringField('Body')
    attachment = FileField('Attachment')

@app.route("/", methods=('GET', 'POST'))
def index():
    form = MailForm()
    if form.validate_on_submit():
        msg = Message('Mail from Flask-Mail Demo',
            recipients=[form.recipients.data])
        msg.body = form.body.data
        filename = form.attachment.data.filename
        form.attachment.data.save(os.path.join('<path>', filename))
        with app.open_resource(filename) as fp:
            msg.attach(form.attachment.data.filename, 'image/png', fp.read())
        mail.send(msg)
        flash('Email sent!')
        return redirect('/')
    return render_template('index.html', form=MailForm())

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5110)
