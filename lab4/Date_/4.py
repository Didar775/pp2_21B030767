from datetime import datetime

past=list(map(int,input().split()))
future=list(map(int,input().split()))

past_date = datetime(past[0], past[1],past[2])
future_date = datetime(future[0], future[1], future[2])


differenc = (future_date - past_date)

total_seconds = differenc.total_seconds()
b=int(total_seconds)
print(total_seconds)
print(b/3600/24)
