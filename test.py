import pandas as pd

if __name__ == "__main__":
    fileName = "HBDS2024.csv"
    with open(fileName, 'r') as file:
        line = file.read()
        print("Using read():")
        print(line)
