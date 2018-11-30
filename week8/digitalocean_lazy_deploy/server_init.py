#!/usr/bin/env python3

################################################################################
#                                %%%%%%%     %%%%%%    %%%%                    #
#                            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                #
# ____________             %%%%%|      %%%%%%%%%           |%%%%               #
# |          |            %%%%%%|                          |%%%%%              #
# |   Greg   |  >-------->  %%%%|    Greg CLOUD Server.... |%%%%%%%            #
# |__________|             %%%%%|                          |%%%%%%             #
#    T    T                  %%%| %%             %%%%%%%   |%%%%               #
# -------------              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%               #
# -------------                     %%%%%   %%%%%%%%%%%   %%                   #
#                                                                              #
#______________________________________________________________________________#
#                                                                              #
# You will need the following information:                                     #
# ~ your email address (email)                                                 #
# ~ your server's internet protocol address (ip_address)                       #
# ~ your server's name (server_name)                                           #
#                                                                              #
# Be advised:                                                                  #
# ~ username must be a string that is not "root"                               #
# ~ password should be a string that is longer than eight characters           #
# ~ port must be an integer that is between 1024 and 65535                     #
#                                                                              #
################################################################################
import os

def start_server(username, password, ip_address):
    # Create credentials and nanorc...
    os.system('./create_credentials.sh "{username}" "{password}"'.format(username=username, password=password, ip_address=ip_address))
    os.system('scp -o "StrictHostKeyChecking no" .credentials root@{ip_address}:'.format(username=username, ip_address=ip_address))
    # Connect to the new server...
    os.system('ssh root@{ip_address} "bash -s" < ./create_user.sh "{username}"'.format(ip_address=ip_address, username=username))
    os.system('scp ~/.ssh/id_rsa.pub root@{ip_address}:/home/{username}/.ssh/authorized_keys'.format(ip_address=ip_address, username=username))
    return 'User setup complete!'

