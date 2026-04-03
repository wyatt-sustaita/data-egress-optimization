import pandas as pd
import os
import json

# LIST OF FUNCTIONS


def dGroup(df):
    df_grouped = df.groupby(['Document_Number', 'Unit', 'Vendor', 'Tag_ID', 'Item_SKU', 'Client_ID', 'Item_Price']).agg(
        {'Item_Quantity': 'sum', 'Item_Extended_Price': 'sum'}).reset_index()
    return df_grouped


def dClean(df):
    df_clean = df[df['Item_Quantity'] != 0]
    return df_clean


# Step 1: Declare Paths
inputDataPath = "Sample_Input_Data.json"
outputDataPath = "Test_Output_Data.json"

# Step 2: Read the JSON file into a DataFrame.
df = pd.read_json(inputDataPath)

# Step 3: Group the data by item and net the values
df_grouped = dGroup(df)

# Step 4: Remove rows with zero quantities
df_clean = dClean(df_grouped)

# Step 5: Generate the optimized JSON file
df_clean.to_json(outputDataPath, orient='records', indent=4)

print("Data optimization complete. Output saved to 'Test_Output_Data.json'")
