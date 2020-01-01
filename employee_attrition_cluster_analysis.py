import matplotlib.pyplot as plot
import pandas as pds
from sklearn.cluster import KMeans

previous_employee = pds.read_excel('TakenMind-Python-Analytics-Problem-case-study-1-1.xlsx',
                                   sheet_name="Employees who have left")
current_employee = pds.read_excel('TakenMind-Python-Analytics-Problem-case-study-1-1.xlsx',
                                  sheet_name="Existing employees")
combined_dataset = pds.concat(
    [current_employee.assign(left_the_company='no'), previous_employee.assign(left_the_company='yes')])

# Cluster grouping of the dataset
previous_staffer = combined_dataset[['satisfaction_level', 'last_evaluation']][
    combined_dataset.left_the_company == 'yes']
fig = plot.subplots(figsize=(25, 10))
k_means = KMeans(n_clusters=3, random_state=0).fit(previous_staffer)
previous_staffer['label'] = k_means.labels_
plot.scatter(previous_staffer['satisfaction_level'], previous_staffer['last_evaluation'], c=previous_staffer['label'],
             cmap='Accent')
plot.xlabel('Satisfaction Level')
plot.ylabel('Last Evaluation')
plot.title('3 different Clusters of employees who left the company')
plot.savefig('Cluster Analysis Graph.png')
