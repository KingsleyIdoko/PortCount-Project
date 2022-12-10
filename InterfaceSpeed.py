import netmiko

cred_login = {
    'device_type': 'cisco_ios',
    'host': '192.168.8.29',
    'username': 'cisco',
    'password': 'cisco123',
    'secret': 'cisco123',
    'port': 22,
}

ssh = netmiko.ConnectHandler(**cred_login)
result = ssh.send_command('show interfaces | i BW')
print(result)