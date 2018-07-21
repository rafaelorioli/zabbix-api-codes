'''
Cira um host chamado servidor linux, adiciona ao grupo linux servers,
o id do grupo e 2, associado ao template OS Linux, cujo o id e o 10001
O host ja entra habilitado, caso nao queria habilitar, mude o status para 1

'''

from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://localhost/zabbix")
zapi.login("admin","zabbix")

host = zapi.host.create({
	"host": "Servidor linux",
	"status": 0,
	"interfaces": [
		{
			"type": 1,
			"main": 1,
			"useip": 1,
			"ip": "192.168.1.1",
			"dns": "",
			"port": 10050

		}
	],
	"groups": [{
		"groupid": 2
	}],
	"template": [{
		"templateid": 10001,
	}]
})

print("--- Host criado com sucesso ---")
print("Host ID: {0}".format(host["hostids"][0]))
