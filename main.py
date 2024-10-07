from fastapi import FastAPI
from app.chat_with_pdf import router as chat_router
from app.upload_pdf import router as upload_router

app = FastAPI()

app.include_router(upload_router, prefix="/v1/pdf")
app.include_router(chat_router, prefix="/v1/chat")