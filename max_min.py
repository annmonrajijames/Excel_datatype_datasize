import pandas as pd

# Function to determine the data type and size based on maximum and minimum values
def determine_data_type_and_size(max_value, min_value):
    """
    Determine the C data type and size based on the range of values.
    """
    # Try converting to float and check if it's really an integer
    try:
        max_val = float(max_value)
        min_val = float(min_value)
        is_integer = max_val.is_integer() and min_val.is_integer()
    except ValueError:
        # If value cannot be converted to float, it's a string or other type
        return "Invalid data type", None

    # Determine the type based on range and whether values are integers
    if is_integer:
        max_val, min_val = int(max_val), int(min_val)
        if min_val >= 0:  # Unsigned integer
            if max_val <= 255:
                return "uint8_t", 1
            elif max_val <= 65535:
                return "uint16_t", 2
            elif max_val <= 4294967295:
                return "uint32_t", 4
            else:
                return "uint64_t", 8
        else:  # Signed integer
            range_max = max(abs(max_val), abs(min_val))
            if -128 <= min_val <= 127:
                return "int8_t", 1
            elif -32768 <= min_val <= 32767:
                return "int16_t", 2
            elif -2147483648 <= min_val <= 2147483647:
                return "int32_t", 4
            else:
                return "int64_t", 8
    else:
        # Floating point (ESP32 supports only single precision)
        return "float", 4

# Load the data from the CSV file
file_path = r'C:\Lectrix_company\work\Git_Projects\Excel_datatype_datasize\max_min.csv'
data = pd.read_csv(file_path)

# Apply the function to each row to determine the data type and size
data[['Data_Type', 'Size_in_Bytes']] = data.apply(
    lambda row: determine_data_type_and_size(row['Maximum range of metric'], row['Minimum range of metric']),
    axis=1, result_type='expand')

# Save the updated DataFrame to a new CSV file
output_file_path = r'C:\Lectrix_company\work\Git_Projects\Excel_datatype_datasize\output.csv'
data.to_csv(output_file_path, index=False)

# Confirm the file has been saved
print(f"Data has been saved to {output_file_path}")
