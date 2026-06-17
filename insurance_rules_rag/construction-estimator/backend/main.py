from fastapi import FastAPI, UploadFile, File
import shutil

from graph.orchestrator import create_graph

app = FastAPI(
    title="Construction Estimation System",
    version="1.0.0"
)
user_prices = {
    "wall_price": 500,
    "kitchen_price": 3000,
    "pipeline_price": 100,
    "demolition_price": 300
}
graph = create_graph()


@app.get("/")
def root():
    return {
        "message": "Construction Estimation System is running"
    }


@app.get("/test-graph")
def test_graph():

    result = graph.invoke(
        {
            "prices": {},
            "pdf_path": "",
            "pdf_text": "",
            "detected_tasks": {},
            "cost_breakdown": {},
            "final_report": ""
        }
    )

    return result
@app.post("/set-prices")
def set_prices(prices: dict):

    global user_prices

    user_prices = prices

    return {
        "message": "Prices updated successfully",
        "prices": user_prices
    }

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = graph.invoke(
        {
            "prices": user_prices,
            "pdf_path": file_path,
            "pdf_text": "",
            "detected_tasks": {},
            "cost_breakdown": {},
            "final_report": ""
        }
    )

    return result