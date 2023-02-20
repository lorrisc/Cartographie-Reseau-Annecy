import pandas as pd
import re

excel_file = "address.xlsx"
df = pd.read_excel(excel_file)

csv_rows = []

for index, row in df.iterrows():
    node_id = row["id"]
    edges = str(row["edges"])

    if pd.isna(edges) or edges == "" or edges == "nan":
        continue

    edges_list = re.split('[,.]', edges)
    
    for edge in edges_list:
        csv_rows.append({"Source": node_id, "Target": edge.strip()})
        
csv_df = pd.DataFrame(csv_rows)
csv_df.to_csv("edges.csv", index=False)
