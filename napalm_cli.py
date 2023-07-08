from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_cli
from nornir_utils.plugins.functions import print_result
from pprint import pprint
from nornir_inspect import nornir_inspect

nr=InitNornir(config_file="config.yaml")

result=nr.run(napalm_cli,commands=["show run","show run | i snmp"])

#print_result(result)

pprint(result["R1"][0].result["show run | i snmp"])