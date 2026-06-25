from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from .processing import run_full_compression, process_file_input

app = FastAPI()

# Allow your browser (Tampermonkey) to talk to the server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://gemini.google.com"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Endpoint for raw text input
@app.post("/compress")
async def compress_endpoint(data: dict):
    try:
        raw_text = data.get("text")
        if not raw_text:
            raise HTTPException(status_code=400, detail="No text provided")
        
        compressed = run_full_compression(raw_text)
        return {"compressed_text": compressed}
    except Exception as e:
        print(f"TEXT COMPRESSION ERROR: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# 2. Endpoint for file uploads (PDF, DOCX, TXT)
@app.post("/compress-file")
async def compress_file_endpoint(file: UploadFile = File(...)):
    # Use a unique temporary path
    temp_path = f"temp_{file.filename}"
    try:
        # Save uploaded file temporarily
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Process the file using your existing logic
        compressed = process_file_input(temp_path)
        
        return {"compressed_text": compressed}
    
    except Exception as e:
        print(f"FILE COMPRESSION ERROR: {e}")
        raise HTTPException(status_code=500, detail=str(e))
        
    finally:
        # Cleanup: remove the temp file after processing
        if os.path.exists(temp_path):
            os.remove(temp_path)