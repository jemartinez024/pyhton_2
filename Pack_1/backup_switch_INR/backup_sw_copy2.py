"""Funciona"""

import exsh

def backup_config():
    tftp_server = "192.168.13.49"
    filename = "sw13_200.cfg"
    command = "tftp put " + tftp_server + " vr VR-Default config current " + filename
    exsh.clicmd(command, True)

backup_config()
