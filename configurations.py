from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nornir = InitNornir(config_file='nornir_config.yml')


commands = ("show ip int br | exclude unassigned",
            "show ip arp",
            "show ip route",
            "show ip protocols"
            )


def triage(task):
    for command in commands:
        task.run(task=netmiko_send_command, command_string=command)


results = nornir.run(task=triage)
print_result(results)
