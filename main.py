import pandas as pd
import fitz


# Load bank statement
bank_df = pd.read_excel("Input 1 - Bank Statement.xlsx")

# Load transaction records
transactions_df = pd.read_excel("Input 2 - Transaction Records.xlsx")

total_receipts = transactions_df[transactions_df["Amount"] > 0]["Amount"].sum()
total_payments = transactions_df[transactions_df["Amount"] < 0]["Amount"].sum()
net_cash_flow = total_receipts + total_payments
doc = fitz.open("Input 3 - Vouchers.pdf")
text = ''

for page in doc:
    text += page.get_text()
doc.close()


print(f"Total Receipts: {total_receipts}")
print(f"Total Payments: {total_payments}")
print(f"Net Cash Flow: {net_cash_flow}")

def main():
    print("Hello from pycash!")


if __name__ == "__main__":
    main()
