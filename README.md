---
title: deep-research-assistant-by-manjunath-asundi
app_file: deep_research.py
sdk: gradio
sdk_version: 5.31.0
---

<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" alt="AI Research Assistant" width="120" />
</p>

# Deep Research Assistant <img src="https://cdn-icons-png.flaticon.com/512/1828/1828884.png" alt="Magnifier" width="32" style="vertical-align:middle;"/>

Deep Research Assistant is a comprehensive <img src="https://cdn-icons-png.flaticon.com/512/4712/4712035.png" alt="AI" width="24" style="vertical-align:middle;"/> AI-powered application designed to automate and streamline the process of conducting in-depth research on any topic. By leveraging advanced language models and web search capabilities, it can plan, execute, and synthesize research with minimal user intervention, making it ideal for students, professionals, and anyone needing high-quality, structured information quickly.

## 🛠️ Tech Stack

- <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20" /> **Python 3.12+**
- <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/gradio/gradio-original.svg" width="20" /> **Gradio** (modern web interface for rapid prototyping and deployment)
- <img src="https://cdn-icons-png.flaticon.com/512/5968/5968705.png" width="20" /> **OpenAI GPT-4o-mini** (advanced AI model powering research and summarization)
- <img src="https://cdn-icons-png.flaticon.com/512/1055/1055687.png" width="20" /> **OpenAI Agent SDK** (enables seamless integration of OpenAI's agentic workflows, allowing the assistant to plan, execute, and chain tasks autonomously using OpenAI's latest agent framework)
- <img src="https://cdn-icons-png.flaticon.com/512/5968/5968705.png" width="20" /> **Pydantic** (robust data validation and settings management)
- <img src="https://cdn-icons-png.flaticon.com/512/1055/1055687.png" width="20" /> **Asyncio** (efficient asynchronous task management for concurrent operations)

## ✨ Features

- **Automated Research Planning:**  
  The assistant analyzes your query and generates three highly relevant web search terms, ensuring your research covers multiple perspectives and is both broad and deep.

- **Web Search & Summarization:**  
  For each search term, the assistant performs real-time web searches and summarizes the findings into concise, information-rich paragraphs, focusing on the most important insights.

- **Comprehensive Report Generation:**  
  All summaries are synthesized into a detailed, well-structured markdown report. The report typically spans 5-10 pages, includes an outline, a summary of findings, and a main body for clarity and readability.

- **Follow-up Suggestions:**  
  At the end of each report, you'll find a curated list of follow-up questions and suggested topics for further exploration, helping you continue your research journey.

- **Email Delivery:**  
  Optionally, receive the final report directly via email—perfect for sharing or saving for later reference.

- **Traceability:**  
  Each research session receives a unique trace ID, so you can review the process, debug, or audit the research steps for transparency and reproducibility.

## 🧭 How It Works

1. <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f50d.png" width="18" /> **Input a Query:**  
   Enter your research question or topic of interest into the application interface.

2. <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4a1.png" width="18" /> **Planning:**  
   The system analyzes your query and automatically generates three targeted web search terms that collectively address different aspects of your topic.

3. <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f50e.png" width="18" /> **Searching:**  
   Each search term is used to perform a web search. The assistant reads and summarizes the most relevant information from the search results, distilling them into concise, focused summaries.

4. <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4dd.png" width="18" /> **Report Writing:**  
   The assistant combines all summaries and synthesizes them into a detailed, markdown-formatted report. The report includes an outline, a short summary, the main content, and a list of follow-up questions.

5. <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4e4.png" width="18" /> **Delivery:**  
   The completed report is displayed within the app interface. Optionally, you can provide your email address to receive the report directly in your inbox.

6. <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f517.png" width="18" /> **Traceability:**  
   A unique trace link is provided for each session, allowing you to review the research process and outputs at any time.

## 🚀 Usage

This application is built using [Gradio](https://gradio.app/), making it easy to launch locally or deploy on cloud platforms. The interface is user-friendly and requires no prior technical knowledge.

### 🏠 Running Locally

1. <img src="https://cdn-icons-png.flaticon.com/512/1828/1828919.png" width="16" /> **Install dependencies:**  
   Ensure you have Python 3.12 or higher installed. Then, install all required packages using:
   ```
   uv venv
   source .venv/bin/activate
   uv add -r requirements.txt
   ```

2. <img src="https://cdn-icons-png.flaticon.com/512/1828/1828884.png" width="16" /> **Start the app:**  
   Launch the Gradio interface with:
   ```
   uv run deep_research.py 
   ```

3. <img src="https://cdn-icons-png.flaticon.com/512/709/709496.png" width="16" /> **Open in your browser:**  
   After starting, Gradio will provide a local URL (e.g., http://127.0.0.1:7860/). Open this link in your web browser to access the Deep Research Assistant.

## 🌐 Live Demo

✨ [Try Deep Research Assistant Now — Click Here!](https://huggingface.co/spaces/manju0707/deep-research-assistant-by-manjunath-asundi) ✨

No signup or installation needed. Just open the link, ask your question, and get a detailed research report in seconds!

**Screenshot:**  
![App Screenshot](https://github.com/manju07/deep-research-assistant/blob/main/deep-research-assistant-output.png)

## 📝 Example

Suppose you want to research <b>"The impact of remote work on employee productivity."</b>  
- <img src="https://cdn-icons-png.flaticon.com/512/1828/1828919.png" width="14" /> Enter this query into the app.
- <img src="https://cdn-icons-png.flaticon.com/512/1828/1828884.png" width="14" /> The assistant will generate three focused search terms, such as "remote work productivity studies," "challenges of remote work," and "benefits of remote work for companies."
- <img src="https://cdn-icons-png.flaticon.com/512/709/709496.png" width="14" /> It will search the web for each term, summarize the findings, and then synthesize a detailed report.
- <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" width="14" /> The final report will be displayed in the app and can also be sent to your email for convenience.

---

For more information, troubleshooting, or to contribute, please refer to the project repository or contact the maintainer.
