import pandas as pd

# Specify the full path of the input CSV file
input_file_path = r"C:\Lectrix_company\work\Git_Projects\Excel_data_type_size\Data_type_size.csv"

# Read the input CSV file
df = pd.read_csv(input_file_path)

# Calculate the maximum and minimum values for each column
max_values = df.max()
min_values = df.min()

# Create a new DataFrame for the output
output_df = pd.DataFrame(columns=["Data", "Maximum", "Minimum"])

# Convert the column-wise data to row-wise
for col_name, max_val, min_val in zip(df.columns, max_values, min_values):
    output_df = pd.concat([output_df, pd.DataFrame({"Data": [col_name], "Maximum": [max_val], "Minimum": [min_val]})], ignore_index=True)

# Specify the full path of the output CSV file
output_file_path = r"C:\Lectrix_company\work\Git_Projects\Excel_data_type_size\Output.csv"

# Save the output DataFrame to the specified CSV file
output_df.to_csv(output_file_path, index=False)
