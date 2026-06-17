# AI Multi-Agent Construction Estimation System

## Project Overview

This project is an AI-powered construction estimation platform that analyzes construction plans and automatically generates cost estimations.

The system allows users to upload PDF construction plans, define pricing for construction tasks, and receive an automated project estimation report.

The project was developed using a Multi-Agent Architecture where each agent is responsible for a specific stage of the estimation process.

---

## Main Features

* Upload construction plans in PDF format
* Extract information from PDF files
* Analyze construction drawings using AI Vision
* Detect construction tasks automatically
* Define custom pricing for construction work
* Generate automated cost estimations
* Produce a final project report

---

## Multi-Agent Architecture

### 1. Input Agent

Responsible for initializing the project workflow and handling user input.

### 2. PDF Agent

Extracts text and information from uploaded PDF files.

### 3. Vision Agent

Converts the PDF plan into an image and analyzes it using an AI Vision model.

### 4. Task Detection Agent

Identifies construction elements and tasks such as:

* Walls
* Rooms
* Kitchens
* Bathrooms
* Doors
* Windows
* Pipelines
* Demolition areas

### 5. Pricing Agent

Applies user-defined prices to detected construction tasks.

### 6. Estimation Agent

Calculates the total project cost and generates the final estimation report.

---

## Technologies Used

* Python
* FastAPI
* LangGraph
* OpenAI / OpenRouter
* PyMuPDF (fitz)
* OCR / PDF Processing
* REST API

---

## API Endpoints

### GET /

System status endpoint.

### POST /set-prices

Allows users to define construction pricing.

Example:

```json
{
  "wall_price": 1000,
  "kitchen_price": 5000,
  "pipeline_price": 200,
  "demolition_price": 800
}
```

### POST /upload-pdf

Uploads a construction plan and generates a project estimation.

### GET /test-graph

Runs the multi-agent workflow for testing purposes.

---

## Workflow

1. User defines pricing
2. User uploads PDF construction plan
3. PDF Agent extracts information
4. Vision Agent analyzes the drawing
5. Task Agent identifies construction tasks
6. Pricing Agent calculates costs
7. Estimation Agent generates final report

---

## Example Output

Detected Tasks:

* 5 Walls
* 1 Kitchen
* 1 Bathroom
* 3 Doors
* 2 Windows
* 15 Feet Pipeline

Estimated Cost:

* Walls Cost
* Kitchen Cost
* Pipeline Cost

Final Total Cost Calculation

---

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Author

Ayelet Nektalov

Final Project – Agentic AI Course
