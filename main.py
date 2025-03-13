import pandas as pd

# Load bank statement
bank_df = pd.read_excel("Input 1 - Bank Statement.xlsx")

# Load transaction records
transactions_df = pd.read_excel("Input 2 - Transaction Records.xlsx")

def main():
    print("Hello from pycash!")


if __name__ == "__main__":
    main()
