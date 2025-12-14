import pandas as pd
import matplotlib.pyplot as plt

# Load sample dataset (later replace with Germany renewables dataset)
url = "https://raw.githubusercontent.com/datasets/energy/master/data/energy.csv"
df = pd.read_csv(url)

# Show basic info
print("Rows:", len(df))
print(df.head())

# Plot sample trend if column exists
if 'Quantity' in df.columns:
    df['Quantity'].plot(figsize=(10,4), title='Sample energy trend')
    plt.show()
feat: add week_01_load_data script
