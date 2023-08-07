# https://colab.research.google.com/drive/1R1FkLo9F2KZ06SnaUIJQJotTABjPAKwY?usp=sharing

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_csv():
    print("Choose an option:")
    print("1. Upload from local computer")
    print("2. Enter URL")
    print("3. Use a predefined URL")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        file_path = input("Enter the path of the .csv file: ")
    elif choice == '2':
        url = input("Enter the URL of the .csv file: ")
        file_path = pd.read_csv(url)
    elif choice == '3':
        url = "https://example.com/data.csv"  # Replace with your predefined URL
        file_path = pd.read_csv(url)
    else:
        print("Invalid choice.")
        return None
    
    return file_path

def main():
    df = load_csv()
    
    if df is None:
        return
    
    print("Dataframe loaded successfully.\n")
    print("Column names:")
    print(df.columns.tolist())
    
    print("\nFirst two rows:")
    print(df.head(2))
    
    column_names = df.columns.tolist()
    
    print("\nChoose one or two columns:")
    print("Available columns:", column_names)
    
    selected_columns = input("Enter column names (comma-separated): ").split(',')
    selected_columns = [col.strip() for col in selected_columns]
    
    if len(selected_columns) > 2:
        print("Please select at most two columns.")
        return
    
    data = df[selected_columns].values
    
    print("\nChoose a type of graph:")
    print("1. Scatter plot")
    print("2. Line graph")
    
    graph_choice = input("Enter your choice: ")
    
    if graph_choice == '1':
        plt.scatter(data[:, 0], data[:, 1])
        plt.xlabel(selected_columns[0])
        plt.ylabel(selected_columns[1])
        plt.title("Scatter Plot")
        plt.show()
    elif graph_choice == '2':
        plt.plot(data[:, 0], data[:, 1])
        plt.xlabel(selected_columns[0])
        plt.ylabel(selected_columns[1])
        plt.title("Line Graph")
        plt.show()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
