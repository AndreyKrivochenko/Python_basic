time = '215477'
time = int(time)

hours = time // 3600
minute = (time - hours * 3600) // 60
seconds = time % 60

print(f'{hours:02d}:{minute:02d}:{seconds:02d}')
