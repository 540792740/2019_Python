import pandas as pd

columns = ['PEID', '姓名', '检查日期']

save_file = pd.DataFrame(columns=columns)

save_file.to_csv('mm.csv', index=False, encoding="utf-8")