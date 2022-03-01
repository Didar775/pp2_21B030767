
from datetime import datetime, date,timedelta

today=date.today()


print(f"Yesterday is: {today-timedelta(days=1)}")
print(f"Today was: {today}")
print(f"Tomorrow will be: {today+timedelta(days=1)}")

