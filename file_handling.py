import pandas as pd

class DataStore:
    """Singleton class to store global data."""
    _instance = None
    global_df = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataStore, cls).__new__(cls)
        return cls._instance

def upload_csv(file):
    """Uploads CSV and validates it."""
    if file is None:
        return "⚠ No file uploaded.", None

    try:
        df = pd.read_csv(file.name)
        datastore = DataStore()  # Get singleton instance
        datastore.global_df = df  # Store the dataframe globally

        if df.empty:
            return "⚠ The uploaded CSV file is empty.", None

        missing_values = df.isnull().sum().sum()
        column_info = df.dtypes.to_string()
        preview = df.head()

        result = f"✅ File loaded successfully!\n"
        result += f"🔍 Missing Values: {missing_values}\n"
        result += f"📊 Column Types:\n{column_info}"

        return result, preview

    except Exception as e:
        return f"❌ Error loading file: {str(e)}", None
