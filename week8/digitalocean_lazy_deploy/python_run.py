#!usr/bin/env python3

import os
import server_init
import remote_variable_writer


print ('#######################################################################')
print ('#                             %%%%%%%     %%%%%%    %%%%              #')
print ('#                         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%          #')
print ('# ____________          %%%%%|      %%%%%%%%%           |%%%%         #')
print ('# |          |         %%%%%%|                          |%%%%%        #')
print ('# |   Greg   |  >----->  %%%%|    Greg CLOUD Server.... |%%%%%%%      #')
print ('# |__________|          %%%%%|                          |%%%%%%       #')
print ('#    T    T               %%%| %%             %%%%%%%   |%%%%         #')
print ('# -------------           %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%         #')
print ('# -------------                  %%%%%   %%%%%%%%%%%   %%             #')
print ('#                                                                     #')
print ('#_____________________________________________________________________#')
print ('                                                                       ')
print ('                         ENTER PARAMETERS.....                         ')
print ('_______________________________________________________________________')
print('')


username = input('Please specify a lowercase username: ')
password = input('Please specify a SECURE password: ')
email = input('Please specify an email address: ')
ip_address = input('Please specify the ip for the server: ')
ssh_port = input('Please specify a non-default port number for your SSH Connection: ')
vps_name = input('Please specify the server name: ')
http_port = input('Please specify a non-default port number for your HTTP connection:')

# Make project directory & write config files
os.system('mkdir {}'.format(vps_name))
remote_variable_writer.write_configs(username, password, email, 
                                     ip_address, ssh_port, vps_name)
variable_here = input()
# Create credentials, create new user, send keys
server_init.start_server(username, password, ip_address)
# Update the server
variable_here = input()
os.system('ssh root@{} "bash -s" < ./update.sh'.format(ip_address))
# Install programs
variable_here = input()
os.system('ssh root@{} "bash -s" < ./install.sh'.format(ip_address))
# Configure said programs from stock config script
variable_here = input()
os.system('ssh root@{ip_address} "bash -s" < ./{vps_name}/{vps_name}_config.sh'.format(ip_address=ip_address,vps_name=vps_name))
# Clone github files if we want to
git_import = input('Would you like to clone from github? (y/n) ')
if git_import == 'y':
    filepath = input('What would you like to add (filepath)? ')
    try:
        clone_cmd='ssh -p {} {}@{} "git clone {}"'.format(ssh_port,username,
                                                          ip_address,filepath)
        os.system(clone_cmd)
    except:
        print("I'm sorry, that was link doesn't exist. \
\n\nYou can manually add files later with the 'git clone' command.\n")
choose_to_connect = input('Would you like to connect now? (y/n) ')
if choose_to_connect == 'y':
    try:
        os.system('ssh -p {} {}@{}'.format(ssh_port,username,ip_address))
    except:
        print('Connection error')

