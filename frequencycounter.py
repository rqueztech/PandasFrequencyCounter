import os
import pandas as pd
import csv

frequ_counts = {}
frequ_counts_dict = {}

df = pd.read_csv('sampledata.csv', delimiter='\t')
df.reset_index(drop=True, inplace=True)

columnnames = []

for column_name in df.columns:
    columnnames.append(column_name)
    frequ_counts = df[column_name].value_counts()
    frequ_counts_copy = frequ_counts.copy()
    frequ_counts_dict[column_name] = frequ_counts_copy

show_column_names = True  # Toggle to show/hide column names

os.system("cls" if os.name == "nt" else "clear")

while True:
    if show_column_names:
        print("Enter the column name or index you want to see the frequency count of (or 'toggle' to toggle column names): ")

        count = 0

        for x in columnnames:
            if count % 5 == 0:
                print()

            printedcount = count + 1

            print(printedcount, x.ljust(20), end="\t")

            count += 1

    else:
        print("Enter the column name or index you want to see the frequency count of (or 'toggle' to toggle column names, 'clear' to clear the screen): ")
    print("")
    
    input_column = input().strip()
    
    if input_column.lower() == "toggle":
        show_column_names = not show_column_names
        if show_column_names:
            print("Column names are now shown.")
        else:
            print("Column names are now hidden.")
    elif input_column.lower() == "clear":
        os.system("cls" if os.name == "nt" else "clear")  # Clear the screen
    else:
        try:
            # Check if the input is an integer (index)
            column_index = int(input_column) - 1
            if 0 <= column_index < len(columnnames):
                column_name = columnnames[column_index]
                os.system("cls" if os.name == "nt" else "clear")
                print(frequ_counts_dict[column_name])
            else:
                print("Index out of range")
        except ValueError:
            # Input is not an integer, treat it as a column name
            if frequ_counts_dict.get(input_column) is None:
                print("Column name not found")
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print(frequ_counts_dict[input_column])
    
    # Prompt to press anything to continue
    input("Press Enter to continue...")
    os.system("cls" if os.name == "nt" else "clear")  # Clear the screen

