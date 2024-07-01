from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from flask import Flask, request, jsonify
from flask_restful import Api, Resource

# Extract data from the website
url = "https://brainlox.com/courses/category/technical"
loader = WebBaseLoader(url)
data = loader.load()

# Split the text into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(data)

# Save the extracted data to a file
with open("course_data.txt", "w", encoding="utf-8") as f:
    for doc in data:
        f.write(doc.page_content + "\n\n")

print("Data extracted and saved to course_data.txt")

# Create embeddings and store in a vector store
embeddings = HuggingFaceEmbeddings()
vectorstore = Chroma.from_documents(texts, embeddings)

print("Embeddings created and stored in Chroma vector store")

# Create a Flask RESTful API
app = Flask(__name__)
api = Api(app)

# Simple custom QA system
def simple_qa(question, vectorstore):
    # Retrieve relevant documents
    docs = vectorstore.similarity_search(question, k=2)
    
    # Combine the content of retrieved documents
    context = " ".join([doc.page_content for doc in docs])
    
    # Simple answer generation (just returning the context for now)
    answer = f"Based on the available information: {context}"
    
    return answer

class ChatbotAPI(Resource):
    def post(self):
        data = request.get_json()
        question = data.get('question')
        
        if not question:
            return jsonify({"error": "No question provided"}), 400
        
        # Get the answer using the simple QA system
        answer = simple_qa(question, vectorstore)
        
        return jsonify({"answer": answer})

api.add_resource(ChatbotAPI, '/chat')

if __name__ == '__main__':
    app.run(debug=True)
