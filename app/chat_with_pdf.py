import os
from fastapi import APIRouter, HTTPException, Request
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS

router = APIRouter()

genai.configure(api_key=os.getenv("API_KEY"))

def get_prompt(context, question):
    return """
    Please Answer the question based on the context provided. If the answer is not provided in context, please indicate that
    its not provided. Write the results in plain text\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

@router.post("/{pdf_id}")
async def chat_with_pdf(request: Request, question, pdf_id):
    model = genai(model="gemini-1.5-flash")
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001")

    pdf = FAISS.load_local(f"{pdf_id}.pdf", embeddings)
    if pdf:
         prompt = PromptTemplate(template=get_prompt(pdf, question))
    else: 
        raise Exception("pdf was not found")
    
    response = model.generate_context(prompt)
    

    if response:
        return response.text
    else: 
        raise HTTPException()