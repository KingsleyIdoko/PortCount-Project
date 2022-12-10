dsat = {'GigabitEthernet1': '1G_Port', 'GigabitEthernet2': '1G_Port', 'GigabitEthernet3': '1G_Port', 'GigabitEthernet4': '1G_Port'}

from itertools import groupby
from operator import itemgetter


class Utilities: 
    def __init__(self, data):
        self.data = data
    
    def CheckPortSpeed(self):
        interface_type = {}
        for key, value in self.data.items():    
            if value['speed'] == 100.00:
                interface_type[key] = 'FE_Port'
            elif value['speed'] == 1000.00:
                interface_type[key] = '1G_Port'
            elif value['speed'] == 10000.00:
                interface_type[key] = '10G_Port'
            else:
                interface_type[key] = '100G_Port'
        return interface_type

    def Port_Group_Func(self, kwargs):
        Port_Group = {}
        for k, v in groupby(sorted(kwargs.items(), key=itemgetter(1)), itemgetter(1)):
            Port_Group[k] = len(list(map(itemgetter(0), v)))
            return Port_Group
        



    
