import matplotlib.pyplot as plot
import pandas as pds
import seaborn as sbn

previous_employee = pds.read_excel('TakenMind-Python-Analytics-Problem-case-study-1-1.xlsx',
                                   sheet_name="Employees who have left")
current_employee = pds.read_excel('TakenMind-Python-Analytics-Problem-case-study-1-1.xlsx',
                                  sheet_name="Existing employees")

# previous_employee summary
print(previous_employee.head())
print(previous_employee.tail())
print(previous_employee.describe())
print(previous_employee.info())
print(previous_employee.columns)

cols = ['satisfaction_level', 'number_project', 'time_spend_company', 'Work_accident', 'promotion_last_5years', 'dept',
        'salary']
fig = plot.subplots(figsize=(25, 10))
for i, j in enumerate(cols):
    plot.subplot(2, 4, i + 1)
    plot.subplots_adjust(hspace=1.0)
    sbn.countplot(x=j, data=previous_employee)
    plot.xticks(rotation=90)
    plot.title("Previous Employee Information")
    plot.tight_layout()
    plot.savefig('Previous Employee Information.png')

# Satisfactory insight count based on number of projects
number_of_projects = previous_employee.groupby('number_project').count()
print(number_of_projects['satisfaction_level'])

# Satisfactory insight count based on number of years used in the company
time_spent = previous_employee.groupby('time_spend_company').count()
print(time_spent['satisfaction_level'])

# combined_dataset summary
combined_dataset = pds.concat(
    [current_employee.assign(left_the_company='no'), previous_employee.assign(left_the_company='yes')])

print(combined_dataset.describe())
print(combined_dataset.shape)
print(combined_dataset.info())
print(combined_dataset.columns)

cols = ['satisfaction_level', 'number_project', 'time_spend_company', 'Work_accident', 'promotion_last_5years', 'dept',
        'salary', 'left_the_company']

fig = plot.subplots(figsize=(25, 10))
for i, val in enumerate(cols):
    plot.subplot(2, 4, i + 1)
    plot.subplots_adjust(hspace=1.0)
    sbn.countplot(x=val, data=combined_dataset, hue='left_the_company')
    plot.xticks(rotation=90)
    plot.title("Combined Dataset Information")
    plot.tight_layout()
    plot.savefig('Combined Dataset Information.png')
