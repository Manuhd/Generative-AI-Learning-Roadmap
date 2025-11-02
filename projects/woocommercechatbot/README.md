# WooCommerce AI Chatbot

A **[Python](https://github.com/Manuhd/basic-python) -based AI assistant** for WooCommerce stores. This chatbot fetches product data from your WooCommerce store and answers customer questions using **Google Gemini via [LangChain](https://github.com/Manuhd/Langchain/blob/main/README.md)**. It displays product names, prices, descriptions, images, and clickable links in a **modern chat widget** that can be embedded in WordPress pages via a **Gutenberg block**.

### Live DEMO:
- [http://43.204.11.39:5000/](http://43.204.11.39:5000/)- Backend
- [https://demo-manu-hd.wasmer.app/shop/](https://demo-manu-hd.wasmer.app/shop/) -Frontend (In Progress)

### View flow diagram - [link](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=woochatbot.drawio&dark=auto#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Page-1%22%20id%3D%220UkqQFFutkzzMXLk0LOX%22%3E7Vxdc%2BI2F%2F4tvWBmcwHjb%2BCSj5DNNNnNJu2kfW86whbgjbFdWQTor3%2BPLNvYkgCTNdk0DYRgH1uydJ6j8yWJljlabq4Iihe3kYeDlqF5m5Y5bhlGr2vAf0bYcoJl9jlhTnyPk%2FQd4cH%2FB2dELaOufA8nlRtpFAXUj6tENwpD7NIKDRESrau3zaKg%2BtQYzbFEeHBRIFMffY8usm4Z3R39M%2Fbni%2FzJupP1b4nym7OeJAvkResSybxsmSMSRZQfLTcjHDDe5Xzh5SZ7rhYNIzikdQr82fs9%2FK195T153rf7q3F7%2BP3pf22T1%2FKMglXW4d8TTLIG023OheQJU5d1R2uZw2hFAz%2FEo4LjjDiLQjqKgoikBUx4T1gzhnOCPB%2FvroVRCHUOE0qiJ6wqMPODoESfpS%2BgeyhZYC972jMm1AeQbtAUB3dR4lM%2FCuHaNKI0WpZuGAT%2BnF2gUQxUlJ250CDopTlc0GUA53rWgUz8dCM%2FzzjAHomSmPd25m9YO4aAZ8wuLjdzJvkdtE6sDsFJtCIuvnZZe4Zwyo%2Bqd62S9OkyghmorPV4UyJliF7haIkp2cIt2VVD0zo2L5QPMFvrWBms653EOpkULkrCmtNQNkbmRfU7MYKDTJJOkCpbkipJoki0Cr0Cz%2FXCp%2FghRi67ugZGVbEhEUUZwn1NkJGA9aftIfL0CcQFe7MZhsdDu6Fzpo7Y%2B0IlcE76kiWXv5pBx%2BppFWwALhU2pq4Ap9CAjaPjSOh8hlIR06wLTPAvnHuPmDUIPbMvBJ8hmrOjZ%2BQH0wCnqhT0hGZr2gFs9ePYNsBm3aiy2cpZV%2BKxril4bJ%2BLxT2JxS4KWQOjFWPVaj7HCYWjafaV8pYxjbEUmirzNNc2oNMCUMDH%2BRpj4kNnmKLJC93tSMM4U5pGNgITrvpMrXSNXeqwuqYoSfWi1pDSsnrH8TJfU2H1jyssHHoD5k8wdgYoSXxX1FFlhcbVTe4xGIf4hr2KByJzrcQV%2B4AQExyAknyu%2Bi0qTmVPuIv8kJYGUVfQVeLg4IYtK1X2M4SKbPNIRRSROaZSRcBdtC3dFrMbkv0NNg31c3ZywGvcSUXB05cLSi6pJUmZ3AwefgXS5H5we%2Fn49f7XH7N1sv9juK7KgHnO1LGdZkak7VSdCENTjEhLKXyFQWt8UOq6xOubwZer0efB9ZdGeewh3Jspeey4PTydnYfHpqZ0Bvaw%2BVw8NmQe39wm7ZbhoCXjWjhN4rT%2FTsCMzhQMlDNnR1%2FvLr8MrlM3a3J1eXv9hR0P7q4bRQbrno27KmT6TtdEZ5J%2B600gYx23SSex1vMJBDDcrIMuZ72SlE1%2F1uWxjchu0zH7pteQu%2BYIilupbHSZ13r%2FbMw%2BKWKp4dWKjLXZ%2B2eFIXpXrzLcYfKt7V6OzH%2B9%2F8rKXo5KJAQqKQBlFqKEgBTrB0KuoLjwwmSCGP%2Bv8TSI5lHSWUfEiyHyT2Q50LRBdzyQ5CBNijTgV%2BtiMsBw7E6u3EroqhSZdbax1T2ObCW%2FlDl%2BcMEewh%2B0a8Q%2F9piFpkDpGLaCqKJ1ZaIu3wZfuuoJIlFF68pEXb6NneWtrhJVtK4tt1gsrStK60Jp%2BPtgZ8PsPCn7uT9RhfTZzDKKRNVs1tO9vjJR9S4zoO4C0SnLfEsJ4iqbbDTzLKtgE%2FbY%2B6KhNISkLk1T9kTyXEVFV%2FbOpSvlxNEjWJO71Jqkrjb8v8fIZXHwhABAOPSY3x3HAYCdyoCoW4EbtAq0yndRGKSq%2BGYkSYBEOVv6nsceLSREmnBjTDsdjCXACley7Lr0%2BjmsZcxM%2B1yYycmjuy1dMCS0IXKfUoTeKyZ2TwDEUgCiSr2a53I38qxQc7k84A7Z%2FsEudTRdzwl%2FsqsdE9DPCONN%2Bf7xtnxWyrwe5jzPjdUIC99I1tAQZjgscdaibtbQ1KoVmWKstydr2FRirxD95sRm49OK1MA5FxrHNrLzncywk23ppLbEcAb%2FiyRGANrSXigxRTZgn%2BidW2JkW%2F1thZP3bYPNrlVherG64chU8%2FnUvWx973ESR2GC%2FzsomHkVPwsFUza67x8F2xaiB6f2yovzASGbsRGLEjb0%2FeLgWGLS6w3gYHzg8MrjYbQlxGvTxF09Ps3DyfyPb0%2BPbYVX14W%2BTtZx%2B3vCDPVk7cK%2FZ2jmJCaRt3JZqmzS6o7fNE4SKAro9lsPq%2Bo4FZ5dOWZTeYBnQ0me6lpQCtwcpAmPiW50O1onXYoysNPFMROWP3rHCIn2XZHmeNVhlI%2Fsgzn8LBs4C%2FAmC5OGyogpAcecnhBI5Z1Ok5Jp4SxLaXWcLn9IldBSxTu1%2BH8sa1EQfzAIckyrY5tVjDV5dq1uKJRWVx3TVl%2Bqrbl4SC0jNWbwPmTkh2TE0vQGZcRUzOeeW0ZUC%2B34yhLPf86XlhwgTXMCX6autS6NVs9p9VmlpUz5pJQbL98yAUl6Emg3KJyPFsgPBfoVXvqhnz8Y6pyKjQHaia2Wl9VoH6SfRcqwNj8gfkukfNhpcxxigihmE18oTNZsvH8A9U5JH2Pxp5NUtnGPGeXG91Sk6uNHjhUV3MofWpp3fIG1uEQhLeX102V7iLiZYwkRcyPBn96rBn92PsVWXpSgWsGlN7FjSOm22fI2QQmDl02OaR2732%2FtJsfyibI9E2P5TKzW6RmVmdi21tF2lFOmYuWdGvun346HCzXm4zInvOZM78%2BaphOTRKa4PrD2xK4wTWecb2JXLbunLj9sYnuroGNGfcNORVuZe3pz67rSFYOYXD5jvnAwbblyrZeX%2FLXcJn8Hf%2FkhBN0hk%2FsmVCCoMjGfoTmdHLjyzknF4iyzgcVZakmSJ3xz%2B7QwDvkgKYFxHQrPUKYcnL9X6fo36D2Z%2B2hHyAs%2BbBOKl1BkQFxm0Vy6Imzf5dhHAMHyoLHkD5PI%2Bxq1Gwp5I9iFNt8TOIAb%2BvGGlxLaKPoQuxCceQsaOHTcq8jPdrF2Tinc%2FXxFIMgJib5DbztH%2BvPjHH4Bw4BWxrpBP8TRUF9XbnUxxl1HUyihYmFoEyNO2P2nWMZlnmtHpnKwOSqX4zSh7e0T2pHRGvThBnjbuWerpcGHdotCtkP383ivbKjnHOpOKqjVsmEJallXKPpiukHS9Q3gL87d2bp6C5Qq4dnEzgG1DMjzQqVknWjD1%2F4yQCmTjwy8cno4ddrFiAB5fU%2B5WQdhSzeZCU33krDFnfN0yAsg86ugCjERruxFyo2CAMUJ3v%2FjHse2sAnu2p4tbIc8xgPO4T3oY%2BB8uu%2F%2FtCcWiqXy2wbiRBUKQJJDRPGQsTM5hx%2FoqKaw%2BBiPgewhitrxsp0EvmA%2BgPEa%2B6TbJ8ZldaJQQS7Hm6mf0kJ2Mp9%2B0vgi9vzrgn%2BzK4ad%2FWBF%2BeCCL3LXPD%2BJA7aLmVXph8wzhYNf%2FGUcEYCE1jLLdXMCCo9CUahqfScYMceEZemiWSv9DYlWNal%2B408JSoX1Om01CPkBC6v0Z2KRFr8K9w84DFKLokCkBH5OuSPRMmZ72bVP%2FPA3vARUKb442OtdBXKVbJcuq6%2Fwn56Zh7Pj%2B0XNem7xMkqx%2BQQBDyimJN1EMFzNZpjwa3VrSh%2BbtgnalmPfhs%2BIpwPq1vN1ReMVM%2FB3iCTQIFbjAyWczGm1O5f9GtUj2IA4qwpaRq%2BiCHTZFU8wQ4w8uD5cIxBleCUJqErFq6xNCPCMHnIVqkmX%2FXZpjz2r7sWZTMYs52WMKEFhwm3TbivOEffjgIGXjVoR9NU0J%2BIS4hoeCJzufnqL25jd75eZl%2F8H%3C%2Fdiagram%3E%3C%2Fmxfile%3E)
![alt text](https://github.com/Manuhd/Generative-AI-Learning-Roadmap/blob/main/projects/woocommercechatbot/frontend/woochatbot.archetecture%20diagram.png)
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


