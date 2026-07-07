from services.llm_service import model

def generate_summary(text):

    prompt = f"""
    You are an expert study assistant.

Analyze the following study material.

Generate a structured summary.

Rules:

1. Divide the summary into major topics.
2. Use clear headings and explain it.
3. Under each heading provide concise bullet points.
4. Highlight important definitions.
5. Mention formulas if present.
6. Mention important facts.
7. Keep each bullet short.
8. Use Markdown formatting.

    Document:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text