import pandas as pd

# Load dataset
df = pd.read_csv("data/creditcard.csv")

summary = []
summary.append(f"Shape: {df.shape}")
summary.append("\nColumn list and data types:\n")
summary.append(df.dtypes.to_string())
summary.append("\n\nFirst 10 rows:\n")
summary.append(df.head(10).to_string())
summary.append("\n\nBasic descriptive statistics:\n")
summary.append(df.describe().to_string())

print("\n".join(summary))

output_path = "_extra/proposal_data_summary.txt"
with open(output_path, "w") as f:
    f.write("\n".join(summary))

print(f"\nSummary saved to {output_path}")