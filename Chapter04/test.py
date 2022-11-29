import csv
import re

import usecsv
import usecsv2

# 너같은 경우에는 C:\Users\user\Desktop\files\Python\.conda\Lib
data = usecsv.opencsv("popSeoul.csv")

re = usecsv2.switch(data)
print(re)