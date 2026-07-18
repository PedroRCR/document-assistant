# Document Assistant

A Python-based conversational assistant that answers questions about the content of a document , grounding every response strictly in the source material. Built as a hands-on exploration of LLM application development, prompt engineering, and AI agent patterns.

## Setup

1. Clone the repository and enter the project folder:
   ```bash
   git clone https://github.com/pedro-rcrodrigues/doc-assistant.git
   cd doc-assistant
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add your API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```

Usage

The document path is currently set in main.py (documents/cv.pdf by default). Run:

bashpython main.py

Once running, ask questions in the terminal. Type sair, exit, or quit to end the session.

Pedro Rodrigues — [LinkedIn](https://www.linkedin.com/in/pedro-rcrodrigues)
