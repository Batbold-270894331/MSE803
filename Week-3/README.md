# Week 3 - Activity 1: Data Cleaning

## Overview

Before performing statistical analysis, the original dataset was cleaned to improve data quality and consistency.

- Raw file: `Sample_dataset.csv`
- Cleaned file: `Sample_dataset_cleaned.csv`

The original dataset was kept unchanged.

---

## Data Cleaning Steps

### 1. Clean text values
Extra spaces were removed from `Name` and `Country`.

Example:

```text
" Alice " -> "Alice"
```

---

### 2. Correct text entered in numeric columns

Known text errors were corrected.

```text
thirty-eight -> 38
sixty five thousand -> 65000
```

This allows `Age` and `Salary` to be treated as numeric values.

---

### 3. Clean Net worth

Commas were removed from `Net worth`.

```text
30,000 -> 30000
```

The column was then converted to numeric format.

---

### 4. Convert numeric columns

The following columns were converted to numeric data types:

- `ID`
- `Age`
- `Net worth`
- `Salary`

Invalid numeric values were converted to missing values using `errors="coerce"`.

---

### 5. Standardise Country

Australia had two values:

```text
AU
AUS
```

They were standardised as:

```text
AUS
```

`NZ` was kept unchanged.

Final country values:

```text
NZ
AUS
```

---

### 6. Clean Join Date

Different date formats were converted to one standard format:

```text
dd/MM/yyyy
```

Example:

```text
2020-01-15 -> 15/01/2020
```

The invalid date:

```text
2019-13-01
```

was treated as a known data-entry error and corrected to:

```text
2019-01-13
```

which becomes:

```text
13/01/2019
```

This correction is an assumption for this activity.

---

### 7. Merge duplicate Bob records

Bob appeared more than once with the same ID.

Rows with the same ID were merged into one record, keeping the first available non-missing value from each column.

This prevents duplicate records while preserving useful information.

---

### 8. Handle missing Name

Missing names were replaced with:

```text
Unknown
```

This avoids inventing a person's name.

---

### 9. Handle missing Country

Missing country values were filled using the **mode**.

The mode is the most frequently occurring country in the dataset.

This method was used because `Country` is categorical data.

---

### 10. Handle missing Age

Missing `Age` values were filled using the **median** age.

The median is the middle value after the numbers are sorted.

It is less affected by unusually high or low values than the mean.

---

### 11. Handle missing Net worth

Missing `Net worth` values were filled using the median.

The median was chosen because financial data can contain extreme values.

---

### 12. Handle missing Salary

Missing `Salary` values were filled using the median salary.

The median is less affected by very high or very low salaries.

---

### 13. Handle missing ID

Missing IDs were not automatically created or estimated.

An ID is an identifier, so it should normally be confirmed from the original source.

---

### 14. Sort and validate the data

The cleaned dataset was sorted by ID.

The data was then checked again for:

- remaining missing values
- formatting problems
- duplicate records
- incorrect data types

---

### 15. Save cleaned data

The cleaned dataset was saved as:

```text
Sample_dataset_cleaned.csv
```

The original dataset was not overwritten.

---

## Cleaning Summary

| Data issue | Action |
|---|---|
| Extra spaces | Removed |
| Text in Age | Converted to numeric |
| Text in Salary | Converted to numeric |
| Commas in Net worth | Removed |
| `AU` country code | Changed to `AUS` |
| `NZ` country code | Kept as `NZ` |
| Missing Country | Filled using mode |
| Mixed date formats | Standardised to `dd/MM/yyyy` |
| Invalid date | Corrected using a documented assumption |
| Duplicate Bob records | Merged by ID |
| Missing Name | Replaced with `Unknown` |
| Missing Age | Filled using median |
| Missing Net worth | Filled using median |
| Missing Salary | Filled using median |
| Missing ID | Left for verification |

---

## Important Note

Some missing values were estimated using the median or mode.

These are **imputed values**, not original observed values.

The invalid date correction is also an assumption made for this activity.

The cleaned dataset is now ready for the next step: **basic statistical analysis**.
