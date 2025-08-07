# QueryForge

**QueryForge** is an LLM-powered data analysis tool that takes a CSV file, a natural language question, and returns a tailored pandas script that runs server-side in a secure sandbox—no schema, no templates, no bullshit.

Built for fast, stateless, in-session querying with zero setup friction.

---

## 🔧 MVP Features

- Upload a CSV file
- Ask a free-form natural language question
- Query is sent to OpenAI API
- LLM generates a pandas script to answer the question
- Script is executed server-side in a restricted environment
- Output (value, table, or plot) is returned to the user

---

## 🚫 What It Doesn't Do (by design)

- No user authentication
- No saved history
- No database
- No stored tokens
- No pre-defined schemas

This is a disposable, surgical interface for ad-hoc data analysis.

---
