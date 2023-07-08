from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir_inspect import nornir_inspect
import pprint
cmd="show run"
nr = InitNornir(config_file="config.yaml")
result = nr.run(task=netmiko_send_command,command_string=cmd)
print_result(result)