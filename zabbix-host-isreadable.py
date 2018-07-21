from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://localhost/zabbix")
zapi.login("admin","zabbix")

read = zapi.host.isreadable([
	10254
])

if read:
	print("Host {0} disponivel para leitura".format(read))
else:
	print("host {0} nao disponivel para leitura".format(read))