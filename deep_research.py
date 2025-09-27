import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)


async def run(query: str):
    async for chunk in ResearchManager().run(query):
        yield chunk


with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Deep Research Assistant\n crafted by Manjunath Asundi")
    query_textbox = gr.Textbox(
        label="🔎 What topic would you like to research?",
        placeholder="Type your research topic here...",
        lines=3,
        elem_classes=["big-query-textbox"],
        scale=2
    )
    gr.HTML(
        """
        <style>
        .big-query-textbox textarea {
            font-size: 1.5em !important;
            padding: 1.2em !important;
            border-radius: 12px !important;
            border: 2px solid #38bdf8 !important;
            box-shadow: 0 4px 16px rgba(56,189,248,0.10);
            background: #f0f9ff;
        }
        .big-query-textbox label {
            font-size: 1.2em !important;
            font-weight: bold !important;
            color: #0369a1 !important;
        }
        </style>
        """
    )
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")
    
    run_button.click(fn=run, inputs=query_textbox, outputs=report)
    query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)

ui.launch(inbrowser=True)

