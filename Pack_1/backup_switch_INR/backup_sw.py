import cli
import datetime

# Configuración del servidor TFTP y el archivo de respaldo
TFTP_SERVER = "192.168.13.49"
BACKUP_FILENAME = f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.cfg"
LOG_FILE = "/usr/local/cfg/backup_log.txt"

def log_message(message):
    """Registra mensajes en un archivo de log en el switch."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"{timestamp} - {message}\n")

def backup_switch():
    """Realiza el respaldo y lo envía al servidor TFTP."""
    try:
        log_message("🔄 Iniciando respaldo...")

        # Guardar configuración en la memoria del switch
        cli.execute("save configuration")
        log_message("✅ Configuración guardada correctamente.")

        # Enviar respaldo al servidor TFTP
        cli.execute(f"upload configuration {TFTP_SERVER} {BACKUP_FILENAME}")
        log_message(f"✅ Respaldo subido exitosamente a {TFTP_SERVER} como {BACKUP_FILENAME}.")

    except Exception as e:
        error_message = f"❌ Error en el respaldo: {e}"
        log_message(error_message)

# Ejecutar el respaldo
backup_switch()
