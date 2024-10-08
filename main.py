from fastapi import FastAPI
from app.endpoints.chat_with_pdf import router as chat_router
from app.endpoints.upload_pdf import router as upload_router
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

app.include_router(upload_router, prefix="/v1/pdf")
app.include_router(chat_router, prefix="/v1/chat")