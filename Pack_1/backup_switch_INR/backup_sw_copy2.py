# -*- coding: ascii -*-
import exsh

def backup_config():
    tftp_server = "192.168.13.49"
    filename = "sw11_200.cfg"
    temp_file = "/tmp/backup_config.cfg"  # Cambiado a /tmp/

    # Comandos para capturar detalles de la configuracion
    commands = [
        "show configuration"  # Configuracion completa del switch
    ]
    # Crear un archivo temporal con la configuracion
    with open(temp_file, "w") as f:
        for command in commands:
            output = exsh.clicmd(command, capture=True)
            f.write("### Output of '" + command + "' ###\n")
            f.write(output + "\n\n")

    # Enviar el archivo al servidor TFTP
    tftp_command = "upload configuration " + tftp_server + " " + filename + " vr VR-Default"
    exsh.clicmd(tftp_command, True)

    print("Backup completado y enviado al servidor TFTP.")

backup_config()
backup_config()