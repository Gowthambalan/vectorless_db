def build_prompt(context, question):
    context_text = "\n".join([item["content"] for item in context])

    prompt = f"""
You are an AI assistant.

Answer the question ONLY using the context below.

Context:
{context_text}

Question:
{question}

Answer:
"""
    return prompt