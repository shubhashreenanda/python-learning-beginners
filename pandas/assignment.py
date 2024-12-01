import pandas as pd

df = pd.read_csv('sample_data.csv')
print(df)

print("Printing first 5 records")
print(df.head(5))

print("Printing column name and data type")
print(df.dtypes)

print("Printing summary")
print(df.describe())

print("Printing number of rows and column")
row, column = df.shape
print('Rows: ', row)
print('Columns: ', column)

print("Data manipulation rename column")
df.rename({'Height(Inches)': 'Height', 'Weight(Pounds)': 'Weight'},axis='columns', inplace=True)
print(df)

print("Add a new column")
df['Height_in_meters'] = df['Height']*0.0254
print(df)

print("Filter row")
print(df.query('Weight > 150'))
print(df[df.Weight > 150])