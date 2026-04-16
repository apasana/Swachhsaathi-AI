# SwachhSaathi AI – Smart Waste Management System

SwachhSaathi AI is an intelligent, AI-driven platform designed to improve urban waste management. It connects citizens, waste collectors, and municipal authorities through AI-powered analysis.

## Features
- **Complaint Analyzer**: NLP-based classification of complaints (Missed Pickup, Overflow, General) with priority assignment.
- **Waste Classification**: Computer Vision for classifying waste types (Organic, Recyclable, Hazardous).
- **Smart Decision System**: Logic-based alerts and priority decisions.
- **Flask Backend**: REST API for handling requests.

## Technology Stack
- Python
- Flask
- NLTK/spaCy (NLP)
- OpenCV (Computer Vision)
- scikit-learn

## Installation
1. Clone the repo.
2. Install dependencies: `pip install -r requirement.txt`
3. Run the app: `python backend/app.py`

## Usage
- Submit complaint via POST to `/submit_complaint` with JSON: `{"text": "complaint text", "image_path": "path/to/image.jpg"}`

## Project Structure
- `backend/`: Flask API
- `ai/`: AI modules (NLP, CV, Decision)
- `utils/`: Helpers and config
- `dataset/`: Sample data
