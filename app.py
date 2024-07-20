import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('your-name')
    email = request.form.get('your-email')
    message = request.form.get('your-message')

    # Log the received data
    app.logger.info(f"Received submission: Name={name}, Email={email}, Message={message}")

    # Save data to a file
    with open('submissions.txt', 'a') as file:
        file.write(f"Name: {name}, Email: {email}, Message: {message}\n")

    response = {
        'status': 'success',
        'name': name,
        'email': email,
        'message': message
    }
    return jsonify(response)

@app.route('/view_submissions', methods=['GET'])
def view_submissions():
    try:
        with open('submissions.txt', 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return 'No submissions found', 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
