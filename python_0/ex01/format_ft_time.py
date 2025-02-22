from datetime import datetime 

now = datetime.now()
old = datetime(1970, 1, 1)
delta = (now - old).total_seconds()

print(f"Seconds since January 1, 1970: {delta:,} or {delta:.2e} in scientific notation")
print (now.strftime('%b %d %Y'))