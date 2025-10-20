# WooCommerce AI Chatbot

A **Python-based AI assistant** for WooCommerce stores. This chatbot fetches product data from your WooCommerce store and answers customer questions using **Google Gemini via LangChain**. It displays product names, prices, descriptions, images, and clickable links in a **modern chat widget** that can be embedded in WordPress pages via a **Gutenberg block**.

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

