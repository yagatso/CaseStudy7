import uuid
from PyPDF2 import PdfReader
from fastapi import APIRouter, UploadFile
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("")
async def generate_chunks(pdf_docs: UploadFile):
    #extract all texts
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader:
             text += page.extract_text()
    
    #get chunks from text
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(text)

    unique_id = str(uuid.uuid4())

    vectorstore = Chroma.from_texts(documents=chunks, embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"))
    vectorstore.save_local(f"pdf_{unique_id}.pdf")

    pdf_data = {
        "text": chunks,
        "unique_id": id
    }

    return JSONResponse(pdf_data)