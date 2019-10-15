from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://localhost/zabbix")
zapi.login("admin","zabbix")

hosts = zapi.host.get({
	"output": [
		"hostid",
		"name"
	]
})

interfaces = zapi.hostinterface.get({
	"output":[
		"hostid",
		"ip",
		"type"
	]
})

#For para percorrer host para verificar id
for host in hosts:
	for interface in interfaces:
		if interface["hostid"] == host["hostid"]:
			print("hostid: {0} - name: {1} - IP: {2} - Tipo de interface: {3}"\
				.format(host["hostid"], host["name"], interface["ip"], interface["type"]))
