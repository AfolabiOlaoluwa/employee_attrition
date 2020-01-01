import pandas as pds
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics

previous_employee = pds.read_excel('TakenMind-Python-Analytics-Problem-case-study-1-1.xlsx',
                                   sheet_name="Employees who have left")
current_employee = pds.read_excel('TakenMind-Python-Analytics-Problem-case-study-1-1.xlsx',
                                  sheet_name="Existing employees")
combined_dataset = pds.concat(
    [current_employee.assign(left_the_company=0), previous_employee.assign(left_the_company=1)])

le = preprocessing.LabelEncoder()
combined_dataset['salary'] = le.fit_transform(combined_dataset['salary'])
combined_dataset['dept'] = le.fit_transform(combined_dataset['dept'])
X = combined_dataset[['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours',
                      'time_spend_company', 'Work_accident', 'promotion_last_5years', 'dept', 'salary']]
y = combined_dataset['left_the_company']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
gb = GradientBoostingClassifier()
gb.fit(X_train, y_train)
y_pred = gb.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred))
print("Recall:", metrics.recall_score(y_test, y_pred))
