import pandas as pd
import os

df = pd.DataFrame({
    "Name":["Ayuhs","Vasu","Lakshay"],
    "city":["UP","UK","Sonipat"],
    "age":[23,22,22]
})

new_gf1 = {"Name":"GF","city":"city2","age":22}
df.iloc[len(df.index)] = new_gf1


dir_data = "data"

os.makedirs(dir_data,exist_ok=True)

file_path = os.path.join(dir_data,"sample_data.csv")

df.to_csv(file_path,index=False)

print(f"CSV file is saved: {file_path}")