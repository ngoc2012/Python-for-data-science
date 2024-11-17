import time
epoch = time.time()
today = time.strftime('%b %d %Y', time.gmtime(epoch))
print(f"Seconds since January 1, 1970: \
{epoch:,.4f} or {epoch:.2e} in scientific notation")
print(f"{today}")
