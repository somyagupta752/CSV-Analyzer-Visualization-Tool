import matplotlib.pyplot as plt
from file_handling import DataStore

def plot_graph(x_column, y_column, graph_type):
    """Generates a graph based on user input and handles errors."""
    datastore = DataStore()  # Get singleton instance
    df = datastore.global_df  # Access the shared dataframe

    if df is None:
        return "⚠ No CSV file uploaded. Please upload a file first."

    try:
        plt.figure(figsize=(8, 5))

        if graph_type == "Bar":
            plt.bar(df[x_column], df[y_column], color="skyblue")
        elif graph_type == "Line":
            plt.plot(df[x_column], df[y_column], marker="o", linestyle="-", color="green")
        elif graph_type == "Scatter":
            plt.scatter(df[x_column], df[y_column], color="red")

        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"{graph_type} Plot of {y_column} vs {x_column}")
        plt.xticks(rotation=45)
        plt.savefig("plot.png")
        plt.close()

        return "plot.png"

    except Exception as e:
        return f"❌ Error generating graph: {str(e)}"
