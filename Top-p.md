# 🎯 **What is Top-p (Nucleus Sampling)? **

**Top-p controls how many “likely next words” the LLM is allowed to choose from.**

Instead of taking all possible words, the model selects only the **most probable words whose combined probability = p**.

---

# ✔ Example (Very Easy)

Suppose the model can choose the next word from this probability list:

| Word    | Probability |
| ------- | ----------- |
| “cat”   | 0.40        |
| “dog”   | 0.30        |
| “apple” | 0.10        |
| “car”   | 0.10        |
| “moon”  | 0.05        |
| “train” | 0.05        |

---

### 🟩 If **top-p = 0.5**

Model chooses from words whose combined probability = **50%**.
So it only picks from:

* “cat” (0.40)
* “dog” (0.30 → exceeds 0.5 if added, so stop)

So allowed choices = **["cat"] only**
→ output becomes more **predictable**.

---

### 🟧 If **top-p = 0.9**

Model chooses words until probability sum reaches **90%**:

* cat (0.40)
* dog (0.30)
* apple (0.10)
* car (0.10)
  Total = 0.90 → stop.

Allowed choices =
**["cat", "dog", "apple", "car"]**
→ more creative options.

---

### 🔥 If **top-p = 1.0**

Model can pick from **all words** → most creative and random.

---

# 🧠 Summary 

**Top-p restricts the model to pick from only the top probable words whose cumulative probability adds up to p.
Lower top-p = more focused + accurate. Higher top-p = more creative.**

---

# 🧪 Difference between Temperature & Top-p (Very Important)

| Feature    | Temperature        | Top-p                         |
| ---------- | ------------------ | ----------------------------- |
| Controls   | randomness         | how many likely words allowed |
| Low value  | deterministic      | fewer choices                 |
| High value | creative           | more choices                  |
| Type       | randomness scaling | probability cutoff            |

---
