from ucimlrepo import fetch_ucirepo
import pandas as pd

# ---------------------------------------
# Load Iris dataset from UCI Repository
# ---------------------------------------
iris = fetch_ucirepo(id=53)

# Features and target
X = iris.data.features
y = iris.data.targets

# ---------------------------------------
# Dataset summary
# ---------------------------------------
print("========== DATASET SUMMARY ==========")
print(f"Number of records : {len(X)}")
print(f"Number of features: {X.shape[1]}")
print(f"Number of classes : {y.nunique().iloc[0]}")

print("\nClass Distribution:")
print(y.iloc[:, 0].value_counts())

# ---------------------------------------
# Load dataset from CSV
# ---------------------------------------
url = "https://archive.ics.uci.edu/static/public/53/data.csv"
df = pd.read_csv(url)

print("\n========== DATA INFORMATION ==========")
print(df.head())
print()
df.info()

# ---------------------------------------
# Missing values
# ---------------------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# ---------------------------------------
# Duplicate records
# ---------------------------------------
duplicate_count = df.duplicated().sum()

print("\n========== DUPLICATE CHECK ==========")
print(f"Duplicate records: {duplicate_count}")

if duplicate_count > 0:
    print("\nDuplicate rows:")
    print(df[df.duplicated()])

    # Remove duplicates
    df = df.drop_duplicates()

print(f"\nDataset size after removing duplicates: {df.shape}")

# ---------------------------------------
# Final Summary
# ---------------------------------------
print("\n========== FINAL SUMMARY ==========")

print(f"Features           : {X.shape[1]}")
print(f"Classes            : {y.nunique().iloc[0]}")

print("Class names:")
print(y.value_counts())

print(f"Duplicate records  : {duplicate_count}")
print(f"Final dataset size : {df.shape[0]} rows × {df.shape[1]} columns")
