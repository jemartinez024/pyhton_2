# -*- coding: ascii -*-
import exsh

def backup_config():
    try:
        # Definir el nombre del archivo
        filename = "sw13_200_backup.cfg"

        # Comandos para obtener la configuración detallada
        commands = [
            "show configuration"
        ]
        
        # Guardar la salida de cada comando en el archivo
        with open(filename, "w") as f:
            for command in commands:
                # Ejecutar el comando en el switch y capturar la salida
                output = exsh.clicmd(command)
                f.write(f"### Output of '{command}' ###\n")
                f.write(output)
                f.write("\n\n")
        
        print("Backup completado con exito y detalles añadidos al archivo.")
    except Exception as e:
        print("Error al realizar el backup: " + str(e))

backup_config()
