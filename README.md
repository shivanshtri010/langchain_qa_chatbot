# Simple QA System with Flask and LangChain

This project demonstrates a simple question-answering (QA) system using Flask and LangChain. It extracts data from a specified website, processes the data, and provides a RESTful API to answer questions based on the extracted information.

## Steps

1. **Extract Data from the Website**
    - Use `WebBaseLoader` to load data from the specified URL.
    - Save the extracted data to a text file.

2. **Create Embeddings and Store in a Vector Store**
    - Split the extracted text into chunks using `CharacterTextSplitter`.
    - Create embeddings using `HuggingFaceEmbeddings`.
    - Store the embeddings in a Chroma vector store.

3. **Create a Flask RESTful API**
    - Set up a Flask application with Flask-RESTful.
    - Implement a simple custom QA system to handle questions.
    - Create a RESTful API endpoint to receive questions and return answers.

## Requirements

- Flask
- Flask-RESTful
- langchain_community
- chromadb

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/shivanshtri010/langchain_qa_chatbot.git
    cd langchain_qa_chatbot
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the application:
    ```sh
    python app.py
    ```

## Usage

Send a POST request to the `/chat` endpoint with a JSON body containing the `question` key:
```json
{
    "question": "What technical courses are available?"
}
