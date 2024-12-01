from tkinter.font import names

import pandas as pd

customer_df = pd.read_csv('customer_df.csv',names=['first_name','last_name','email','phone'])
print(customer_df)

customer_df.to_csv('customer.csv',index=False)
