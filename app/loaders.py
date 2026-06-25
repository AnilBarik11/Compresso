import pypdf
import docx

def load_text(file_path: str) -> str:
    """Detects file type and extracts text."""
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
            
    elif file_path.endswith('.pdf'):
        text = ""
        with open(file_path, 'rb') as f:
            reader = pypdf.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
        
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
        
    else:
        raise ValueError("Unsupported file format")