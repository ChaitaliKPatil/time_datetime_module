from time import*
start_time=time()
struct=localtime(start_time)
print('Countdown starts at: ',strftime('%X',struct))
i=10
while i>-1:
    print(i)
    i-=1
    sleep(1)
end_time=time()
diff=round(end_time-start_time)
print('time taken by loop to play completely: ',diff)