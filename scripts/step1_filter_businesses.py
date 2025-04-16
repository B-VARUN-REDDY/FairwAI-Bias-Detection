import pandas as pd
import os

# Set paths
input_path = os.path.join('..', 'data', 'yelp_academic_dataset_business.json')
output_path = os.path.join('..', 'output', 'hospitality_businesses.csv')

# Load business data
print("Loading business data...")
business_df = pd.read_json(input_path, lines=True)

# Show total businesses
print(f"Total businesses in dataset: {len(business_df)}")

# DEBUG: See what cities are available
print("\nSample of unique cities in dataset:")
print(business_df['city'].dropna().unique()[:50])  # Show first 50 unique cities

# Target cities (these are what FairwAI requested)
target_cities = ['Tampa', 'Indianapolis', 'Boise', 'New Orleans', 'Philadelphia']


# Filter for target cities
city_filtered = business_df[business_df['city'].isin(target_cities)]
print(f"\nBusinesses in target cities: {len(city_filtered)}")

# DEBUG: Safely sample category values
if len(city_filtered) > 0:
    print("\nSample categories from filtered businesses:")
    print(city_filtered['categories'].dropna().sample(min(10, len(city_filtered))))
else:
    print("No businesses found in selected cities. Check city names!")

# Expanded hospitality-related keywords
hospitality_keywords = [
    'Hotel', 'Resort', 'Motel', 'Inn', 'Hostel', 'Lodging',
    'Restaurant', 'Dining', 'Food', 'Cafe', 'Eatery',
    'Spa', 'Wellness', 'Massage'
]

# Filter by categories that mention hospitality terms
hospitality_filtered = city_filtered[
    city_filtered['categories'].str.contains('|'.join(hospitality_keywords), na=False, case=False)
]
print(f"\nHospitality-related businesses found: {len(hospitality_filtered)}")

# Save to output
hospitality_filtered.to_csv(output_path, index=False)
print(f"\n✅ Filtered data saved to: {output_path}")
