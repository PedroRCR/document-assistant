import os
from dotenv import load_dotenv
from openai import OpenAI
from pdf_reader import extract_text_from_pdf

load_dotenv()

API_KEY = os.getenv("API_KEY")
MODEL="tencent/hy3:free"


def get_client() -> OpenAI:

    if not API_KEY:
        raise EnvironmentError(
            "API_KEY not found. "
        )
    return OpenAI(
        api_key=API_KEY,
        base_url="https://openrouter.ai/api/v1",
        timeout=30.0,
    )
    
def create_initial_prompt(document_text: str):
    return f"""You have access to the following document and must answer questions about it.
            --- START OF DOCUMENT ---
            {document_text}
            --- END OF DOCUMENT ---

            Always answer based ONLY on the information present in the document above.
            If the answer is not in the document, clearly state "I cannot find this information in the document". Do not make things up or use external knowledge.
            """
    

def initialize_chat(client: OpenAI, document_as_text: str):
    messages = [
        {"role": "system", "content": create_initial_prompt(document_as_text)}
    ]
    
    print("Welcome! Do the questions you want.")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ("sair", "exit", "quit"):
            print("See you soon!")
            break
        
        print("\nAssistant: ", end="")
        
        messages.append({"role": "user", "content": user_input})
        
        response = client.responses.create(
            model = MODEL,
            input = messages
        )

        print(response.output_text)
        
        messages.append({"role": "assistant", "content": response.context_text})
    

def main():
    client = get_client()
    document_as_text = extract_text_from_pdf("documents/cv.pdf")
    initialize_chat(client, document_as_text)
        
if __name__ == "__main__":
    main()