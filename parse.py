from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3")

template = (
    "You need to extract specific information from the following text: {dom_content}."
    "Please adhere strictly to these guidelines: \n\n"
    "1. **Extract Only Relevant Information:** Retrieve only the details that exactly match the given criteria: {parse_description}. "
    "2. **No Additional Content:** Do not include explanations, comments, or any extra text."
    "3. **Return an Empty String if No Match:** If no relevant information is found, respond with an empty string ('')."
    "4. **Provide Only the Required Data:** Your response should consist solely of the requested information, without any modifications or additional context."
)


def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)
