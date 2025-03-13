import pandas as pd

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