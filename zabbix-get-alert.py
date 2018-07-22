'''
Conta o numero de vezes que o alerta foi disparado
Com esse mesmo metado, podemos verificar quantas vezes
o agent foi disparado, basta trocar o ssh port agent
'''

from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://localhost/zabbix")
zapi.login("admin","zabbix")

alerts = zapi.alert.get({
	"output": "extend",
	"search": {
		"messages": "ssh"
	},
	"actionsids": "7",
	"countOutput": "True",
})

print("Numero de vezes que a acao foi disparada {0}".format(alerts))