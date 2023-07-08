from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_ping
from nornir_utils.plugins.functions import print_result
from nornir_inspect import nornir_inspect
import pprint
nr = InitNornir(config_file="config.yaml")
result = nr.run(task=napalm_ping,dest='172.16.138.14')
nornir_inspect(result)
print_result(result["R1"])