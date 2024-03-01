from datetime import datetime
date_string = '01.01.25 12:10:3.234567'
date_dt = datetime.strptime(date_string, '%m.%d.%y %H:%M:%S.%f')
print(date_dt)