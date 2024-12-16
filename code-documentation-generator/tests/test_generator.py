import pytest
from src.doc_generator import CodeDocGenerator

def test_code_doc_generator_initialization():
    """Test if the CodeDocGenerator initializes properly"""
    try:
        generator = CodeDocGenerator()
        assert isinstance(generator, CodeDocGenerator)
    except ValueError:
        pytest.skip("Skipping test: No API key found")

def test_documentation_generation():
    """Test if documentation is generated correctly"""
    generator = CodeDocGenerator()
    
    test_code = """
    def add(a: int, b: int) -> int:
        return a + b
    """
    
    docs = generator.generate_documentation(test_code)
    assert isinstance(docs, dict)
    assert 'overview' in docs
    assert 'functions' in docs
    assert 'parameters' in docs
    assert 'examples' in docs

def test_documentation_formatting():
    """Test if documentation is formatted correctly"""
    generator = CodeDocGenerator()
    
    test_docs = {
        'overview': 'Test overview',
        'functions': 'Test functions',
        'parameters': 'Test parameters',
        'examples': 'Test examples'
    }
    
    formatted = generator.format_documentation(test_docs)
    assert isinstance(formatted, str)
    assert '# Code Documentation' in formatted