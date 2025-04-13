import openai
import os
from dotenv import load_dotenv

from openai_client import generate_flashcards
from file_loader import load_article

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    article_path = "test.txt"  # Make sure this file exists in your project directory

    try:
        # Read the Wikipedia article from the file
        text = load_article(article_path)
        # Generate flashcards
        flashcards = generate_flashcards(text)
        # Print the generated flashcards
        print("\n📚 Generated Flashcards:\n")
        print(flashcards)
    except Exception as e:
        print(f"❌ Error: {e}")
