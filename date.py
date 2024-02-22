#problem 1
import datetime
from datetime import timedelta
now = datetime.datetime.now()
fda = now - timedelta(days = 5)
print(fda.strftime("%A"))
print(fda.strftime("%x"))
