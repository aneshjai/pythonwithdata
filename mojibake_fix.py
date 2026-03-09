import pandas as pd
import html

# Read CSV using the wrong encoding on purpose
df = pd.read_csv("b15d8f18-9bd6-4513-97fe-8e753a5d2cda.csv", encoding="latin1")

def fix_text(text):
    if not isinstance(text, str):
        return text

    # Step 1: fix mojibake
    try:
        text = text.encode("latin1").decode("utf-8")
    except UnicodeError:
        pass

    # Step 2: decode HTML entities
    text = html.unescape(text)

    return text

# Apply only to string columns (faster & safer)
for col in df.select_dtypes(include="object"):
    df[col] = df[col].apply(fix_text)

# Write clean UTF-8 CSV
df.to_csv("output_fixed.csv", index=False, encoding="utf-8")
