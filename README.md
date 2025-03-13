# CSV Analyzer & Visualization Tool

## 📌 Overview
This is a **CSV Analyzer & Visualization Tool** built using **Gradio**, **Pandas**, **Matplotlib**, and **Pydantic-AI** powered by **Ollama**. The tool helps in:
- Uploading and validating CSV files.
- Generating different types of graphs (Bar, Line, Scatter) from CSV data.
- Answering questions about the uploaded CSV using AI.

## 🚀 Features
- 📂 **CSV File Upload & Validation** – Checks for missing values, displays column types, and gives a preview.
- 📊 **Graph Generator** – Allows users to create **Bar, Line, or Scatter plots** for easy visualization.
- 🧠 **AI-Powered Query System** – Users can ask questions and get responses based on CSV data using **Ollama LLM**.
- 🎨 **Dark-Themed UI** – Styled for a modern and clean look.

## 🛠 Problem-Solving Approach
- **CSV Handling** – Validates uploaded files and ensures clean data processing.
- **Data Visualization** – Provides an easy way to analyze trends in data through charts.
- **AI Query System** – Uses an **Ollama-powered LLM** to answer user questions about the uploaded CSV.
- **Error Handling** – Catches and displays errors in a user-friendly manner.

## 🎓 Learnability
- The project is structured with clear function definitions and separate concerns.
- Uses **Pydantic-AI** to structure AI responses cleanly.
- Built with **Gradio**, making the interface intuitive and easy to use.

## ✨ Code Quality & Modularity
- **Modular Functions** – Separate functions handle file upload, plotting, and queries.
- **Global Variables** – Used only where necessary to maintain performance.
- **Clean Code** – Follows best practices for readability and maintainability.

## 🔍 Error Handling
- **File Validation** – Ensures proper file format and non-empty data.
- **Graph Generation Errors** – Prevents errors from invalid column names or missing data.
- **AI Query Handling** – Ensures meaningful responses, even for unclear questions.

## 🎯 User Experience
- **Minimal Inputs Needed** – Simple, easy-to-use interface.
- **Helpful Error Messages** – Provides useful feedback for troubleshooting.
- **Dark-Themed UI** – A visually appealing interface for better readability.

## 🔧 Installation & Usage
### Prerequisites
- Python 3.8+
- Install dependencies:
  ```bash
  pip install gradio pandas matplotlib pydantic-ai
  ```
- Start the application:
  ```bash
  python app.py
  ```


