# Compresso  : Token Reducing Platform 

**Compresso** is a local bridge written in Python which improves the experience of interacting with Google Gemini by providing intelligent, token-saving compression of large documents and text prompts from the browser.

## 🛠 Features
- **Smart Compression:** Makes use of `LLMLingua` for efficient compression of prompt tokens without losing semantic sense.
- **File Uploader:** Extracts and compresses texts from **PDF, DOCX, and TXT** files in an efficient manner.
- **Easy Integration:** Adds the ability to compress and upload through the "Compress" and "Upload" buttons in the Gemini website via Tampermonkey.

# Step by Step Procedure 

### 1. Requirements
- [Python 3.10+](https://www.python.org/)
- [Tampermonkey](https://www.tampermonkey.net/) browser extension

### 2. Installation
Install the project by running these commands:

```bash
git clone https://github.com/YOUR_USERNAME/Compresso.git
cd Compresso

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\activate  # On Windows

# Install dependencies
pip install fastapi uvicorn spacy llmlingua tiktoken google-genai pypdf python-docx python-multipart
python -m spacy download en_core_web

### 3. Running the Server
- Start your terminal in the Compresso folder.
- Ensure your virtual environment is activated.
- Run the following command:

python -m uvicorn app.main:app --reload

### 4. Setting Up Tampermonkey 
- Install the Tampermonkey extension in your browser.
- Create a new script in Tampermonkey and paste the contents of `scripts/Compresso_bridge.js` into it.
- Save the script and ensure it is enabled.
