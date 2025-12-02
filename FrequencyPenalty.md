

# 🎯 **What is Frequency Penalty?**

**Frequency penalty reduces the score of words that the model has already used many times.**

Meaning:

* If a word repeats often → its probability decreases.
* This helps avoid repetition in answers.

---

# 🧠 Why do we need it?

LLMs sometimes repeat phrases like:

* “The reason is…”
* “In conclusion…”
* “The main point is…”

Frequency penalty **forces the model to use different words** instead of repeating the same one again and again.

---

# ✔ Example (Very Easy)

User input:
👉 *“Explain RAG.”*

Without frequency penalty:
“RAG works by retrieving relevant chunks and generating answers based on those chunks. These chunks help the model generate better answers because chunks contain context.”

Repeats **“chunks”** too much.

---

### After applying **frequency penalty = 1.0**

“RAG retrieves relevant sections of text and then the model uses that context to produce a final answer.”

✔ Repetition reduced
✔ More diverse words

---

# 🔢 How it works internally

Each time the model uses a word,
→ a penalty is added to that word’s probability.
→ the model prefers other words.

---

# 🔍 Difference Between Frequency Penalty vs Presence Penalty

| Feature  | Frequency Penalty                    | Presence Penalty                         |
| -------- | ------------------------------------ | ---------------------------------------- |
| Purpose  | Reduce repeated words                | Encourage *introducing new topics/words* |
| Based on | How many times word already appeared | Whether the word appeared at least once  |
| Effect   | Less repetition                      | More variety / new ideas                 |

**Frequency penalty = reduce overuse**
**Presence penalty = encourage diversity**

---

# 🎯 Summary

“Frequency penalty reduces how often an LLM repeats the same word.
The more times a word was already used, the more the model penalizes it, encouraging varied wording."

---
