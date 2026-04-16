import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, request, jsonify
from ai.nlp_model import analyze_complaint
from ai.cv_model import classify_waste
from ai.decision import decide_priority

app = Flask(__name__)

# Root endpoint
@app.route('/')
def home():
    return '''
    <h1>Welcome to SwachhSaathi AI!</h1>
    <p>Use the form below to submit a complaint:</p>
    <form action="/submit_complaint" method="post">
        <label for="text">Complaint Text:</label><br>
        <textarea name="text" id="text" rows="4" cols="50"></textarea><br><br>
        <label for="image_path">Image Path (optional):</label><br>
        <input type="text" name="image_path" id="image_path"><br><br>
        <input type="submit" value="Submit Complaint">
    </form>
    '''

# Endpoint for submitting complaint
@app.route('/submit_complaint', methods=['POST'])
def submit_complaint():
    try:
        # Handle both JSON and form data
        if request.is_json:
            data = request.json
            text = data.get('text', '')
            image_path = data.get('image_path', '')
        else:
            text = request.form.get('text', '')
            image_path = request.form.get('image_path', '')

        # Analyze complaint
        category, priority = analyze_complaint(text)

        # Classify waste if image provided
        waste_type = None
        if image_path and os.path.exists(image_path):
            waste_type = classify_waste(image_path)

        # Decide final priority
        final_priority = decide_priority(category, priority, waste_type)

        # Generate alert (for demo, just return response)
        response = {
            'category': category,
            'priority': final_priority,
            'waste_type': waste_type,
            'message': 'Complaint processed successfully. Alert sent to authorities.'
        }

        if request.is_json:
            return jsonify(response)
        else:
            return f'''
            <h2>Complaint Submitted!</h2>
            <p><strong>Category:</strong> {category}</p>
            <p><strong>Priority:</strong> {final_priority}</p>
            <p><strong>Waste Type:</strong> {waste_type or 'Not provided'}</p>
            <p><strong>Message:</strong> {response['message']}</p>
            <a href="/">Submit Another Complaint</a>
            '''
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        if request.is_json:
            return jsonify({'error': error_msg}), 500
        else:
            return f'<h2>Error!</h2><p>{error_msg}</p><a href="/">Try Again</a>', 500

if __name__ == '__main__':
    app.run(debug=True)