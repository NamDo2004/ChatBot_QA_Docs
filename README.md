# Chatbot with LangChain
This project develops a chatbot that answers questions based on provided documents using the LangChain framework, leveraging pre-trained models from Hugging Face. The chatbot processes documents and retrieves answers efficiently using vector stores and language models.

## Project Overview
### Objective: Build a document-based Q&A chatbot with LangChain.
### Features:
- Loads and processes documents from the data/ folder.
- Uses vector stores for similarity search.
- Integrates pre-trained models for natural language understanding.
### Steps:
1. Preprocess documents and generate embeddings.
2. Set up a LangChain-based chatbot with a vector store.
3. Implement a query interface using external models.\

## Repository Structure
- **data/**: Contains input documents or datasets (e.g., PDFs, CSV files like nguoimiennuichat.csv).
- **models/**: Stores downloaded pre-trained models (e.g., vinallama-7b-chat-GGUF, all-MiniLM-L6-v2-f16.gguf).
- **src/**: Includes the main source code (e.g., chatbot.py or related modules).
- **vectorstores/**: Holds vectorized data for similarity search.
- **nguoimiennuichat.csv**: Dataset or dialogue data.
- **Picture1.jpg**: chatbot app logo.
- **requirements.txt**: Lists required Python packages.

## Tools Used
- **Language**: Python
- **Framework**: LangChain
- **Libraries**: [To be updated, e.g., langchain, transformers, sentence-transformers, llama-cpp-python—check requirements.txt]
- **Pre-trained Models**:
- vinallama-7b-chat-GGUF by **vilm**
- all-MiniLM-L6-v2-f16.gguf by **caliex**
- Environment: Python 3.9.x with virtual environment (venv)

## Acknowledgments
- This project utilizes pre-trained models graciously provided by the Hugging Face community. Special thanks to:

- **vilm** for the vinallama-7b-chat-GGUF model, available at https://huggingface.co/vilm/vinallama-7b-chat-GGUF.
- **caliex** for the all-MiniLM-L6-v2-f16.gguf model, available at https://huggingface.co/caliex/all-MiniLM-L6-v2-f16.gguf.
### Please respect the terms of use and licensing for these models as outlined by their respective authors.

## How to run
1. Clone the repository:
   - ```git clone https://github.com/your-username/Chatbot_LangChain.git```
2. Set up the virtual environment and install dependencies:
   - ```
      cd Chatbot_LangChain
      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate
      pip install -r requirements.txt
     ```
3. Download pre-trained models
  - Note: Install huggingface-hub (pip install huggingface_hub) if not included in requirements.txt.4
4. Place your documents in the data/ folder.
5. Run the chatbot
  - ```
    cd src
    streamlit run app.py
    ```
## Chatbot app
![Image](https://github.com/user-attachments/assets/d62d81d1-5a5d-4d19-bb4e-392afc8a313c)
