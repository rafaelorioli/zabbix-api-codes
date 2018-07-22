from zabbix_api import ZabbixAPI
from operator import itemgetter

zapi = ZabbixAPI(server="http://localhost/zabbix")
zapi.login("admin","zabbix")

chave = "system.cpu.util[,user]"
titulo = "TOP 10 CPU"
dicionario = {}

totalHost = 0
totalValorItem = 0
mediaHost = 0
contador = 0

itens = zapi.item.get({

	"filter":{
		"key_": chave
	},
	"selectHost": [
		"hostid",
		"host"
	],
	"monitored": True

})

for x in itens:
	historico = zapi.history.get({
		"hostids": x["hostid"],
		"itemids": x["itemid"],
		"history": 0,
		"output": "extend",
	})

	for y in historico:
		totalHost = len(historico)
		totalValorItem += float(y["value"])
		mediaHost = float("%.2f".format(totalValorItem / totalHost))

	dicionario[x["hosts"][0]["host"]] = {"media": mediaHost}
ordem = sorted(dicionario.items(),key=itemgetter(1), reverse=True)

barra = "========================================================="
print(titulo.center(len(barra)))
print(barra)
print("{0:2} | {1:22} | {2:4}".format(" #", "Host", ("%")))
print("-----------------------------------------------------------")

for z in ordem[0:10]:
	contador += 1
	print("{0:2} | {1:22} | {2:4}".format(contador, z[0], z[1], ["media"]))

print(barra)
