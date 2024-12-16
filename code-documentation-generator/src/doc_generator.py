import os
from typing import Dict, List
from openai import OpenAI
from dotenv import load_dotenv

class CodeDocGenerator:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key not found in environment variables")
        self.client = OpenAI(api_key=self.api_key)

    def generate_documentation(self, code: str) -> Dict[str, str]:
        """
        Generate documentation for the given code snippet.
        
        Args:
            code (str): The source code to document
            
        Returns:
            Dict[str, str]: A dictionary containing different documentation components
        """
        prompt = """
        Analyze the following code and provide documentation in this exact format:
        
        OVERVIEW
        [Your overview here]
        
        FUNCTION EXPLANATIONS
        [Your function explanations here]
        
        PARAMETER DESCRIPTIONS
        [Your parameter descriptions here]
        
        USAGE EXAMPLES
        [Your examples here]
        
        Code to analyze:
        {code}
        """.format(code=code)
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful code documentation assistant. Provide clear, concise, and accurate documentation using the exact format specified."},
                    {"role": "user", "content": prompt}
                ]
            )
            
            documentation = response.choices[0].message.content
            
            # Split by section headers
            try:
                sections = documentation.split('\n\n')
                docs = {}
                
                for section in sections:
                    if 'OVERVIEW' in section:
                        docs['overview'] = section.split('OVERVIEW')[-1].strip()
                    elif 'FUNCTION EXPLANATIONS' in section:
                        docs['functions'] = section.split('FUNCTION EXPLANATIONS')[-1].strip()
                    elif 'PARAMETER DESCRIPTIONS' in section:
                        docs['parameters'] = section.split('PARAMETER DESCRIPTIONS')[-1].strip()
                    elif 'USAGE EXAMPLES' in section:
                        docs['examples'] = section.split('USAGE EXAMPLES')[-1].strip()
                
                # Check if all sections are present
                required_sections = ['overview', 'functions', 'parameters', 'examples']
                for section in required_sections:
                    if section not in docs:
                        docs[section] = "Section not found in generated documentation."
                
                return docs
                
            except Exception as e:
                return {
                    'error': f"Error parsing documentation: {str(e)}",
                    'raw_response': documentation
                }
            
        except Exception as e:
            return {
                'error': f"Error generating documentation: {str(e)}"
            }

    def format_documentation(self, docs: Dict[str, str]) -> str:
        """
        Format the documentation into a readable markdown string.
        
        Args:
            docs (Dict[str, str]): Documentation dictionary
            
        Returns:
            str: Formatted documentation in markdown format
        """
        if 'error' in docs:
            error_msg = f"# Error\n{docs['error']}"
            if 'raw_response' in docs:
                error_msg += f"\n\n# Raw Response\n{docs['raw_response']}"
            return error_msg
            
        markdown = f"""
# Code Documentation

## Overview
{docs['overview']}

## Function Explanations
{docs['functions']}

## Parameters
{docs['parameters']}

## Usage Examples
{docs['examples']}
"""
        return markdown

def main():
    """Example usage of the CodeDocGenerator"""
    doc_generator = CodeDocGenerator()
    
    sample_code = """
    def calculate_statistics(numbers: List[float]) -> Dict[str, float]:
        if not numbers:
            return {'mean': 0, 'median': 0, 'std_dev': 0}
        
        mean = sum(numbers) / len(numbers)
        sorted_nums = sorted(numbers)
        mid = len(numbers) // 2
        median = sorted_nums[mid] if len(numbers) % 2 else (sorted_nums[mid-1] + sorted_nums[mid]) / 2
        
        variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
        std_dev = variance ** 0.5
        
        return {'mean': mean, 'median': median, 'std_dev': std_dev}
    """
    
    docs = doc_generator.generate_documentation(sample_code)
    formatted_docs = doc_generator.format_documentation(docs)
    print(formatted_docs)

if __name__ == "__main__":
    main()