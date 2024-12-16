from flask import Flask, render_template, request, jsonify
from doc_generator import CodeDocGenerator
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# Initialize the documentation generator
doc_generator = CodeDocGenerator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    code = request.form.get('code', '')
    if not code:
        return jsonify({'error': 'No code provided'})
    
    docs = doc_generator.generate_documentation(code)
    formatted_docs = doc_generator.format_documentation(docs)
    return jsonify({'documentation': formatted_docs})

if __name__ == '__main__':
    app.run(debug=True)