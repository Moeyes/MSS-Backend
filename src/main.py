from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "Worldh"}

@app.get("/favicon.ico", include_in_schema=False)
async def get_favicon():
    return FileResponse(Path(__file__).parent.parent / "favicon.ico")