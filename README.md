---
title: deep-research-assistant-by-manjunath-asundi
app_file: deep_research.py
sdk: gradio
sdk_version: 5.31.0
---

# Deep Research Assistant

Deep Research Assistant is a comprehensive AI-powered application designed to automate and streamline the process of conducting in-depth research on any topic. By leveraging advanced language models and web search capabilities, it can plan, execute, and synthesize research with minimal user intervention, making it ideal for students, professionals, and anyone needing high-quality, structured information quickly.

## Tech Stack

- **Python 3.12+**
- **Gradio** (for the web interface)
- **OpenAI GPT-4o-mini** (AI model)
- **Pydantic** (data validation)
- **Asyncio** (for async tasks)


## Features

- **Automated Research Planning:**  
  Upon receiving your query, the assistant intelligently analyzes it and generates a set of three highly relevant and focused web search terms. This ensures that the research covers multiple facets of your topic, increasing the breadth and depth of the final report.

- **Web Search & Summarization:**  
  For each generated search term, the assistant performs real-time web searches. It then summarizes the findings for each term into concise, information-rich paragraphs, filtering out irrelevant details and focusing on the core insights.

- **Comprehensive Report Generation:**  
  The assistant synthesizes all gathered summaries into a cohesive, well-structured report written in markdown format. The report is designed to be detailed and thorough, typically spanning 5-10 pages and exceeding 1000 words. It includes an outline, a short summary of findings, and the main body of the report, ensuring clarity and readability.

- **Follow-up Suggestions:**  
  At the end of each report, the assistant provides a curated list of follow-up questions and suggested topics for further exploration. This helps guide future research or deeper dives into related areas.

- **Email Delivery:**  
  Users have the option to receive the final report directly via email. This feature is especially useful for sharing results with colleagues or saving them for later reference.

- **Traceability:**  
  Every research session is assigned a unique trace ID, allowing users to review the process, debug issues, or audit the research steps for transparency and reproducibility.

## How It Works

1. **Input a Query:**  
   Enter your research question or topic of interest into the application interface.

2. **Planning:**  
   The system analyzes your query and automatically generates three targeted web search terms that collectively address different aspects of your topic.

3. **Searching:**  
   Each search term is used to perform a web search. The assistant reads and summarizes the most relevant information from the search results, distilling them into concise, focused summaries.

4. **Report Writing:**  
   The assistant combines all summaries and synthesizes them into a detailed, markdown-formatted report. The report includes an outline, a short summary, the main content, and a list of follow-up questions.

5. **Delivery:**  
   The completed report is displayed within the app interface. Optionally, you can provide your email address to receive the report directly in your inbox.

6. **Traceability:**  
   A unique trace link is provided for each session, allowing you to review the research process and outputs at any time.

## Usage

This application is built using [Gradio](https://gradio.app/), making it easy to launch locally or deploy on cloud platforms. The interface is user-friendly and requires no prior technical knowledge.

### Running Locally

1. **Install dependencies:**  
   Ensure you have Python 3.12 or higher installed. Then, install all required packages using:
   ```
   pip install -r requirements.txt
   ```

2. **Start the app:**  
   Launch the Gradio interface with:
   ```
   gradio app_file=deep_research.py
   ```

3. **Open in your browser:**  
   After starting, Gradio will provide a local URL (e.g., http://127.0.0.1:7860/). Open this link in your web browser to access the Deep Research Assistant.

## Live Demo

Try the Deep Research Assistant instantly in your browser:  
[https://huggingface.co/spaces/manju0707/deep-research-assistant-by-manjunath-asundi](https://huggingface.co/spaces/manju0707/deep-research-assistant-by-manjunath-asundi)

Image link - 
### Example

Suppose you want to research "The impact of remote work on employee productivity."  
- Enter this query into the app.
- The assistant will generate three focused search terms, such as "remote work productivity studies," "challenges of remote work," and "benefits of remote work for companies."
- It will search the web for each term, summarize the findings, and then synthesize a detailed report.
- The final report will be displayed in the app and can also be sent to your email for convenience.

---

For more information, troubleshooting, or to contribute, please refer to the project repository or contact the maintainer.
