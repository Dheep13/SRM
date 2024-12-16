# Code Documentation Generator

A Python-based tool that automatically generates comprehensive documentation for code snippets using OpenAI's GPT API.

## Features
- Web interface for easy code input
- Generates detailed documentation including:
  - Code overview
  - Function explanations
  - Parameter descriptions
  - Usage examples
- Markdown formatted output
- Real-time documentation generation

## Prerequisites
- Python 3.x
- OpenAI API key

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Dheep13/SRM.git
cd SRM/code-documentation-generator
```

### 2. Install required packages
```bash
pip install openai python-dotenv flask
```

### 3. Configuration
Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

### 4. Run the application
```bash
python src/app.py
```

### 5. Access the web interface
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## Project Structure
```
code-documentation-generator/
├── src/
│   ├── templates/
│   │   └── index.html     # Web interface
│   ├── __init__.py
│   ├── doc_generator.py   # Core documentation generator
│   └── app.py            # Flask web application
├── tests/
├── .env                  # API key configuration
└── requirements.txt      # Project dependencies
```

## Usage
1. Open the web interface at http://127.0.0.1:5000
2. Paste your code in the text area
3. Click "Generate Documentation"
4. View the comprehensive documentation generated below

## Error Handling
- Ensure your OpenAI API key is correctly set in .env file
- Check internet connection if documentation generation fails
- Verify all files are in their correct locations

## License
MIT License