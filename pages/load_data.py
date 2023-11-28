import pandas as pd

df_call_for_service = pd.read_csv("./Data/SF_FD.csv")
fire_incidents = pd.read_csv("./Data/Fire_Incidents.csv", low_memory = False)
fire_violations = pd.read_csv("./Data/Fire_Violations_20231011.csv")