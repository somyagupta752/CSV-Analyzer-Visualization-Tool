from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from file_handling import DataStore

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

async def query_csv(question):
    """Handles errors when querying CSV with LLM."""
    datastore = DataStore()  # Get singleton instance
    global_df = datastore.global_df  # Access the shared dataframe
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