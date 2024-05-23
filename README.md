## Chat with NicK

## Project Overview

This project is a chatbot application built using Streamlit and the Ollama LLM model. The chatbot, named NicK, is designed to interact with users through text and voice input, providing responses powered by the Ollama LLM model. The application features a simple and interactive UI, making it easy to use and engage with.

## Project Structure

- `app.py`: The main Streamlit application file.
- `requirements.txt`: The file listing the Python dependencies required for the project.

## Ollama model installation

```bash
ollama  run vignesh/vicky
```
# or 
check this ```https://ollama.com/vignesh/vicky```
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chat-with-nick.git
   cd chat-with-nick ```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4.Usage
Run the Streamlit application:
```bash
streamlit run app.py
```
Open your web browser and go to http://localhost:8501 to interact with the chatbot.

## Features
- Text Chat: Users can type messages to interact with NicK.
- Voice Input: Users can speak to NicK using their microphone, and the speech will be converted to text for the chatbot to process.
- Streamed Responses: Responses from the Ollama LLM model are streamed in real-time, providing a more interactive experience.

5. Contributing:
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

6. Acknowledgements:
This project was inspired by the need for searching tools for various requirements and the potential benefits of machine learning in public needs.
