from datetime import datetime, timedelta, date

today=date.today()

n_days_ago=today-timedelta(days=5)
print(f"Today is: {today}")
print(f"5 days ago day was: {n_days_ago}")
