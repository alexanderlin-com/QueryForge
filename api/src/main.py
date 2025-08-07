from fastapi import FastAPI, File, Form, UploadFile
from typing import Annotated

app = FastAPI()


@app.post("/analyze")
async def analyze(
    file: Annotated[UploadFile, File()],
    query: Annotated[str, Form()],
):
    # This is where the magic will happen.
    # For now, we're just proving the endpoint works.
    
    # We'll need to add logic here to:
    # 1. Save the `file` to a temporary directory.
    # 2. Pass the `query` and the file path to the llm_handler.
    # 3. Get a script back.
    # 4. Send the script and file path to the sandbox_client.
    # 5. Return the result.

    return {"filename": file.filename, "query": query, "status": "received"}