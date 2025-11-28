python
import pandas as pd

# Load the dataset
df = pd.read_csv('Abu_Dhabi_Organizations_and_Their_Roles.csv')

# Display the first few rows
print(df.head())

# Function to filter organizations by sector
def filter_by_sector(sector):
    return df[df['Sector'] == sector]

# Example usage: Get organizations in the 'Education' sector
education_orgs = filter_by_sector('Education')
print(education_orgs)

# Analyze the role of a specific organization
def organization_role(organization_name):
    org_info = df[df['Organization'] == organization_name]
    return org_info[['Organization', 'Primary Function']]

# Example usage: Get the role of 'Abu Dhabi City Municipality'
municipality_role = organization_role('Abu Dhabi City Municipality')
print(municipality_role)
