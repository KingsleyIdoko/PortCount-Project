from operator import itemgetter
from itertools import groupby
import re
import interface_data

items1 = {'GigabitEthernet1': '1G_Port', 'GigabitEthernet2': '1G_Port', 'TenGigabitEthernet3': '10G_Port', 'TenGigabitEthernet4': '10G_Port'}

from itertools import groupby
from operator import itemgetter

for k, v in groupby(sorted(items1.items(), key=itemgetter(1)), itemgetter(1)):
    print(k, list(map(itemgetter(0), v)))

