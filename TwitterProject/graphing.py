#####################################################################################
############################### Second Part #########################################
#####################################################################################


import csv
import numpy as np
import pandas as pd

cr = csv.reader(open("test.csv","rb"))

mon = 0
tue = 0
wed = 0
thu = 0
fri = 0
sat = 0
sun = 0
for row in cr:
	if row[0].lower() == "mon":
		mon = mon + 1
	if row[0].lower() == "tue":
		tue = tue + 1
	if row[0].lower() == "wed":
		wed = wed + 1
	if row[0].lower() == "thu":
		thu = thu + 1
	if row[0].lower() == "fri":
		fri = fri + 1
	if row[0].lower() == "sat":
		sat = sat + 1
	if row[0].lower() == "sun":
		sun = sun + 1

# Testing Purposes
# print mon
# print tue
# print wed
# print thu
# print fri
# print sat
# print sun

#####################################################################################
############################### Third Part ##########################################
#####################################################################################

import numpy as np
import matplotlib.pyplot as plt


n_groups = 7

tweets = (mon, tue, wed, thu, fri, sat, sun)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.5

opacity = 1
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, tweets, bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config,
                 label='UIUC')


plt.xlabel('Day of the Week')
plt.ylabel('Number of Tweets')
plt.title('Tweets having the term UIUC in them')
plt.xticks(index + bar_width, ('Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'))
plt.legend()

plt.tight_layout()
plt.show()
