import pandas as pd
import json

data = ""

with open("node.txt") as data_file:
    df = pd.read_json(data_file)
    df.to_csv("data.csv", index = False, columns=["FIELD_1", "FIELD_2", "FIELD_3", "FIELD_4", "FIELD_5", "FIELD_6"])