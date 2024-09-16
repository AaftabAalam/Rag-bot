# 💬 Mistral-OpenOrca PDF Chatbot

## Overview
This project is a PDF chatbot application that allows users to interact with the content of uploaded PDF documents using a language model, specifically the Mistral-OpenOrca model, provided through the Ollama platform. The application is built using Streamlit, a popular framework for creating data apps, and uses PyPDF2 to extract text from PDF files. By uploading PDF documents, users can ask questions about the content, and the chatbot will provide relevant responses based on the information extracted from the documents.

## Features
- **PDF Upload:** Upload multiple PDF documents simultaneously for text extraction.
- **Text Extraction:** Extracts text content from the uploaded PDFs using PyPDF2.
- **Natural Language Query:** Allows users to ask natural language questions related to the content of the uploaded PDFs.
- **Contextual Responses:** Uses the Mistral-OpenOrca model from Ollama to generate responses based on the extracted text content.
- **Streaming Responses:** Provides real-time streaming responses to user queries.

## Prerequisites
Before running the application, ensure that you have the following software installed on your local machine:
- **Python 3.9 or later**
- **Docker** (if you prefer running the application in a Docker container)
- **Ollama**: Download and install the Ollama package on your local machine from the [Ollama website](https://ollama.com/).
- **Mistral-OpenOrca Model**: Download the `mistral-openorca` model from the Ollama package repository. Follow the instructions provided on their website to set up and download the model.

## Installation

### Step 1: Clone the Repository
Clone this repository to your local machine.
```bash
git clone https://github.com/AaftabAalam/Rag-bot.git
cd Rag-bot
```

### Step 2: Set Up Ollama
1. Download and install Ollama from the [Ollama website](https://ollama.com/).
2. Start the Ollama service on your local machine:
    ```bash
    ollama start
    ```
3. Download the Mistral-OpenOrca model using the following command:
    ```bash
    ollama pull mistral-openorca
    ```

### Step 3: Install Python Dependencies
Install the required Python packages using `pip`. Ensure you have Python 3.9 or later installed.
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
Run the Streamlit application.
```bash
streamlit run bot.py
```

By default, Streamlit will start a local web server at `http://localhost:8501`. Open this URL in your web browser to interact with the chatbot.

## Usage

1. **Upload PDFs:** On the web interface, use the "Upload PDF documents" button to upload one or more PDF files. The application will process the uploaded files and extract the text content.
   
2. **Ask a Question:** Once the documents are uploaded and processed, enter a question related to the content of the uploaded PDFs into the chat input. For example, "What is the main topic of the document?" 

3. **Receive Responses:** The chatbot will search through the text extracted from the uploaded PDFs and generate a response using the Mistral-OpenOrca model. The response is displayed in the chat interface, providing a relevant answer to the user's query.

4. **Streaming Responses:** The response is streamed in real-time, allowing you to see the answer as it is being generated.

## Docker Setup

If you prefer running the application within a Docker container, follow these steps:

### Step 1: Build the Docker Image
Build the Docker image using the provided Dockerfile.
```bash
docker build -t pdf-chatbot .
```

### Step 2: Run the Docker Container
Run the Docker container.
```bash
docker run -p 8501:8501 pdf-chatbot
```

### Step 3: Access the Application
Open your web browser and go to `http://localhost:8501` to access the application.

**Note:** Ensure that Ollama is running on your local machine and that the Mistral-OpenOrca model is available, even when using Docker. The Docker container connects to the local instance of Ollama to generate responses.

## Project Structure

- **`bot.py`**: The main application file that sets up the Streamlit interface, handles PDF upload and text extraction, and interacts with the Ollama model to generate responses.
- **`requirements.txt`**: Lists all the required Python packages to run the application.
- **`Dockerfile`**: Defines the Docker image for the application, including the installation of dependencies and setup instructions.

## How It Works

1. **PDF Text Extraction**: When a PDF is uploaded, the application uses the PyPDF2 library to extract text content from each page of the document. The extracted text is stored in the session state for later retrieval.
2. **Keyword Search**: When a user asks a question, the application searches through the extracted text from all uploaded documents to find relevant content. It does this by checking if any keywords from the user's query are present in the text of the documents.
3. **Generating Responses**: If relevant documents are found, the extracted text is passed as context to the Mistral-OpenOrca model using the Ollama platform. The model then generates a response based on the given context and the user's query.
4. **Streaming Response**: The response is streamed to the user in real-time using Streamlit's `write_stream` functionality, providing an interactive chat experience.

## Troubleshooting

- **Error Extracting Text from PDF**: Ensure that the PDF is not password-protected or corrupted. The PyPDF2 library may have limitations with certain PDF formats.
- **Ollama Not Running**: If you encounter errors related to Ollama, ensure that the Ollama service is running on your local machine (`ollama start`) and that the Mistral-OpenOrca model is properly downloaded.
- **Docker Issues**: If running in Docker, ensure that the Docker container can communicate with the local Ollama service. The Ollama service must be started on the host machine.

## Limitations
- **Response Quality**: The quality of responses depends on the context extracted from the PDFs and the capabilities of the Mistral-OpenOrca model.
- **Local Ollama Dependency**: The application relies on Ollama being set up and running on the local machine.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to suggest improvements or report bugs.

## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **Ollama** for providing the Mistral-OpenOrca model.
- **Streamlit** for providing an easy-to-use framework for building interactive data applications.
- **PyPDF2** for PDF text extraction capabilities.
