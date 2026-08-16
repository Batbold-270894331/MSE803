import pandas as pd

# Load data
df = pd.read_csv("Sample_dataset.csv")

# Clean text
df["Name"] = df["Name"].astype("string").str.strip()
df["Country"] = df["Country"].astype("string").str.strip()

# Fix text numbers
df["Age"] = df["Age"].replace({"thirty-eight": "38"})
df["Salary"] = df["Salary"].replace({"sixty five thousand": "65000"})

# Remove commas
df["Net worth"] = (
    df["Net worth"]
    .astype("string")
    .str.replace(",", "", regex=False)
)

# Convert to numeric
df["ID"] = pd.to_numeric(df["ID"], errors="coerce")
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Net worth"] = pd.to_numeric(df["Net worth"], errors="coerce")
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

# Standardise country
df["Country"] = df["Country"].replace({"AU": "AUS"})

# Fix invalid date
df["Join Date"] = df["Join Date"].replace({
    "2019-13-01": "2019-01-13"
})

# Parse dd/MM/yyyy
date_ddmmyyyy = pd.to_datetime(
    df["Join Date"],
    format="%d/%m/%Y",
    errors="coerce"
)

# Parse yyyy-MM-dd
date_yyyymmdd = pd.to_datetime(
    df["Join Date"],
    format="%Y-%m-%d",
    errors="coerce"
)

# Merge date formats
df["Join Date"] = date_ddmmyyyy.fillna(date_yyyymmdd)

# Format dates
df["Join Date"] = df["Join Date"].dt.strftime("%d/%m/%Y")

# Get first valid value
def first_valid_value(column):
    valid_values = column.dropna()

    if len(valid_values) > 0:
        return valid_values.iloc[0]

    return pd.NA

# Separate valid IDs
with_id = df[df["ID"].notna()]
without_id = df[df["ID"].isna()]

# Merge duplicate IDs
with_id = (
    with_id
    .groupby("ID", as_index=False)
    .agg(first_valid_value)
)

# Add missing-ID rows
df = pd.concat(
    [with_id, without_id],
    ignore_index=True
)

# Fill missing names
df["Name"] = df["Name"].fillna("Unknown")

# Fill missing country
country_mode = df["Country"].mode()[0]
df["Country"] = df["Country"].fillna(country_mode)

# Fill missing age
age_median = df["Age"].median()
df["Age"] = df["Age"].fillna(age_median)

# Fill missing net worth
networth_median = df["Net worth"].median()
df["Net worth"] = df["Net worth"].fillna(networth_median)

# Fill missing salary
salary_median = df["Salary"].median()
df["Salary"] = df["Salary"].fillna(salary_median)

# Sort by ID
df = df.sort_values(
    by="ID",
    na_position="last"
).reset_index(drop=True)

# Show cleaned data
print("\nCleaned Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Show imputed values
print("\nValues used:")
print("Country mode:", country_mode)
print("Age median:", age_median)
print("Net worth median:", networth_median)
print("Salary median:", salary_median)

# Save cleaned data
df.to_csv(
    "Sample_dataset_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved.")