import numpy as np
import pandas as pd
import re
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

# path = 'C:\\Users\\abcja\\Documents\\Coding\\Data\\Twitter Sentiment\\training.1600000.processed.noemoticon.csv'
# df = pd.read_csv(path)

# cols = [1,2,3,4]
# df.drop(df.columns[cols], axis=1, inplace=True)

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)