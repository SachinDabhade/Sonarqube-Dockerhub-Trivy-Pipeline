from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route for testing GET request
@app.route('/')
def home():
    return "Welcome to the Flask Test App! Try the form below."

# Route for testing POST request (form submission)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        message = f"Hello, {name}! Your form has been submitted successfully."
        return render_template('submit.html', message=message)
    return render_template('form.html')

# Route to test JSON response (GET)
@app.route('/api/test', methods=['GET'])
def api_test():
    return jsonify({"message": "This is a simple JSON response for testing!"})

if __name__ == '__main__':
    app.run(debug=True)
