import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider


class AIResponse(BaseModel):
    answer: str


ollama_model = OpenAIModel(
    model_name='llama3.1:8b', provider=OpenAIProvider(base_url='http://localhost:11434/v1')
)

csv_agent = Agent(
    model=ollama_model,
    result_type=AIResponse,
    system_prompt="You are an expert data analyst. Answer questions based on the provided dataset."
)


# Global variables
global_df = None
column_names = []


def upload_csv(file):
    """Uploads CSV and validates it."""
    global global_df, column_names

    if file is None:
        return "⚠ No file uploaded.", None

    try:
        df = pd.read_csv(file.name)
        global_df = df
        column_names = df.columns.tolist()

        # Check if CSV is empty
        if df.empty:
            return "⚠ The uploaded CSV file is empty.", None

        # Check missing values
        missing_values = df.isnull().sum().sum()
        column_info = df.dtypes.to_string()
        preview = df.head()

        result = f"✅ File loaded successfully!\n"
        result += f"🔍 Missing Values: {missing_values}\n"
        result += f"📊 Column Types:\n{column_info}"

        return result, preview

    except Exception as e:
        return f"❌ Error loading file: {str(e)}", None


def plot_graph(x_column, y_column, graph_type):
    """Generates a graph based on user input and handles errors."""
    global global_df
    if global_df is None:
        return "⚠ No CSV file uploaded. Please upload a file first."

    try:
        plt.figure(figsize=(8, 5))

        if graph_type == "Bar":
            plt.bar(global_df[x_column], global_df[y_column], color="skyblue")
        elif graph_type == "Line":
            plt.plot(global_df[x_column], global_df[y_column],
                     marker="o", linestyle="-", color="green")
        elif graph_type == "Scatter":
            plt.scatter(global_df[x_column], global_df[y_column], color="red")

        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"{graph_type} Plot of {y_column} vs {x_column}")
        plt.xticks(rotation=45)
        plt.savefig("plot.png")
        plt.close()

        return "plot.png"

    except Exception as e:
        return f"❌ Error generating graph: {str(e)}"


async def query_csv(question):
    """Handles errors when querying CSV with LLM."""
    global global_df
    if global_df is None:
        return "⚠ No CSV file uploaded. Please upload a file first."

    if not question.strip():
        return "⚠ Question cannot be empty. Please ask something."

    try:
        sample_data = global_df.to_string()
        prompt = f"Q: {question}\nCSV file Data: {sample_data}"
        response = await csv_agent.run(prompt)
        return response.data

    except Exception as e:
        return f"❌ Error processing query: {str(e)}"



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