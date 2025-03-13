import gradio as gr
from file_handling import upload_csv
from graph_plotting import plot_graph
from query_processing import query_csv

csv_interface = gr.Interface(
    fn=upload_csv,
    inputs=gr.File(),
    outputs=["text", "dataframe"],
    title="📂 CSV File Uploader & Validator",
    description="Upload a CSV file and explore its contents.",
)

graph_interface = gr.Interface(
    fn=plot_graph,
    inputs=[
        gr.Textbox(label="📊 X-axis Column"),
        gr.Textbox(label="📈 Y-axis Column"),
        gr.Radio(["Bar", "Line", "Scatter"], label="📍 Graph Type")
    ],
    outputs="image",
    title="📉 CSV Graph Generator",
    description="Enter column names and select a graph type to visualize data.",
)

query_interface = gr.Interface(
    fn=query_csv,
    inputs=gr.Textbox(placeholder="🧠 Ask a question about your data..."),
    outputs="text",
    title="🔍 CSV Question Answering",
    description="Ask the AI about your uploaded CSV data.",
)

with open("styles.css", "r") as css_file:
    custom_css = css_file.read()

gr.TabbedInterface(
    [csv_interface, graph_interface, query_interface],
    ["📂 Upload CSV", "📊 Generate Graph", "🧠 Ask Questions"],
    css=custom_css
).launch()