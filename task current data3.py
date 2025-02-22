from datetime import date, timedelta
dt = date.today() - timedelta(1)
tomorrow = date.today() + timedelta(1)
print('Todays Date :', date.today())
print('Yesterdays Date:', dt)
print('Tomorrows Date:',  tomorrow)