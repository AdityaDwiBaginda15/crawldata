import pandas as pd
import numpy as np

# Menentukan jumlah data dan kolom
num_data = 100
num_columns = 5

# Membuat data dummy dengan numpy
data = np.random.rand(num_data, num_columns)

# Membuat DataFrame dengan pandas
df = pd.DataFrame(data, columns=[f'Column_{i+1}' for i in range(num_columns)])

# Menampilkan DataFrame
print(df)

# Menyimpan DataFrame ke dalam file CSV
df.to_csv('dummy_data.csv', index=False)
