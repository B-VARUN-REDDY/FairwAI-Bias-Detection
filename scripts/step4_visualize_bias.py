import pandas as pd
import os
import matplotlib.pyplot as plt

# Paths
input_path = os.path.join('..', 'output', 'bias_reviews.csv')

# Load data
df = pd.read_csv(input_path)
print(f"Total bias-reviewed entries: {len(df)}")

# --- Analysis 1: Flag counts ---
flag_counts = df[['race_flag', 'gender_flag', 'treatment_flag']].sum()

# Bar chart of flag counts
plt.figure(figsize=(8, 6))
flag_counts.plot(kind='bar')
plt.title('Number of Reviews Flagged for Potential Bias (Race / Gender / Treatment)')
plt.ylabel('Review Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('../output/bias_flag_counts.png')
plt.show()

# --- Analysis 2: Bias Count by City ---
if 'city' in df.columns:
    city_bias = df[df['bias_count'] > 0].groupby('city').size().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10, 6))
    city_bias.plot(kind='bar')
    plt.title('Top 10 Cities by Number of Reviews Flagged for Bias')
    plt.ylabel('Review Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('../output/top_bias_cities.png')
    plt.show()
else:
    print("No 'city' column found — city-level analysis skipped.")
