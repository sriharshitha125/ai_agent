# 🧠 Ecommerce AI Agent

This project uses FastAPI and Gemini LLM to answer natural language questions about e-commerce sales data.

## 🛠 Setup

```bash
pip install -r requirements.txt
```

## 🔧 Running the App

```bash
uvicorn main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) to try the API.

## 🧪 Sample Questions
- What is my total sales?
- Calculate the Return on Ad Spend.
- Which product had the highest CPC?

## 📊 Visualization Endpoint

```bash
GET /plot/highest_cpc
```

## 📂 Datasets
Make sure the following datasets are in a SQLite database `ecommerce.db`:
- `ad_sales.csv`
- `total_sales.csv`
- `eligibility.csv`

Use this to load them:
```python
import pandas as pd
import sqlite3

conn = sqlite3.connect("ecommerce.db")

pd.read_csv("ad_sales.csv").to_sql("ad_sales", conn, if_exists="replace", index=False)
pd.read_csv("total_sales.csv").to_sql("total_sales", conn, if_exists="replace", index=False)
pd.read_csv("eligibility.csv").to_sql("eligibility", conn, if_exists="replace", index=False)

conn.close()
```

---

You're now ready to build and test your GenAI e-commerce agent! 🎯
