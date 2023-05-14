from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'your.mail.server'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'yourusername'
app.config['MAIL_PASSWORD'] = 'yourpassword'
app.config['MAIL_DEFAULT_SENDER'] = 'yourdefaultsender'
app.config['MAIL_SUBJECT_PREFIX'] = '[Contact Form]'
app.config['MAIL_SENDER'] = 'Contact Form <noreply@example.com>'

mail = Mail(app)

client = MongoClient('mongodb://mongo:27017')
db = client.contact_form_db

@app.route('/contact', methods=['POST'])
def send_contact_form():
    data = request.get_json()
    name = data['name']
    email = data['email']
    phone = data['phone']
    message = data['message']
    timestamp = datetime.now()

    submission = {
        'name': name,
        'email': email,
        'phone': phone,
        'message': message,
        'timestamp': timestamp
    }
    db.submissions.insert_one(submission)

    msg = Message(
        'New Contact Form Submission',
        recipients=['yourrecipient@example.com']
    )
    msg.body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    mail.send(msg)

    return jsonify({
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3099)
