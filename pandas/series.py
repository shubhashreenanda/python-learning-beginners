from itertools import count

import pandas as pd

reviews = pd.Series([4.6, 4.4, 4.8, 5])
print(reviews)
print(reviews.describe())
print(reviews[0])

print(reviews.count())
print(reviews.mean())
print(reviews.min())
print(reviews.max())
print(reviews.std())

reviews = pd.Series([4.6, 4.4, 4.8, 5], index =['python','django','devops','c++'])
print(reviews)

courses = pd.Series(['java','python','aws'])
print(courses)
print(courses.str.upper())
print(courses.str.contains('y'))