from typing import TypedDict, Dict, Any


class ConstructionState(TypedDict):
    prices: Dict[str, Any]

    pdf_text: str
    pdf_path: str

    detected_tasks: Dict[str, Any]

    cost_breakdown: Dict[str, Any]

    final_report: str