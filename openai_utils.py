import openai

def answer_question_with_chat_gpt(question, context, openai_api_key, model="gpt-3.5-turbo"):
    """
    Sends question + context to OpenAI ChatCompletion and returns the answer.

    Args:
        question (str): User's query.
        context (str): Relevant text from the PDF (retrieved chunks).
        openai_api_key (str): Your OpenAI API key.
        model (str): Chat model (e.g., gpt-3.5-turbo or gpt-4).

    Returns:
        (str): The answer from GPT.
    """
    openai.api_key = openai_api_key

    # System message to guide the assistant
    system_message = {
        "role": "system",
        "content": (
            "You are a helpful assistant. Use the following text to answer the question accurately. "
            "If you are unsure or the answer doesn't appear in the text, say: 'I'm not sure based on the document.'"
        )
    }

    # User message includes both context and question
    user_message = {
        "role": "user",
        "content": f"Context:\n{context}\n\nQuestion: {question}"
    }

    response = openai.ChatCompletion.create(
        model=model,
        messages=[system_message, user_message],
        max_tokens=300,
        temperature=0.0
    )

    answer = response["choices"][0]["message"]["content"].strip()
    return answer
