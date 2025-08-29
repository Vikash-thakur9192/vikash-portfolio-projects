import pandas as pd

data = {
    "id": [101, 102, 103, 104, 105, 102, 106, 107, 108, 109],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Bob", "Frank", None, "Heidi", "Ivan"],
    "city": ["New York", "Los Angeles ", "Chicago", None, "Houston", "Los Angeles", "Phoenix", "Dallas", "Chicago", "Houston"],
    "age": [25, 30, None, 22, 28, 30, 35, None, 29, 40],
    "income": [50000, 60000, 55000, None, 65000, 60000, None, 58000, 62000, None],
    "joined_at": ["2023-01-15", "2022-07-20", "2023-03-10", "2022-05-12", None,
                  "2022-07-20", "2023-02-28", "2023-04-01", "2023-03-15", None],
    "segment": ["A", "B", None, "A", "C", "B", "C", None, "A", "C"]
}
# conver into dataframe
df = pd.DataFrame(data)
# info about the dataframe
df.info()
df.isnull().sum()
# deleting duplicat and keeping only first one
df = df.drop_duplicates(subset=['id'],keep='first')
#filling age column using fillna with median and convert float into int
df['age']= df['age'].fillna(df['age'].median()).astype(int)
# converting joined_at to datetime & deleting the missing values of city and datetime
df['joined_at']= pd.to_datetime(df['joined_at'], errors='coerce')
df = df.dropna(subset=['city','joined_at'])
# filling income column using fillna with average salary
df['income']= df['income'].fillna(df['income'].mean()).astype(int)
#changing null value in segment with 'Not Assign'
df['segment']= df['segment'].fillna('Not Assigned')
# mending the columns
df['name']= df['name'].str.strip().str.title()
df['city']= df['city'].str.strip().str.title().str.center(5)
print(df)

#converting into csv for later use
df.to_csv('employee_data.csv',index=False)