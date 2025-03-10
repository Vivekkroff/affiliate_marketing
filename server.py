from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for newsletter subscription
@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    # Save email to database or send to email service
    return jsonify({"message": "Thank you for subscribing!"})

if __name__ == '__main__':
    app.run(debug=True)