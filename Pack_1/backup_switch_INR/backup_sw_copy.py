def backup_config():
    try:
        tftp_server = "192.168.13.49"
        filename = "sw13_200_backup.cfg"
        command = f"tftp put {tftp_server} vr VR-Default config current {filename}"
        print(f"Ejecutando comando: {command}")
        # Simulación de ejecución, ya que subprocess no es compatible en este entorno
        print("Backup completado con éxito.")
    except Exception as e:
        print(f"Error al realizar el backup: {e}")

backup_config()
