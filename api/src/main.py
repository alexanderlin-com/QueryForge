from fastapi import FastAPI, File, Form, UploadFile
from typing import Annotated
import shutil
import uuid
from pathlib import Path

app = FastAPI()

# A temporary directory to store uploaded CSVs. 
# In a real Docker setup, this would be a shared volume.
TEMP_UPLOADS_DIR = Path("/tmp/query_forge_uploads")


@app.post("/analyze")
async def analyze(
    file: Annotated[UploadFile, File()],
    query: Annotated[str, Form()],
):
    # Ensure the temporary directory exists
    TEMP_UPLOADS_DIR.mkdir(exist_ok=True)

    # Create a unique path to save the file to prevent collisions
    # e.g., /tmp/query_forge_uploads/some-unique-id_test_data.csv
    temp_file_path = TEMP_UPLOADS_DIR / f"{uuid.uuid4()}_{file.filename}"

    # Stream the uploaded file content to the new file on disk
    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    finally:
        # Make sure to close the file handle from the upload
        file.file.close()

    # The rest of the logic will go here...

    return {
        "filename": file.filename,
        "query": query,
        "status": "file_saved",
        "temp_path": str(temp_file_path) # Return path for verification
    }