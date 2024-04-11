# ValueError: cannot reindex on an axis with duplicate labels

import pandas as pd

df = pd.DataFrame({
    'id': [112, 113, 114, 115],
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'salary': [1500, 2500, 3500, 4500],
}, index=[0, 1, 1, 2])  # 👈️ non-unique indexes

#     id  name  salary
# 1  114  Carl    3500
print(df[df.index.duplicated()])