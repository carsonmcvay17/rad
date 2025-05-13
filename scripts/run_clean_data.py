# imports
import pandas as pd
from radcode.clean_data import Data

data = '/Users/carsonmcvay/desktop/gradschool/research/rad/data/large_dataset/run_data_meta.csv'
model = Data()
model.clean_data(data)