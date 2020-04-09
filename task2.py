
seconds = int(input("Введите время в секундах.\n"))

seconds: int = seconds
minutes: int = seconds / 60
hours: int = (seconds / 60) / 60

result = '{0}:{1}:{2}'.format(seconds, minutes, hours)

print(result)
