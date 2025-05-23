import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# Load the dataset
file_path = 'sociodemograpgicinequalitiesinsuicidesdataset20230306correction.xlsx'

# Load the only sheet we need
df = pd.read_excel(file_path, sheet_name='Table 2')

#replace the default column names with the values from the first row
df.columns = df.iloc[0]

#remove empty rows from the  dataFrame
df = df.dropna(how='all')

#Define the columns
df.columns = ['Exposure', 'Group', 'Population size', 'Number of suicide deaths', 'Number of deaths from all other causes']

#Check for missing values
df.isnull().sum()

#Defien your ethniciy varaiable to only ethnicity data.
ethnicity_df = df[df['Exposure'] == 'Ethnicity'].copy()

# Calculate suicide rate per 100,000 for Ethnicity.
ethnicity_df['Suicide Rate per 100,000'] = (
    ethnicity_df['Number of suicide deaths'] / ethnicity_df['Population size']
) * 100000

ethnicity_comparison = ethnicity_df.groupby('Group')['Suicide Rate per 100,000'].mean()

ethnicity_df_sorted = ethnicity_comparison.sort_values(ascending=False)

#create the chart
ethnicity_df_sorted.plot(kind='barh', color='skyblue')
plt.title('Average Suicide Rate per 100,000 by Ethnicity')
plt.xlabel('Suicide Rate per 100,000')
plt.ylabel('Ethnicity')
plt.tight_layout()
plt.show()

# defien the varileb for sex to only inlcude data related to sex/gender
sex_df = df[df['Exposure'] == 'Sex'].copy()

# Calculate suicide rate per 100,000 for Sex (male/female).
sex_df['Suicide Rate per 100,000'] = (
    sex_df['Number of suicide deaths'] / sex_df['Population size']
) * 100000



#Compare the  mean of suicide rate by gender
sex_comparison = sex_df.groupby('Group')['Suicide Rate per 100,000'].mean()

# Create the bar chart
sex_comparison.plot(kind='bar', color=['blue', 'orange'])
plt.title('Average Suicide Rate per 100,000 by Sex')
plt.xlabel('Sex')
plt.ylabel('Suicide Rate per 100,000')
plt.xticks(rotation=0)  
plt.show()

# defien the varileb for age  to only inlcude data realted to age.
Age_df= df[df['Exposure'] == 'Age group'].copy()

# Calculate suicide rate per 100,000 for age.
Age_df['Suicide Rate per 100,000'] = (
    Age_df['Number of suicide deaths'] / Age_df['Population size']
) * 100000

#Compare the  mean of suicide rate by age.
Age_comparison= Age_df.groupby('Group')['Suicide Rate per 100,000'].mean ()

# Create the bar chart
Age_comparison.plot(kind='bar', color=['red'])
plt.title('Average Suicide Rate per 100,000 by Age')
plt.ylabel ('Suicide Rate per 100,000')
plt.xlabel('Age group')
plt.show()

# defien the varileb for disability status   to only inlcude data realted to disability status.
disability_df= df[df['Exposure'] == 'Disability status'].copy()

# Calculate suicide rate per 100,000 for age.
disability_df['Suicide Rate per 100,000'] = (
    disability_df['Number of suicide deaths'] / disability_df['Population size']
) * 100000


#Compare the  mean of suicide rate by disability status.
disability_coparison= disability_df.groupby ('Group') ['Suicide Rate per 100,000'].mean ()

# Create the bar chart
disability_coparison.plot(kind='bar', color=['red','blue'])
plt.title('Average Suicide Rate per 100,000 by Disability Status')
plt.xlabel ('Distability Status')
plt.ylabel ( 'Suicide Rate per 100,000')
plt.xticks(rotation=0) 
plt.show
