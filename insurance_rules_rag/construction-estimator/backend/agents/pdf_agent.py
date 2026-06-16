import fitz

from graph.state import ConstructionState

def pdf_agent(state: ConstructionState):
    print("PDF Agent Running")

    pdf_path = state.get("pdf_path")

    if not pdf_path:
        return state

    text = ""

    try:
        doc = fitz.open(pdf_path)

        for page in doc:
            text += page.get_text()

        doc.close()

        state["pdf_text"] = text
        print("PDF TEXT:")
        print(text[:2000])

    except Exception as e:
        state["pdf_text"] = f"Error reading PDF: {str(e)}"

    return state