import openai

# Create flashcards using the OpenAI API
def generate_flashcards(text, model="gpt-3.5-turbo"):
    prompt = (
        "Based on the following text, generate 10 flashcards. "
        "Each flashcard should be in the format:\n\n"
        "Q: [question]\nA: [answer]\n\n"
        "Text:\n" + text
    )

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an educational tutor helping students study."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )

    return response['choices'][0]['message']['content']