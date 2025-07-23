# 🧠 Ecommerce AI Agent

This project uses FastAPI and Gemini LLM to answer natural language questions about e-commerce sales data.
## Step tp Follow

1. Open Command Promt
2. Copy the path to thr folder and paste and click enter.

```bash
cd "PATH to the folder"
```
   
3. Now you are in you project Folder.

## How to create virtual environment

```bash
python -m venv venv
```

## Load Virtual Environment

```bash
venv\Scripts\activate
```


## 🛠 Setup

```bash
pip install -r requirements.txt
```

## 📂 Load Datasets

```bash
python load_data.py
```

<img width="904" height="132" alt="image" src="https://github.com/user-attachments/assets/fa1681d5-268d-4d57-bad6-660715c36fed" />



## 🔧 Running the App

```bash
uvicorn main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) to try the API.

## How to give the query

- click on post/ ask
- click on Try it out
- under request body give your question.

## 🧪 Sample Questions
- total sales?
- ROAS.
- highest cpc

## 📂 Datasets
Make sure the following datasets are in a SQLite database `ecommerce.db`:
- `ad_sales.csv`
- `total_sales.csv`
- `eligibility.csv`
---

You're now ready to build and test your GenAI e-commerce agent! 🎯
