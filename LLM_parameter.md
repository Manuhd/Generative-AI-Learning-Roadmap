

# ⭐ **LLM PARAMETERS (Complete List)**
These parameters control how the LLM **thinks, generates, and behaves**.

# 🔵 **1. Generation / Sampling Parameters**

These control **creativity and randomness** of the output.

### **1️⃣ Temperature**

* Controls randomness
* High = creative
* Low = accurate
* Range: 0.0 – 2.0

### **2️⃣ Top-p (Nucleus Sampling)**

* Model picks from the smallest set of tokens whose total probability ≥ p
* Example: top_p = 0.9 → choose tokens covering 90% probability

### **3️⃣ Top-k**

* Model picks from only top **k most likely** next tokens
* Example: top_k = 50 → choose from 50 best choices

### **4️⃣ Max Tokens / Max Output Tokens**

* Maximum number of tokens the model can generate
* Higher = longer answers

### **5️⃣ Frequency Penalty**

* Reduces repetition of the same words
* High value → prevent repeating sentences

### **6️⃣ Presence Penalty**

* Encourages the model to talk about new topics
* Prevents looping

### **7️⃣ Repetition Penalty**

* General punishment for repeated tokens
* Used in many open-source models

### **8️⃣ Stop Sequences**

* Define when the model must stop generating
* Example: stop=["</end>"]

---

# 🔵 **2. Behavior / Control Parameters**

These control **how the LLM behaves**.

### **1️⃣ System Prompt / Role**

* Sets the model identity
* "You are a helpful assistant"

### **2️⃣ Seed**

* Controls randomness reproducibility
* Same seed → same answer

### **3️⃣ Response Format**

* JSON mode
* Structured output
* OpenAI function calling
* Gemini tool calling

### **4️⃣ Safety Settings**

* Harmful content filters
* Toxicity level
* Corporate guardrails

---

# 🔵 **3. Performance Parameters**

These affect **speed, cost, latency**.

### **1️⃣ Context Window**

* Maximum tokens model can handle in prompt + output
* Example: GPT-4o = 128k tokens

### **2️⃣ Batch Size**

* How many inputs are processed in parallel

### **3️⃣ Streaming**

* Token streaming (like ChatGPT typing effect)

---

# 🔵 **4. Embedding Parameters**

Used in RAG / vector DB.

### **1️⃣ Embedding Dimensions**

* Length of vector (e.g., 768, 1024, 3072)

### **2️⃣ Chunk Size**

* How much content per chunk before embedding

### **3️⃣ Distance Metric**

* Cosine similarity
* Dot product
* Euclidean

---

# 🔵 **5. Fine-Tuning Parameters**

Used when training models.

### **1️⃣ Learning Rate**

### **2️⃣ Number of Epochs**

### **3️⃣ Batch Size**

### **4️⃣ LoRA Rank**

### **5️⃣ Warmup Steps**

---

# 🔵 **6. Vendor-Specific Parameters**

Different providers have custom parameters:

### ✔️ **OpenAI (ChatOpenAI)**

* temperature
* top_p
* frequency_penalty
* presence_penalty
* max_tokens
* response_format (JSON mode)
* logprobs

### ✔️ **Gemini (ChatGoogleGenerativeAI)**

* temperature
* top_p
* top_k
* max_output_tokens
* safety_settings
* response_schema

### ✔️ **Claude**

* temperature
* max_tokens
* stop sequences

---

# ⭐ **Short**

**LLM parameters control how the model generates text.
Key parameters include temperature, top-p, top-k, max tokens, frequency penalty, and presence penalty.
These define creativity, randomness, repetition control, and length of output.
Different providers like OpenAI, Gemini, and Claude implement slight variations.**

---
