import pandas as pd
import os
import re

# Set file paths
reviews_path = os.path.join('..', 'output', 'hospitality_reviews.csv')
business_path = os.path.join('..', 'output', 'hospitality_businesses.csv')
output_path = os.path.join('..', 'output', 'bias_reviews.csv')

# Load the filtered reviews
print("Loading hospitality reviews...")
df = pd.read_csv(reviews_path)
print(f"Total reviews loaded: {len(df)}")

# Clean the text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra spaces
    return text

df['clean_text'] = df['text'].apply(clean_text)

# Load business data with city info
print("Merging city info...")
business_df = pd.read_csv(business_path)[['business_id', 'city']]
df = df.merge(business_df, on='business_id', how='left')

# Define basic keyword lists
race_keywords = ['black', 'white', 'asian', 'hispanic', 'indian', 'mexican', 'african', 'racist']
gender_keywords = ['woman', 'female', 'man', 'male', 'lady', 'girl', 'creepy', 'harassed', 'uncomfortable']
treatment_keywords = ['rude', 'ignored', 'disrespectful', 'discriminated', 'unfair', 'refused service', 'profiling']

# Apply keyword flags
print("Flagging bias-related reviews...")
df['race_flag'] = df['clean_text'].apply(lambda x: any(word in x for word in race_keywords))
df['gender_flag'] = df['clean_text'].apply(lambda x: any(word in x for word in gender_keywords))
df['treatment_flag'] = df['clean_text'].apply(lambda x: any(word in x for word in treatment_keywords))

# Optional: total bias score
df['bias_count'] = df[['race_flag', 'gender_flag', 'treatment_flag']].sum(axis=1)

# Save cleaned & flagged data
df.to_csv(output_path, index=False)
print(f"\n✅ Bias-flagged reviews saved to: {output_path}")
print(f"Total possible bias reviews flagged: {df['bias_count'].sum()}")
