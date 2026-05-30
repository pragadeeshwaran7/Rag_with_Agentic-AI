# 📝 Agentic RAG Question Paper Generator

[![Live Demo](https://img.shields.io/badge/Live_Demo-ragqp.vercel.app-success?style=for-the-badge&logo=vercel)](https://ragqp.vercel.app/)

An advanced, full-stack AI application that leverages **Retrieval-Augmented Generation (RAG)** to instantly generate perfectly structured, academically accurate mock question papers for various Indian Board Examinations (CBSE, ICSE, and West Bengal Board).

## 🌟 Live Demo

**Try it out here:** [https://ragqp.vercel.app/](https://ragqp.vercel.app/)

---

## ✨ Novel Features

- **Intelligent Pattern Replication:** Unlike generic AI prompts, this system enforces strict adherence to official Board guidelines. It programmatically injects the exact section distributions, marks allocation, and specific exam instructions depending on the chosen Board and Subject.
- **Agentic RAG Pipeline:** The generation doesn't hallucinate. It pulls verified syllabus context directly from a curated vector knowledge base before formulating questions, ensuring the output is grounded in actual curriculum topics.
- **Cognitive Difficulty Scaling:** Dynamically adjusts the cognitive load of the generated questions (Easy, Medium, Hard) while mathematically preserving the structural integrity and total marks of the Board's required pattern.
- **Zero-Dependency PDF Export:** Utilizes a highly optimized client-side `html2pdf.js` rendering engine, providing beautiful, print-ready PDFs without the massive overhead of server-side PDF generation libraries.
- **Vercel Serverless Architecture:** Natively restructured for Vercel's Zero-Config deployment. The FastAPI backend runs entirely on ultra-fast Serverless Functions, with dependencies aggressively pruned to fit well within the strict 250MB hobby-tier limits.

---

## 🏗️ Technical Architecture

The application is built using a modern decoupled architecture:

### Frontend
- **React + Vite:** Lightning-fast HMR and optimized production builds.
- **Tailwind CSS v4:** Modern, utility-first styling with a premium glassmorphism dark-mode aesthetic.
- **Axios & React Markdown:** Seamless API communication and beautiful typography rendering for the generated papers.

### Backend (Serverless API)
- **FastAPI:** High-performance async Python framework routing the endpoints (`/api/boards`, `/api/generate`).
- **LangChain:** Orchestrates the complex RAG chain, tying together prompt templates, document chunking, and the LLM.
- **Groq (Llama-3.3-70b-versatile):** Acts as the primary ultra-fast reasoning engine. Google's Gemini-1.5-Pro is supported as an immediate fallback.
- **Knowledge Base:** Markdown-based syllabus extraction engine that parses specific board requirements at runtime.

---

## 🚀 Local Setup Instructions

Want to run it locally? Follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/pragadeeshwaran7/Rag_with_Agentic-AI.git
cd Rag_with_Agentic-AI
```

### 2. Set Up the Backend
```bash
# Move into the api directory
cd api

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Create your .env file
echo "GROQ_API_KEY=your_groq_api_key_here" > .env

# Run the FastAPI server
uvicorn index:app --reload --port 8000
```

### 3. Set Up the Frontend
Open a new terminal window:
```bash
# From the root directory, install dependencies
npm install

# Start the Vite development server
npm run dev
```

Visit `http://localhost:5173` to see the app running locally!

---

