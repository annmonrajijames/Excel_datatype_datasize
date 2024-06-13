import pandas as pd

# Path to the input CSV file
input_file_path = r'C:\Lectrix_company\work\Git_Projects\Excel_data_type_size\max_min.csv'

# Path to save the output CSV file
output_file_path = r'C:\Lectrix_company\work\Git_Projects\Excel_data_type_size\output.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file_path)

# Clean the data by removing non-numeric characters and converting to numeric type
df['Maximum'] = pd.to_numeric(df['Maximum'].str.replace('[^0-9.-]', ''), errors='coerce')
df['Minimum'] = pd.to_numeric(df['Minimum'].str.replace('[^0-9.-]', ''), errors='coerce')

# Function to find the C data type of a value based on its size
def find_c_data_type(value):
    if pd.isnull(value):
        return "NULL"
    elif isinstance(value, int):
        if -128 <= value <= 127:
            return "char"
        elif 0 <= value <= 255:
            return "unsigned char"
        elif -32768 <= value <= 32767:
            return "short"
        elif 0 <= value <= 65535:
            return "unsigned short"
        elif -2147483648 <= value <= 2147483647:
            return "int"
        elif 0 <= value <= 4294967295:
            return "unsigned int"
        else:
            return "long long"
    elif isinstance(value, float):
        if value.is_integer():
            if -2147483648 <= value <= 2147483647:
                return "int"
            else:
                return "long long"
        else:
            return "double"
    elif isinstance(value, str):
        return "char[]"
    else:
        return "Unknown"

# Get the data types of each value in the "Maximum" and "Minimum" columns
max_data_types = df['Maximum'].apply(find_c_data_type)
min_data_types = df['Minimum'].apply(find_c_data_type)

# Add new columns to the DataFrame to store the data types
df['Maximum_DataType'] = max_data_types
df['Minimum_DataType'] = min_data_types

# Save the DataFrame to a new CSV file
df.to_csv(output_file_path, index=False)

print("Data types saved successfully.")
