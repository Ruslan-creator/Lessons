seconds = int(input('Enter your time in sec: '))

hh = seconds//3600
mm = (seconds%3600)//60
ss = (seconds%3600)%60

print(f'{hh:02d}:{mm:02d}:{ss:02d}')