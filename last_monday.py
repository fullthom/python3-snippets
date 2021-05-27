DATE_FORMAT = "%Y-%m-%d"
import datetime
ds = "2021-05-17"
dt_ds = datetime.datetime.strptime(ds, DATE_FORMAT)
delta = (dt_ds.weekday() - 2) % 7
dt_ds =dt_ds - datetime.timedelta(days=delta)
print(dt_ds.strftime(DATE_FORMAT))
