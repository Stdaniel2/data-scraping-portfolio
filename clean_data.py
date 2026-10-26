import pandas as pd

# Load the scraped dataset
df = pd.read_csv("quotes_raw.csv")

print("BEFORE CLEANING")
print("Total records:", len(df))
print("Missing values:\n", df.isna().sum())

# Remove leading and trailing whitespace
for column in ["quote", "author", "tags"]:
    df[column] = df[column].astype("string").str.strip()

# Remove records missing essential information
df = df.dropna(subset=["quote", "author"])

# Remove records with empty quotes or author names
df = df[
    df["quote"].ne("") &
    df["author"].ne("")
]

# Remove duplicate records
df = df.drop_duplicates(subset=["quote", "author"])

# Reset the row index
df = df.reset_index(drop=True)

# Save the cleaned dataset
df.to_csv("quotes_clean.csv", index=False, encoding="utf-8-sig")
df.to_excel("quotes_clean.xlsx", index=False)

print("\nAFTER CLEANING")
print("Total records:", len(df))
print("Missing values:\n", df.isna().sum())

print("\nCleaned dataset saved successfully!")