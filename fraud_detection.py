import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1. LOAD DATASET
# =========================
file_path = r"C:\Users\HP\OneDrive\Documents\transactions.csv"
data = pd.read_csv(file_path)

print("Sample Data:")
print(data.head())


# =========================
# 2. RISK ANALYSIS FUNCTION
# =========================
def analyze_transaction(amount):
    if amount >= 50000000:
        return "High Risk", "Unusually large transaction", 90
    elif amount >= 10000000:
        return "Medium Risk", "Above normal transaction range", 60
    elif amount < 500000:
        return "Low Risk", "Normal low transaction", 10
    else:
        return "Low Risk", "Moderate transaction", 30


# =========================
# 3. APPLY ANALYSIS
# =========================
results = data['Amount'].apply(analyze_transaction)

data['Risk_Level'] = results.apply(lambda x: x[0])
data['Fraud_Reason'] = results.apply(lambda x: x[1])
data['Risk_Score'] = results.apply(lambda x: x[2])


# =========================
# 4. DUPLICATE CHECK
# =========================
duplicates = data[data.duplicated()]


# =========================
# 5. SAVE OUTPUT
# =========================
output_path = r"C:\Users\HP\OneDrive\Documents\risk_report.csv"
data.to_csv(output_path, index=False)


# =========================
# 6. DISPLAY RESULTS
# =========================
print("\nRisk Summary:")
print(data['Risk_Level'].value_counts())

print("\nDuplicate Transactions:")
print(duplicates)


# =========================
# 7. VISUALIZATION
# =========================
data['Risk_Level'].value_counts().plot(kind='bar')

plt.title("Transaction Risk Distribution")
plt.xlabel("Risk Level")
plt.ylabel("Number of Transactions")

plt.show()


# =========================
# 8. FINAL MESSAGE
# =========================
print("\nAnalysis completed successfully!")
print("Report saved at:", output_path)