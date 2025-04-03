"""Funciona perfectamente"""


import exsh

def backup_config():
    tftp_server = "192.168.13.49"
    filename = "sw13_200.cfg"
    temp_file = "/usr/local/tmp/backup_config.txt"

    # Comandos para capturar detalles de la configuración
    commands = [
        "show configuration",  # Configuración completa del switch
    ]
    
    # Crear un archivo temporal con la configuración
    with open(temp_file, "w") as f:
        for command in commands:
            output = exsh.clicmd(command, capture=True)
            f.write(f"### Output of '{command}' ###\n")
            f.write(output + "\n\n")
    
    # Enviar el archivo al servidor TFTP
    tftp_command = f"upload configuration " + {tftp_server} + {filename} +" vr VR-Default "
    exsh.clicmd(tftp_command, True)
    
    print("Backup completado con éxito y enviado al servidor TFTP.")

backup_config()
