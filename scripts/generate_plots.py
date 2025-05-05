import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import textwrap
import os

# Create images directory if it doesn't exist
if not os.path.exists('public/images'):
    os.makedirs('public/images')

# Read data
indus_parks_all = pd.read_csv('CGS_Industrial_Parks_Sept_2024.csv')

# Convert boolean columns to numeric (0/1)
boolean_columns = ['Foreign Founder or Manager', 'Foreign Tenants', 
                  'China as Founder or Manager', 'China as Tenant',
                  'PLN', 'Captive Coal Power Plant', 'Captive Gas Power Plant', 
                  'Bioenergy', 'Solar', 'Hydropower', 'Electricity Provider Unclear',
                  'Legal dispute with Indonesian government', 'Legal dispute with a company', 
                  'Dispute with local residents', 'Workers\' rights dispute', 
                  'Environmental Impact', 'Land Acquisition Issues']

for col in boolean_columns:
    indus_parks_all[col] = pd.to_numeric(indus_parks_all[col], errors='coerce').fillna(0)

# Data preprocessing
indus_parks_all['Electricity Capacity (GW)'] = indus_parks_all['Electricity Capacity (MW)']/1000

# Set up seaborn
sns.set()
sns.set_style("whitegrid")

# Define color palettes
status_pal = ['#D9D9D9', '#FDE49B', '#A6E4B7', '#277E3E', '#4285F4', '#E75D51']
indus_pal = ['#6DB1A6', '#DBDB92', '#9D99B8', '#D76154', '#045993','#D89343', 
            '#D9ABC2', "#9A619C", '#DCCA4E', '#6B392D', '#B7B7B7']
elec_pal = ['#009DAD', '#000000', '#6D4F16', '#60A760', '#DBB714', '#353783', '#B7B7B7']
status_pal_known = ['#FDE49B', '#A6E4B7', '#277E3E', '#4285F4']

# Function for wrapping labels
def wrap_labels(ax, width, break_long_words=False):
    labels = []
    for label in ax.get_xticklabels():
        text = label.get_text()
        labels.append(textwrap.fill(text, width=width, break_long_words=break_long_words))
    ax.set_xticks(ax.get_xticks())  # Fix for deprecation warning
    ax.set_xticklabels(labels, rotation=0)

# 1. Status Distribution
fig, ax = plt.subplots(figsize=(10,6))
status_order = ["Before Construction", "Under Construction", "Operational", 
               "Operational with Continued Construction", "Stalled", "Unclear"]
sns.countplot(data=indus_parks_all, x="Status", hue="Status", 
             order=status_order, palette=status_pal, legend=False)
plt.xlabel("Status")
plt.ylabel("Number of Industrial Parks")
plt.title("Status of Industrial Parks in Indonesia", fontsize="large")
ax.bar_label(ax.containers[0])
wrap_labels(ax, 10)
plt.tight_layout()
plt.savefig('public/images/status_distribution.png')
plt.close()

# 2. Industry Distribution
fig, ax = plt.subplots(figsize=(10,6))
indus_order = ['Mixed/General', 'Manufacturing', 'IT', 'Nickel', 'Aluminum', 
              'Other Metals', 'Chemicals', 'Petrochemical', 'Palm Oil', 'Coal', 'Unknown']
sns.countplot(data=indus_parks_all, y="Main Industry", hue="Main Industry",
             order=indus_order, palette=indus_pal, legend=False)
plt.xlabel("Number of Industrial Parks")
plt.ylabel("Main Industry")
plt.title("Main Industries of Industrial Parks in Indonesia", fontsize="large")
ax.bar_label(ax.containers[0])
plt.tight_layout()
plt.savefig('public/images/industry_distribution.png')
plt.close()

# [Previous plots remain the same...]

# 8. Foreign Companies Analysis
fig, ax = plt.subplots(figsize=(10,6))
data = {
    'Type': ['Foreign\nFounder/Manager', 'Foreign\nTenants', 
             'Chinese\nFounder/Manager', 'Chinese\nTenant'],
    'Count': [
        int(indus_parks_all['Foreign Founder or Manager'].sum()),
        int(indus_parks_all['Foreign Tenants'].sum()),
        int(indus_parks_all['China as Founder or Manager'].sum()),
        int(indus_parks_all['China as Tenant'].sum())
    ]
}
foreign_df = pd.DataFrame(data)

sns.barplot(data=foreign_df, x='Type', y='Count', hue='Type', legend=False)
plt.xlabel("Foreign Company Type")
plt.ylabel("Number of Industrial Parks")
plt.title("Foreign Company Involvement in Indonesian Industrial Parks", fontsize="large")
ax.bar_label(ax.containers[0])
wrap_labels(ax, 10)
plt.tight_layout()
plt.savefig('public/images/foreign_companies.png')
plt.close()

# 9. Disputes Distribution
dispute_list = ['Legal dispute with Indonesian government', 'Legal dispute with a company',
               'Dispute with local residents', 'Workers\' rights dispute',
               'Environmental Impact', 'Land Acquisition Issues']
dispute_counts = indus_parks_all[dispute_list].sum().reset_index()
dispute_counts.columns = ["Dispute Types", "Count of Industrial Parks"]
dispute_counts = dispute_counts.sort_values(by="Count of Industrial Parks", ascending=False)

fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(data=dispute_counts, x="Dispute Types", y="Count of Industrial Parks", 
           hue="Dispute Types", legend=False)
plt.xlabel("Dispute Types")
plt.ylabel("Number of Industrial Parks")
plt.title("Disputes at Industrial Parks in Indonesia", fontsize="large")
ax.bar_label(ax.containers[0])
wrap_labels(ax, 10)
plt.tight_layout()
plt.savefig('public/images/disputes.png')
plt.close()

print("All plots have been generated and saved in the public/images directory")