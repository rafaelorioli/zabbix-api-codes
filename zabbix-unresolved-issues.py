from zabbix_api import ZabbixAPI
import time

zapi = ZabbixAPI(server="http://localhost")
zapi.login("admin","zabbix")

triggers = zapi.trigger.get ({
	"output": ["description", "lastchange"], 
	"selectHosts": ["hostid", "host"], 
	"selectLastEvent": ["eventid", "acknowledged", "objectid", "clock", "ns"], 
	"sortfield" : "lastchange", 
	"monitored": "true", 
	"only_true": "true", 
	"maintenance":  "false", 
	"expandDescription": True,
	"filter":{"value":1}
})
print("Host - Descricao - Ultima alteracao - Idade")
print("===========================================")

for trigger in triggers:
	nome_host = trigger["hosts"][0]["host"]


	idade = time.time() - float (trigger["lastchange"])
	get_dia = "{0.tm_yday}".format(time.gmtime(idade))

	dia = int(get_dia) - 1
	duracao = "dias {0.tm_hour} horas {0.tm_min} minutos".format(time.gmtime(idade))

	ultima_alteracao = time.strftime("%d/%m/%y %H:%M:%S",
		time.localtime(float(trigger["lastchange"])))

	print("{0} - {1} - {2} - {3}".format(nome_host, trigger["description"], 
										ultima_alteracao, dia, duracao))