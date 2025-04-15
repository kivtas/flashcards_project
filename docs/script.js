async function generateFlashcards() {
  const term = document.getElementById("term").value;
  const responseDiv = document.getElementById("flashcards");

  try {
    console.log("Sending API request with term:", term);

    const response = await fetch(`https://flashcards-backend-w2oi.onrender.com/generate_flashcards?term=${encodeURIComponent(term)}`);
    console.log("Response status:", response.status);

    if (!response.ok) {
      throw new Error("Failed to fetch flashcards.");
    }

    const data = await response.json();
    console.log("Response data:", data); // Log entire data object

    if (Array.isArray(data.flashcards)) {
      responseDiv.innerHTML = data.flashcards.map(flashcard => {
        return `<div class="flashcard"><strong>Q: ${flashcard.question}</strong><br>A: ${flashcard.answer}</div>`;
      }).join('');
    } else {
      throw new Error("Received flashcards are not in the expected format.");
    }
  } catch (error) {
    console.error("Error:", error);
    responseDiv.innerHTML = `<p>Error: ${error.message}</p>`;
  }
}
