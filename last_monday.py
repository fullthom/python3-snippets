DATE_FORMAT = "%Y-%m-%d"
import datetime
ds = "2021-05-10"
dt_ds = datetime.datetime.strptime(ds, DATE_FORMAT)
dt_ds =dt_ds - datetime.timedelta(days=dt_ds.weekday())
print(dt_ds.strftime(DATE_FORMAT))
