import pandas as pd

# Load the CSV file
file_path = r'C:\Lectrix_company\work\Git_Projects\Excel_datatype_datasize\log_file.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Calculate the maximum and minimum values for each metric
max_values = data.max()
min_values = data.min()

# Create a DataFrame for the output
output_df = pd.DataFrame({
    'Data': data.columns,
    'Maximum range': max_values.values,
    'Minimum range': min_values.values
})

# Define the output file path
output_file_path = r'C:\Lectrix_company\work\Git_Projects\Excel_datatype_datasize\output_max_min.csv'  # Specify your desired output file path

# Save the results to a CSV file
output_df.to_csv(output_file_path, index=False)
