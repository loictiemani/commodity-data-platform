import pandas as pd
import great_expectations as ge
import json
from datetime import datetime

# === Step 1: Load & Normalize Nested JSON ===
with open("/tmp/raw_eia_data.json", "r") as f:
    raw_json = json.load(f)

# Extract nested response.data
records = raw_json.get("response", {}).get("data", [])

# Flatten to DataFrame
df = pd.json_normalize(records)

# Preview to ensure expected structure
print(df.head())

# === Step 2: Convert to GE DataFrame ===
ge_df = ge.from_pandas(df)

# === Step 3: Define Expectations ===
# Check for expected columns
expected_columns = [
    "area-name", "duoarea", "period", "process", "process-name",
    "product", "product-name", "series", "series-description",
    "units", "value"
]

ge_df.expect_table_columns_to_match_ordered_list(column_list=expected_columns)

# Not null checks
ge_df.expect_column_values_to_not_be_null("area-name")
ge_df.expect_column_values_to_not_be_null("period")
ge_df.expect_column_values_to_not_be_null("product")
ge_df.expect_column_values_to_not_be_null("series")
ge_df.expect_column_values_to_not_be_null("value")

# Type checks
ge_df.expect_column_values_to_be_of_type("value", "float")

# Period format check (monthly: M01, M12, etc.)
ge_df.expect_column_values_to_match_regex("period", r"^M(0[1-9]|1[0-2])$")

# Value range check
ge_df.expect_column_values_to_be_between("value", min_value=0)

# Optional: check for unique series-product pairs
ge_df.expect_compound_columns_to_be_unique(["series", "period"])

# === Step 4: Validate and Print Results ===
results = ge_df.validate()
print("\nValidation Summary:")
print(results)
