import datetime

print("datetime.datetime.utcnow() = {}".format(datetime.datetime.utcnow()))
print("datetime.datetime.utcnow().timestamp() = {}".format(datetime.datetime.utcnow().timestamp()))
print("datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc) = {}".format(datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)))
print("datetime.datetime.now() = {}".format(datetime.datetime.now()))
print("datetime.datetime.now().timestamp() = {}".format(datetime.datetime.now().timestamp()))
print("datetime.datetime.now().replace(tzinfo=datetime.timezone.utc) = {}".format(datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)))
print("datetime.datetime.now().replace(tzinfo=datetime.timezone.utc).timestamp() = {}".format(datetime.datetime.now().replace(tzinfo=datetime.timezone.utc).timestamp()))
