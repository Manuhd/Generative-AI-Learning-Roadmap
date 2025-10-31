
# What is FastAPI? (Simple Explanation)

FastAPI is a modern Python web framework used to build APIs quickly, with:

- ✅ High performance (faster than Flask & Django for APIs)
- ✅ Easy syntax
- ✅ Auto-generated documentation
- ✅ Async support

It is the most popular framework for AI, ML, and microservices.

## ✅ Why FastAPI is used?

Because it provides:

⚡ High speed (built on ASGI + Starlette + Pydantic)

✅ Automatic Swagger Docs

✅ Built-in validation

✅ Async support

✅ Production-ready

✅ Easy to deploy on AWS, Docker, etc.

##  FastAPI Features (Very Important)
### ✅ 1. Automatic API docs

Open your browser at:

/docs  → Swagger UI
/redoc → ReDoc

### ✅ 2. Data validation with Pydantic

FastAPI automatically checks request data (type, format, missing fields).

### ✅ 3. Async support

Perfect for AI + API + external calls.

### ✅ 4. Dependency injection

Easy to share DB connections, config, auth.

### ✅ 5. High performance

Handles many requests per second.

## ✅ FastAPI — Small Examples
### ✅ 1. Basic API
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

```
Run:
```
uvicorn main:app --reload
```
### ✅ 2. Path & Query Parameters
```
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
```

Call:
```
GET /items/10?q=mobile
```
### ✅ 3. POST API with Request Body (Pydantic Model)
```
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

@app.post("/create-user")
def create_user(user: User):
    return {"message": "User created", "data": user}
```
### ✅ 4. Async API Example
```
@app.get("/async-data")
async def get_data():
    return {"status": "Async response"}
```
### ✅ 5. FastAPI for AI (LLM integration example)
```
from fastapi import FastAPI
from langchain_openai import ChatOpenAI

app = FastAPI()
llm = ChatOpenAI(model="gpt-4o-mini")

@app.post("/ask")
def ask(question: str):
    answer = llm.invoke(question).content
    return {"answer": answer}

```
## ✅ You now have a working AI API.
This is exactly how most GenAI projects deploy backend services.

 #### ✅ FastAPI vs Flask (Quick Comparison)
```
Feature           FastAPI 	           Flask
Speed	          🚀Very Fast	          Slow
Docs	           ✅ Auto	            ❌ Manual
Async	           ✅ Built-in	        ❌ Not native
Validation       ✅ Automatic 	      ❌ Need libraries
Industry Use      AI, Microservices    Simple APIs
```

✅ FastAPI is the future of Python APIs.

### One-line Answer

“FastAPI is a modern, high-performance Python framework for building APIs with automatic documentation, async support, and built-in validation.”

### Short Answer

FastAPI is a fast and developer-friendly Python framework used to build REST APIs. It provides automatic Swagger documentation, data validation through Pydantic, async support, and excellent performance. It is widely used in AI, microservices, and backend systems.
