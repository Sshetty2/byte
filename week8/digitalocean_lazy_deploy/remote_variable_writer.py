#
# TODO Add more specifics, maybe ascii art
#
#
# Variables to be edited:
#
# <os_username>    <os_password>    <email_address>
#
# <vps_ip_addr>    <defined_ssh_port>    <vps_name>
#
# MASTER file to copy >>>>> template_server_config.sh
#
# Copying to <vps_name>_init_config.sh
# 
# TODO Multiple copies for each install???
# 

import os


def write_configs(username, password, email, ip_address, ssh_port, vps_name):
    os.system("sed 's/<os_username>/{username}/g' config_generic_server.sh > {vps_name}/config1_config.sh".format(username=username, vps_name=vps_name))
    os.system("sed 's/<os_password>/{password}/g' {vps_name}/config1_config.sh > {vps_name}/config2_config.sh".format(password=password, vps_name=vps_name))
    os.system("sed 's/<email_address>/{email}/g' {vps_name}/config2_config.sh > {vps_name}/config3_config.sh".format(email=email, vps_name=vps_name))
    os.system("sed 's/<vps_ip_addr>/{ip_address}/g' {vps_name}/config3_config.sh > {vps_name}/config4_config.sh".format(ip_address=ip_address, vps_name=vps_name))
    os.system("sed 's/<defined_ssh_port>/{ssh_port}/g' {vps_name}/config4_config.sh > {vps_name}/config5_config.sh".format(ssh_port=ssh_port, vps_name=vps_name))
    os.system("sed 's/<vps_name>/{vps_name}/g' {vps_name}/config5_config.sh > {vps_name}/{vps_name}_config.sh".format(vps_name=vps_name))


