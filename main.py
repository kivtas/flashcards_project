import openai
import os
from dotenv import load_dotenv

from openai_client import generate_flashcards
from wiki_loader import parse

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":

    try:
        # Read the Wikipedia article search term
        user_in = input("Enter term to generate flash cards from: ")
        text = parse(user_in)
        # Generate flashcards
        flashcards = generate_flashcards(text)
        # Print the generated flashcards
        print("\n📚 Generated Flashcards:\n")
        print(flashcards)
    except Exception as e:
        print(f"❌ Error: {e}")
