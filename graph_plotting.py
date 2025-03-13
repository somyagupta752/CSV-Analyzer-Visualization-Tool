import matplotlib.pyplot as plt
from file_handling import global_df

def plot_graph(x_column, y_column, graph_type):
    """Generates a graph based on user input and handles errors."""
    if global_df is None:
        return "⚠ No CSV file uploaded. Please upload a file first."

    try:
        plt.figure(figsize=(8, 5))

        if graph_type == "Bar":
            plt.bar(global_df[x_column], global_df[y_column], color="skyblue")
        elif graph_type == "Line":
            plt.plot(global_df[x_column], global_df[y_column], marker="o", linestyle="-", color="green")
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