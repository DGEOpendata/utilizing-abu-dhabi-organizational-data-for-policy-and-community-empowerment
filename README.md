# Utilizing Abu Dhabi Organizational Data for Policy and Community Empowerment

This project demonstrates how to use the dataset "Abu Dhabi Organizations and Their Roles" to gain insights into the roles and functions of various organizations in Abu Dhabi. This documentation will guide you through the process of implementing the use case, providing example code and explanations.

## Prerequisites
- Python 3.x
- Pandas library

## Installation
1. Ensure Python is installed on your machine. You can download it from [python.org](https://www.python.org/).
2. Install the Pandas library using pip:
   bash
   pip install pandas
   

## Dataset
The dataset used in this project should be downloaded and placed in the same directory as your script. The file is named `Abu_Dhabi_Organizations_and_Their_Roles.csv`.

## Example Code
The example code provided in this documentation demonstrates how to load the dataset, filter organizations by sector, and analyze the role of specific organizations.

### Loading the Dataset
The dataset is loaded using Pandas:
python
import pandas as pd

df = pd.read_csv('Abu_Dhabi_Organizations_and_Their_Roles.csv')
print(df.head())

This code snippet reads the CSV file and prints the first few rows.

### Filtering by Sector
The function `filter_by_sector` allows you to filter organizations based on their sector:
python
def filter_by_sector(sector):
    return df[df['Sector'] == sector]

education_orgs = filter_by_sector('Education')
print(education_orgs)

This example filters and prints organizations in the 'Education' sector.

### Analyzing Organization Roles
The function `organization_role` retrieves the primary function of a specified organization:
python
def organization_role(organization_name):
    org_info = df[df['Organization'] == organization_name]
    return org_info[['Organization', 'Primary Function']]

municipality_role = organization_role('Abu Dhabi City Municipality')
print(municipality_role)

This example prints the role of the 'Abu Dhabi City Municipality'.

## Conclusion
This documentation provides a basic framework for utilizing the dataset "Abu Dhabi Organizations and Their Roles". By adapting the example code, users can perform more complex analyses tailored to their specific interests or research questions. Further enhancements could involve integrating the dataset into larger data analysis pipelines or visualizing the data for more intuitive insights.