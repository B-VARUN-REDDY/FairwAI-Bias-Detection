FairwAI Hospitality Bias Detection

This repository contains the code, visuals, and summary documentation for the FairwAI Hospitality Intern Challenge. The analysis investigates bias, discrimination, or unfair treatment in hospitality reviews (hotels, restaurants, spas, etc.) using the Yelp Open Dataset.

📂 Repository Structure

FairwAI_Challenge/
├── scripts/                     # Python scripts used for filtering and analysis
│   ├── step1_filter_businesses.py
│   ├── step2_filter_reviews.py
│   ├── step3_bias_signals.py
│   └── step4_visualize_bias.py
│
├── output/                      # Visuals and sample data (no full CSVs)
│   ├── bias_flag_counts.png
│   ├── top_bias_cities.png
│   └── bias_reviews_sample.csv (optional small sample only)
│
├── FairwAI_Submission_Summary.docx  # Final write-up summary
├── requirements.txt
└── README.md                   # This file

🚨 Important Notice on Dataset Access

To reduce repository size and avoid GitHub limits, all large data files (JSON, CSV, and Yelp TAR/ZIP files) have been excluded.

If you wish to replicate the project:

Download the Yelp Open Dataset:
https://www.yelp.com/dataset

Download and extract the following files:

yelp_academic_dataset_business.json

yelp_academic_dataset_review.json

yelp_academic_dataset_user.json

Place them in a local data/ directory or wherever referenced in the scripts.

Run the scripts in order:

Step 1 → Filter businesses in target cities

Step 2 → Extract relevant reviews

Step 3 → Flag potential bias using keyword matching

Step 4 → Generate visuals from the flagged data

📈 Sample Visuals Included

Bias category flag counts across reviews

Top cities by flagged bias keywords

These were generated from the filtered data and are safe to view without the full dataset.

🤖 Tools Used

Python 3.11+

pandas

matplotlib

Git LFS (for managing large files – optional)

Install dependencies:

pip install -r requirements.txt

📬 Contact

Prepared by Varun Reddy Bhimavarapu

For any questions or collaboration:

GitHub: github.com/B-VARUN-REDDY

LinkedIn: linkedin.com/in/varun-bhimavarapu

📄 License

This project is for educational and research use as part of the FairwAI Internship Challenge.

All datasets referenced belong to Yelp and are subject to their open dataset license.

