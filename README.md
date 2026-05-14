## Chat with NicK

A chatbot built with [Streamlit](https://streamlit.io/) and [Ollama](https://ollama.com/) using the `vignesh/vicky` model for real-time AI conversations.

### Setup

```bash
git clone https://github.com/your-username/chat-with-nick.git
cd chat-with-nick

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

### Install Ollama Model

```bash
ollama run vignesh/vicky
```

Model: https://ollama.com/vignesh/vicky

### Run

```bash
streamlit run app.py
```

Open in browser:

```text
http://localhost:8501
```

### Features

- Real-time AI chat
- Streamed responses
- Simple Streamlit UI
- Ollama local model integration

### Contributing

Pull requests and improvements are welcome.
