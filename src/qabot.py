# -*- encoding: utf-8 -*-
from langchain_community.llms import  CTransformers
from langchain.chains import  RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import FAISS
from prepare_vector_db import vector_db_path
from transformers import AutoModelForCausalLM, AutoTokenizer


# Cau hinh
model_file = "../models/vinallama-7b-chat_q5_0.gguf"
vector_db_path = "../vectorstores/db_faiss"

# Load LLM
def load_llm(model_file):
    llm = CTransformers(
        model=model_file,
        model_type="llama",
        max_new_tokens=1024,
        temperature=0.01,
    )
    return llm

# Tao prompt template
def create_prompt(template):
    prompt = PromptTemplate(template = template, input_variables=["context", "question"])
    return prompt

# Tao simple chain
def create_qa_chain(prompt, llm, db):
    llm_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever = db.as_retriever(search_kwargs= {"k":2}, max_tokens_limit=1024),
        return_source_documents = False,
        chain_type_kwargs = {'prompt':prompt}
    )
    return  llm_chain

# Read tu VectorDB
def read_vectors_db():
    # Embedding
    embedding_model = GPT4AllEmbeddings(model_file="../models/all-MiniLM-L6-v2-f16.gguf")
    db = FAISS.load_local(vector_db_path, embedding_model, allow_dangerous_deserialization=True)
    return db

# Bat dau thu nghiem
db = read_vectors_db()
llm = load_llm(model_file)

# Tao Prompt
template = """<|im_start|>system\nSử dụng thông tin sau đây để trả lời câu hỏi.Trả lời một cách ngắn gọn. Nếu bạn không biết câu trả lời, hãy nói không biết, đừng cố tạo ra câu trả lời\n
    {context}<|im_end|>\n<|im_start|>user\n{question}<|im_end|>\n<|im_start|>assistant"""

prompt = create_prompt(template)

llm_chain = create_qa_chain(prompt, llm, db)

# Chay cai chain
question = "Tạo cáp mạng theo chuẩn T568B cần những gì?"
response = llm_chain.invoke({"query": question})
print(response)