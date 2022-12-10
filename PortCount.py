import napalm 
import json
from interface_data import Utilities
import credentials


class DevicePortCount:
    def __init__(self, username, password, hostname):
        self.username = username
        self.password = password 
        self.hostname = hostname 

    def get_raw_data(self):
        ssh_connect = napalm.get_network_driver('ios')
        test_connection= ssh_connect(hostname=self.hostname, username=self.username, password=self.password)
        try:
            test_connection.open()
            interface_data = test_connection.get_interfaces()
            utils = Utilities(interface_data)
            port_grouping = utils.CheckPortSpeed()
            returned_data = utils.Port_Group_Func(port_grouping)
            # try:
            #     device_data = test_connection.get_facts()
            #     print(device_data)
            # except:
            #     raise ValueError('An error has occured Please try again')
            # os_ver = device_data['os_version']
            # hw_model = device_data["model"]
            # get_hostname = device_data["hostname"]
            # list_os_data = os_ver.split(',')
            # list_os_data = list_os_data[1]
            # get_hostname, list_os_data, hw_model,
            return  returned_data, 
        except AssertionError as error:
            print(error)

def device_list():
    device_inventory = {}
    for ips in credentials.host_ips:
        obj =  DevicePortCount(hostname=ips, username=credentials.username,password=credentials.password)
        data = obj.get_raw_data()
        device_inventory[ips] =  data
    return device_inventory

json_data = device_list()
print(json.dumps(json_data, indent=1))



