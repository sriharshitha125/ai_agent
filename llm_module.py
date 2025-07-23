import google.generativeai as genai


genai.configure(api_key="AIzaSyCnOxAjdD1SM8_1kAA7mJBjjsn-EpqeNAA")
model = genai.GenerativeModel('gemini-pro')

def generate_sql(question):
    prompt = f"Convert this question to an SQL query for a SQLite DB:\nQuestion: {question}"
    response = model.generate_content(prompt)
    return response.text.strip()

def format_answer(result):
    if not result:
        return "No data found."
    if len(result[0]) == 1:
        return f"Answer: {result[0][0]}"
    return f"Answer: {result}"

def generate_sql_from_question(question: str) -> str:
    q = question.lower()
    
    if "total sales" in q:
        return "SELECT SUM(total_sales) AS total_sales FROM total_sales;"
    
    elif "return on ad spend" in q or "roas" in q:
        return """
        SELECT item_id, 
               SUM(ad_sales) / NULLIF(SUM(ad_spend), 0) AS roas
        FROM ad_sales
        GROUP BY item_id
        ORDER BY roas DESC;
        """
    
    elif "highest cpc" in q or "cost per click" in q:
        return """
        SELECT item_id, 
               ad_spend / NULLIF(clicks, 0) AS cpc
        FROM ad_sales
        ORDER BY cpc DESC
        LIMIT 1;
        """
    
    else:
        raise ValueError("Unsupported question. Try asking about total sales, ROAS, or CPC.")


