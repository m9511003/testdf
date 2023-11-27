
import numpy as np
import pandas as pd


def getData(filePath):
    df = pd.read_csv(filePath)
    return df
