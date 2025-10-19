import os
import requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
wp_api_url = os.getenv("WP_API_URL")
wc_ck = os.getenv("WC_CONSUMER_KEY")
wc_cs = os.getenv("WC_CONSUMER_SECRET")

# Initialize Flask app
app = Flask(__name__, template_folder="templates")
CORS(app)

# Initialize Gemini model via LangChain
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)

# Fetch WooCommerce products including URL and image
def fetch_products():
    try:
        res = requests.get(wp_api_url, auth=(wc_ck, wc_cs))
        res.raise_for_status()
        products = res.json()
        context = "\n".join([
            f"Product: {p['name']}\nPrice: {p['price']}\nDescription: {p.get('short_description', '')}\nURL: {p['permalink']}\nImage: {p['images'][0]['src'] if p.get('images') else ''}"
            for p in products
        ])
        return context
    except Exception as e:
        print("❌ Error fetching products:", e)
        return ""

# Prompt template guiding AI to return HTML
template = """
You are a friendly shopping assistant for an online WooCommerce store.

Use the following product data to answer customer questions naturally and clearly.

Product Data:
{context}

Guidelines:
- Respond conversationally, like a human chat assistant.
- Mention only relevant products.
- Include product name, price, short description.
- Provide a clickable link using HTML <a href="URL">Product Name</a>.
- Provide the product image using HTML <img src="IMAGE_URL" width="100">.
- Return **only HTML** in the response (do not include markdown or raw symbols like ** or *).
- If the product is not found, politely mention it is unavailable.

User Question:
{question}

Your Response:
"""

# Setup LangChain pipeline
prompt = PromptTemplate(template=template, input_variables=["context", "question"])
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Home page
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_question = data.get("question", "")
    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    context = fetch_products()
    response_html = chain.invoke({"context": context, "question": user_question})

    return jsonify({"response": response_html})

if __name__ == "__main__":
    app.run(debug=True)
