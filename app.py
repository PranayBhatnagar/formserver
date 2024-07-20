import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('your-name')
    email = request.form.get('your-email')
    message = request.form.get('your-message')

    # Here you can process the data, save it to a database, or send an email

    response = {
        'status': 'success',
        'name': name,
        'email': email,
        'message': message
    }
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
