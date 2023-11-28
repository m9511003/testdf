
import numpy as np
import pandas as pd
import time


def getData(filePath):
    print('시간이 10초 걸림....')
    time.sleep(10)
    df = pd.read_csv(filePath)
    return df
