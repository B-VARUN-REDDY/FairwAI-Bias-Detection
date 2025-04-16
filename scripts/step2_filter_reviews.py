import pandas as pd
import os

# Set paths
business_path = os.path.join('..', 'output', 'hospitality_businesses.csv')
reviews_path = os.path.join('..', 'data', 'yelp_academic_dataset_review.json')
output_path = os.path.join('..', 'output', 'hospitality_reviews.csv')

# Load business IDs
print("Loading Hospitality Business IDs...")
hospitality_df = pd.read_csv(business_path)
business_ids = set(hospitality_df['business_id'].unique())

print(f"Unique Hospitality Businesses: {len(business_ids)}")

# Prepare to store filtered reviews
filtered_reviews = []

print("Filtering reviews in chunks...")

# Read large review file in chunks
chunksize = 100000

for chunk in pd.read_json(reviews_path, lines=True, chunksize=chunksize):
    filtered_chunk = chunk[chunk['business_id'].isin(business_ids)]
    filtered_reviews.append(filtered_chunk)
    print(f"Filtered Reviews so far: {sum(len(df) for df in filtered_reviews)}")

# Combine all filtered chunks
final_reviews = pd.concat(filtered_reviews)

print(f"Total Filtered Reviews: {len(final_reviews)}")

# Save to output
final_reviews.to_csv(output_path, index=False)
print(f"Filtered reviews saved to: {output_path}")
