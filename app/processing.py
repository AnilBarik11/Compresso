from .preprocessor import clean_prompt
from .compressor import compress
from .compiler import inject_context
from .loaders import load_text 

def run_full_compression(raw_text: str) -> str:
    """The core pipeline for text compression."""
    # 1. Clean the text
    cleaned = clean_prompt(raw_text)
    
    # 2. Compress the text using LLMLingua
    compressed = compress(cleaned, rate=0.4)
    
    # 3. Wrap it in a system prompt template
    final_prompt = inject_context(compressed, task_role="Efficient Analyst")
    
    return final_prompt

def process_file_input(file_path: str) -> str:
    """
    New function to handle files:
    1. Loads content from any supported format (PDF/DOCX/TXT)
    2. Runs it through the existing compression pipeline
    """
    # 1. Standardize: Convert file to string
    raw_text = load_text(file_path)
    
    # 2. Pipeline: Reuse your existing compression logic
    return run_full_compression(raw_text)