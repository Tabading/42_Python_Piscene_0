
# Files to turn in: format_ft_time.py

# Allowed functions: time, datetime or any other library that allows to receive
# the date. Write a script that formats the dates this way.
# Expected output:
# $> python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$
# $>
import time, datetime

unix_time = time.time()
date = datetime.datetime.now()
print(f'Seconds since January 1, 1970: {unix_time:,} or {unix_time:.2e} in scientific notation')
print(date.strftime("%b %d %Y"))