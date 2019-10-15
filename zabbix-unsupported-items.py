from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://localhost/zabbix")
zapi.login("admin","zabbix")

itens = zapi.item.get({
	"output": "extend",
	"filter": {
		"state": 1
	}
})
print("===============================================")
print("ID Host	-	ID Item 	-	Nome 	- 	Erro")
print("===============================================")

#For para Itens id e erro 
for item in itens:
	print(item["hostid"], item["itemid"], item["name"], item["error"])

print("===============================================")
print("Total de itens nao suportados: {0}".format(len(itens)))
