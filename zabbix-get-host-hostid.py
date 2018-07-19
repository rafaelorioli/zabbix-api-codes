from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="https://localhost/zabbix")

zapi.login("admin","zabbix")

hosts = zapi.host.get({
		"output": [
			"hostid",
			"host"
		]
	})

for x in hosts:
	print(x["hostid"], "-", x["host"])
