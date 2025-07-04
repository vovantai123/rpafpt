import os
import pandas as pd

def ghi_vao_excel_pandas(data_dict, excel_path="output.xlsx"):
    data_dict = {k: str(v) for k, v in data_dict.items()}
    new_row = pd.DataFrame([data_dict])
    if os.path.exists(excel_path):
        df = pd.read_excel(excel_path, dtype=str)
        df = pd.concat([df, new_row], ignore_index=True)
    else:
        df = new_row
    with pd.ExcelWriter(excel_path, engine='openpyxl', mode='w') as writer:
        df.to_excel(writer, index=False)
    print(f"✅ Ghi Excel xong: {excel_path}")
