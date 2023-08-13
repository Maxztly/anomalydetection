import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from adtk.data import validate_series
from adtk.visualization import plot
from adtk.detector import *

data = pd.read_csv("FILE NAME CSV")
data["Date"] = pd.to_datetime(data["Date"])
data = data.set_index("Date")
data = data["Mean"]

iqr_detector = InterQuartileRangeAD(c=1)
anomalies = iqr_detector.fit_detect(data)
plot(data, anomaly=anomalies, anomaly_color="red", anomaly_tag="marker")
plt.show()


