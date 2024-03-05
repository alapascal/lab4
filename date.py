#problem 1
import datetime
from datetime import timedelta
now = datetime.datetime.now()
fda = now - timedelta(days = 5)
print(fda.strftime("%A"))
print(fda.strftime("%x"))

#problem 2
from datetime import datetime, timedelta
now = datetime.now()
ytd = now - timedelta(days = 1)
tmr = now + timedelta(days = 1)
print(ytd.strftime("%A"), end =' ')
print(ytd.strftime("%x"))
print(tmr.strftime("%A"), end =' ')
print(tmr.strftime("%x"))

#problem 3
import datetime
now = datetime.datetime.now()
wtm = now.replace(microseconds = 0)
print(wtm)

#problem 4
import datetime
from datetime import timedelta
date1 = datetime.datetime.now()
date2 = date1 - timedelta(days = 1)
dif = (date1 - date2).total_seconds()
print(dif)
