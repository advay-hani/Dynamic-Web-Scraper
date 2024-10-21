import csv
from googlesearch import search
import pandas as pd
import time
import random

def get_top_urls(query):
    urls = []
    try:
        # Perform search using googlesearch
        for url in search(query, num_results=3):
            urls.append(url)
    except Exception as e:
        print(f"Error occurred during search: {e}")
    return urls

# Step 1: Load search queries from search_results_new.csv
with open('search_results new.csv', mode='r') as file:
    reader = csv.reader(file)
    queries = list(reader)

columns = ['Query', 'URL1', 'URL2', 'URL3']

# Step 2: Collect URLs without removing duplicates and save them in links_saved_new_dupl.csv
df_dupl = pd.DataFrame(columns=columns)

# Loop through queries, perform search, and collect URLs
total_links_with_duplicates = 0
for query in queries:
    urls = get_top_urls(query[0])
    total_links_with_duplicates += len(urls)  # Count total links found (with duplicates)
    row = {
        'Query': query[0],
        'URL1': urls[0] if len(urls) > 0 else '',
        'URL2': urls[1] if len(urls) > 1 else '',
        'URL3': urls[2] if len(urls) > 2 else ''
    }
    df_dupl.loc[len(df_dupl)] = row

# Save search results with duplicates to CSV
df_dupl.to_csv('links_saved_new_dupl.csv', index=False)

# Step 3: Remove duplicates from the URL columns and save them in links_saved_new.csv
df_no_dupl = df_dupl.copy()

# Flatten URL columns into a single list, remove duplicates, and re-assign them back
df_no_dupl['URL1'] = df_no_dupl['URL1'].apply(lambda x: '' if x == '' else x)
df_no_dupl['URL2'] = df_no_dupl['URL2'].apply(lambda x: '' if x == '' or x in df_no_dupl['URL1'].values else x)
df_no_dupl['URL3'] = df_no_dupl['URL3'].apply(lambda x: '' if x == '' or x in df_no_dupl['URL1'].values or x in df_no_dupl['URL2'].values else x)

# Calculate total number of links after removing duplicates
total_links_without_duplicates = df_no_dupl[['URL1', 'URL2', 'URL3']].apply(lambda x: x.astype(bool).sum(), axis=1).sum()

# Save the results without duplicates to a new CSV
df_no_dupl.to_csv('links_saved_new.csv', index=False)

# Print out the total number of links with and without duplicates
print(f"Total links with duplicates: {total_links_with_duplicates}")
print(f"Total links without duplicates: {total_links_without_duplicates}")
