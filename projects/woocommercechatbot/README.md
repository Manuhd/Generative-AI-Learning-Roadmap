# WooCommerce AI Chatbot

A **[Python](https://github.com/Manuhd/basic-python) -based AI assistant** for WooCommerce stores. This chatbot fetches product data from your WooCommerce store and answers customer questions using **Google Gemini via [LangChain](https://github.com/Manuhd/Langchain/blob/main/README.md)**. It displays product names, prices, descriptions, images, and clickable links in a **modern chat widget** that can be embedded in WordPress pages via a **Gutenberg block**.

### Live DEMO:
- [http://43.204.11.39:5000/](http://43.204.11.39:5000/)- Backend
- [https://demo-manu-hd.wasmer.app/shop/](https://demo-manu-hd.wasmer.app/shop/) -Frontend (In Progress)

### View flow diagram - 
![alt text](https://github.com/Manuhd/Generative-AI-Learning-Roadmap/blob/main/projects/woocommercechatbot/woochatbot.drawio%20(1).png)
---

## Features

- Conversational AI assistant for WooCommerce products
- Fetches product data including:
  - Name
  - Price
  - Short description
  - Image
  - Product URL
- Returns **HTML-formatted responses** with:
  - Clickable links
  - Product images
  - Clean chat bubbles
- Floating chat widget visible on all pages
- Mobile-friendly and responsive
- Gutenberg block integration for easy embedding
- Powered by **Google Gemini** through **LangChain**

---

## Project Demo-
![alt text](https://github.com/Manuhd/Generative-AI-Learning-Roadmap/blob/main/projects/woocommercechatbot/Demo%20Project.png)

## Project Structure
```
woo-ai-chatbot/
│
├── backend/                       # Python Flask backend
│   ├── app.py                     # Flask app with AI integration
│   ├── requirements.txt           # Python dependencies
│   ├── .env                       # Environment variables (API keys)
│   ├── templates/                 # Optional HTML fallback for testing
│   │   └── index.html
│   └── README.md                  # Backend-specific instructions (optional)
│----------------------------------------------------------------------------
├── frontend/                      # WordPress Gutenberg / JS frontend
│   ├── plugin/woo-chatbot-block/  # React Gutenberg block plugin
│   │   ├── build/                 # Built JS/CSS files
│   │   ├── src/                   # React source code
│   │   ├── package.json
│   │   └── README.md              # Frontend-specific instructions
│   ├── css/                       # Optional custom CSS
│   └── js/                        # Optional custom JS
│
│
└── README.md                      # Main README.md for the full project
```
## Explanation

`backend/`: All Python/Flask code, environment setup, and optional HTML testing. Run this in PyCharm.

`frontend/`: WordPress plugin folder with Gutenberg block (React). Copy this into your WordPress wp-content/plugins/ folder.

`woo-chatbot-block/` → your plugin code.

`src/` → React components.

`build/`→ compiled plugin ready for WordPress.

## Backend Setup (Python + Flask)

Create and activate virtual environment
```
python -m venv .venv
```
#### Windows
```
.venv\Scripts\activate
```
#### Mac/Linux
```
source .venv/bin/activate
```

Install dependencies
```
pip install -r requirements.txt
```

Create .env file in project root:
```
GOOGLE_API_KEY=your_google_gemini_api_key
WP_API_URL=https://yourstore.com/wp-json/wc/v3/products
WC_CONSUMER_KEY=your_consumer_key
WC_CONSUMER_SECRET=your_consumer_secret
```

Run the Flask server
````
python app.py
````
## 2. Frontend Setup (WordPress Gutenberg Block)

Install Node.js and npm if not already installed.

Navigate to frontend folder (where React block is located) and install dependencies:
```
npm install
```

#### Build the block
```
npm run build
```

#### Add the block to WordPress

Copy the block folder to your WordPress plugin directory.

Activate the plugin in WordPress.

You can now add the WooCommerce AI Chatbot block on any page or post via Gutenberg editor.

## Prompt template guiding AI to return HTML
Use a prompt template to guide the AI to return only HTML code. You can train or instruct the AI by providing structured requirements, constraints, and examples, ensuring consistent and safe HTML output for your project.

```
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
```

#### Usage

Type your question about products in the chat input.

#### AI responds with relevant products including:

Name, price, description

Clickable product links

Product images

### Example queries:
```
“Show me the Pen”

“Do you have budget-friendly bags?”

“I want products under $500”
```
![alt text](https://github.com/Manuhd/Generative-AI-Learning-Roadmap/blob/main/projects/woocommercechatbot/woo_chatbot.PNG)

----
## Project Journey

- **Small Test Project:** API integration with Gemini,Local file and WooCommerce  
   -Project -1: [Gemini AI Chat with Python](https://github.com/Manuhd/gen-ai-with-google)  
   -Project -2: [Local AI File Assistant (LangChain + Gemini)](https://github.com/Manuhd/Local-Text-File-AI-Assistant-LangChain-Gemini-OpenAI-)  
  -Project -3: [WooCommerce AI Product Assistant with API](https://github.com/Manuhd/woocomerce-ai-assistance)
- **Final Project:** WooCommerce AI Chatbot

### Challenge: 
- Library Mismatch in LangChain: *[Link](https://github.com/Manuhd/Langchain/blob/main/Library-Mismatch-in-LangChain.md)*

One of the challenges faced while working with LangChain was the library mismatch caused by version fragmentation.

- Unsupported or removed models: *[Link](https://github.com/Manuhd/Langchain/blob/main/Model-name-mismatch.md)*

Unsupported or removed models are AI models that the provider (GemeniAI, OpenAI, Anthropic, etc.) has stopped supporting, updated, renamed, or fully removed from their API.

### Upcoming
- Deploy in [AWS](https://github.com/Manuhd/aws/tree/main) Cloud  -In Progress
- Agentic AI for Autonomous WooCommerce Management – autonomously perform e-commerce tasks  
- AI-Powered Financial Predictor & Trading Agent – using Yahoo Finance API
---
## Read AI topic in simple way:
- What is [LLMs](https://github.com/Manuhd/Generative-AI-Learning-Roadmap/blob/main/LLM.md)?
- What is [Gen AI](https://github.com/Manuhd/Generative-AI-Learning-Roadmap/blob/main/README.md)?
- What is [Agentic AI](https://github.com/Manuhd/Agentic-AI/blob/main/README.md)?
- What is [Langchain](https://github.com/Manuhd/Langchain/blob/main/README.md)?
- What is [LangGraph](https://github.com/Manuhd/LangGraph/blob/main/README.md)?
- What is [LangSmith](https://github.com/Manuhd/LangSmith/blob/main/README.md)?
- What is [RAG](https://github.com/Manuhd/RAG/blob/main/README.md)?
- What is [LLM Evaluation](https://github.com/Manuhd/Generative-AI-Learning-Roadmap/blob/main/LLM-Evaluations.md)?

---
Follow me on LinkedIn: [Manu HD](https://www.linkedin.com/in/manu-hd-a07090158/)


