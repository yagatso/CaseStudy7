import uuid
from PyPDF2 import PdfReader
from fastapi import APIRouter, HTTPException, UploadFile
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("")
async def upload_and_process_pdf(file: UploadFile):
    
    unique_id = str(uuid.uuid4())

    tmp = ""
    tmp.write(await file.read())

    chunks = await get_chunks(tmp)

    save_to_local(unique_id, chunks)

    pdf_data = {
        "pdf_id": unique_id,
        "filename": file.filename,
        "text": chunks
    }

    return JSONResponse(pdf_data)

def save_to_local(unique_id, chunks):
    vectorstore = FAISS.from_texts(documents=chunks, embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"))
    vectorstore.save_local(f"pdf_{unique_id}.pdf")

def get_chunks(file):
    text = ""
    pdf_reader = PdfReader(file)
    for page in pdf_reader:
        text += page.extract_text()
    
    #get chunks from text
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(text)
    return chunks