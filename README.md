# LangChain JSON Output Parser
[![LangChain](https://img.shields.io/badge/Framework-LangChain-green)](https://www.langchain.com/)
[![JSON](https://img.shields.io/badge/Format-JSON-blue)](https://www.json.org/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)

## 🏗️ Project Overview
This repository demonstrates the use of the **`JsonOutputParser`** in LangChain. This parser is the "middle ground" between raw string manipulation and strict Pydantic validation. It is highly optimized for models that natively understand JSON structures (like Gemini Pro), providing a fast and reliable way to turn unstructured text into a standard Python dictionary without the overhead of external validation libraries.

---

## 🛠️ Key Technical Implementations

### 1. Flexible Schema Injection
* **Dictionary Blueprints:** Defining the desired output structure using simple Python dictionaries, which the parser then converts into format instructions for the LLM.
* **Dynamic Content:** Ideally suited for scenarios where the output keys might change based on user input.

### 2. Stream-Friendly Parsing
* **Incremental Extraction:** One of the key advantages of this parser is its ability to handle partial JSON. As the LLM streams its response, the parser can often yield valid (though incomplete) dictionaries, enabling more responsive UIs.

### 3. Lightweight Orchestration
* **LCEL Pipeline:** Implemented as a standard link in the chain: `Prompt | Model | JsonOutputParser`.
* **Zero Overhead:** Ideal for microservices and serverless functions where performance and package size are critical.

---

## 💻 Tech Stack
* **Language:** Python 3.9+
* **Orchestration:** LangChain (`langchain-core`, `langchain-google-genai`)
* **Model:** Google Gemini Pro
* **Environment:** `python-dotenv`

---

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/langchain-json-extraction-engine.git](https://github.com/your-username/langchain-json-extraction-engine.git)

2. **Install Dependencies:**
   ```bash
   pip install -U langchain-core langchain-google-genai python-dotenv

3. **Setup API Key:**
   Create a .env file in the root directory:

   ```bash
   GOOGLE_API_KEY=your_gemini_key_here

4. **Run the Implementation:**
   ```bash
   python json_output_parser.py   
