# WooCommerce AI Chatbot

A **Python-based AI assistant** for WooCommerce stores. This chatbot fetches product data from your WooCommerce store and answers customer questions using **Google Gemini via LangChain**. It displays product names, prices, descriptions, images, and clickable links in a **modern chat widget** that can be embedded in WordPress pages via a **Gutenberg block**.

### View flow diagram - [link](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=woochatbot.drawio&dark=auto#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Page-1%22%20id%3D%220UkqQFFutkzzMXLk0LOX%22%3E7Vpbc9o4FP4t%2B8DM9iEey3c%2FArk00ySlyXbS7puwBHhjLMYWAfrrV8KysSWFS2poJi2EYB1dLH3n0zk6x3Ts%2FnR5lcHZ5JYgnHQsEy079nnHsgLfYv%2B5YFUIHDssBOMsRoUIbAQP8Q8shKaQzmOE80ZDSkhC41lTGJE0xRFtyGCWkUWz2YgkzbvO4BgrgocIJqr0MUZ0IpZl%2BRv5RxyPJ%2BWdgSfWN4VlY7GSfAIRWdRE9kXH7meE0OJquuzjhGNX4lL0u3yhtppYhlO6T4fvwdf0n7Mr9ITQl%2Fur87Pef0%2F%2FntnFKM8wmYsFf81xJiZMVyUK%2BROmEV%2BO2bF7ZE6TOMX9CnEuHJGU9klCsnUHm70v%2BTR64wyiGG%2FqUpKyMXs5zcgT1nUYxUlSk4%2FWLyZHMJ9gJO72jDMaMyXdwCFOBiSPaUxSVjcklJJprUE3ice8gpIZk0JRitiE2Crt3oROE1YGYgGCfsAqywIBfkuYz4rVjuIln0eP6XPGK6fLMWe%2BARe5Y2Q4J%2FMswtcRn0%2BPFYurZqt5vr67qkGhVD57vKyJhEavMJlimq1YE1Fr2U7RRWwv2xdsW2zI6gnRpMbTUgbF9hhXI28YxC4EiQ4glKsQSiFTRuYpqlS5mMQUP8xgxGsXDKOmWjJCoVBuaLaDmWu6DcyAo2JmAw1olVFqHTVPQe0j60W4sZvgDP%2FVsdi45iPmE4LP%2FAuyTw%2BO%2BdUzjJNhgtfWjW1d0zXNLZiD3Zi3gDEoCVby0lIxBqYGY%2FdYEAcKxBFM%2BQTJnEM1H49xTtnVUHytseWgcUjZVFVMSwPAzEzCbOJuXGc4i9li%2BN4vOw02ot5M2DFL7Iy8sEa2WavjVQYfawjztalqaU9YgbNbX%2FYpDUm425DgFHW5i%2BdwJjDP40i2HXVDU7ic0olb23DDqHEoUFGroeJuIXGGE2a8nptHCR1S4g4DEqe0phTQ3ESVoSqHKHyN6FV3%2FdJAbrBjIAqzMabKQAxduKo1m%2FEG%2BcsTtj39fTY8KEbcsKLC9PVEKUGqMeXypvvwiYku77u3F4%2Bf7z%2F9nA9SjyRWFOkOMcgbeq7XkpcKJSxBaLi%2BuikdLf8Mxz7SvgRAgfume3fV%2F9i9vmsVZgRxMNLC7EUBHo6OA7OlM3x6jI8FsKUA%2FHlwcde9ZrKri9vrO37RHVy3C7aLA%2BTowA6soe0didNaL3NasJ3dbuYgXFGcsTCh8NTMPPNVKfYjHPlFBCFjbXt2aKOWPLrZxDrUQQ1UqEF4NKwPig32OKfKuLr8rTUY65capRavlvAuDWNlrx3DdlXMQXhie63GFgrqjdhaG97XUFeC6EQKwquKV0bpcmC9wMOEjEluLEiGZiykzlXdm2bXP%2B8qul9nG1rQreNIutX6Yp3lkk9a7enV363XRtpGHN5Yhdtjf2xe%2FeLjnvPwkkkMy9UIdTJfFQK1GfsCujvIQp3MV4VAbcZL5aybQp3Md9UZy72BpjeQerO%2FP3C2DOdBScX65k%2F4XjtDMHv6mzWBYDRyrCJdsj6qBwCFH3Q%2B4V0mFqMJpEOeUFbyrk2YXDhC3KYJmDDi7w8tOUKnefCoHGPdUgYaSxkcy1KqqZ9H5kkGa0%2FC13%2FJ%2Ft9jGPFI9jJj6sEpUmwpWz1tKlZ3OtG4nyZdhUghjMyraYwQv7WUxGhBP0A6hLuaQ4ouZWwfzZOpqZ7Bik4Iz871YPT0rrXhSTkeV3NM1%2BVJj6aNMiRrL%2FHGwMlW33iVYQKvFHznteyE7JaC82W9%2FfmqXqqlSQvhMqbfigFCS5T5gGemYXq%2BEGwG5IVVrSAP96IeC5u7BS1hWor82TaOiwPkG8ks2pKNrgLxQzOL8kBWIA30QmaxreRfteHaZys%2FttS5uoungpKc5KBGSdPwXOuEjCyZtpOS3ptipHJqkNMQ%2BzKySuCV1DZPzMg9MkoHMrI0dg1WuVs5dcDDjt2MeltPRVzLazJFfgS1t%2B1yJco57mmZskdmpowFRgleCsr0DmNPqZTC8Za%2FsLGN7XmvN6JrT36g5L9S154bGs2n%2Fspsjq3tffI1%2B2o7Z5OlryCBX%2FataBCGEi%2FWglZ4oT23VsKfZYai0FefYWSSWTLJjs0MNT79Msf5OvPwbuMex5Z2NlADn5NGoZYahd7jfEbSHP8%2BWrB%2BtRbKgX8rLcg%2Fz6iCqF%2BmBTWq6vO02JK%2BXyV4vmSQfrkSrD9KOOJOYMXNb68LV775Abt98T8%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E)
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

'woo-chatbot-block/' → your plugin code.

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

