import os
import subprocess
from datetime import datetime

DB_NAME = "hasta_kayit"
DB_USER = "root"
DB_PASSWORD = "1234"  # ← VİRGÜL KALDIRILDI
BACKUP_DIR = "backups"
LOG_FILE = "backup.log"

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_file = f"{BACKUP_DIR}/backup_{timestamp}.sql"

os.makedirs(BACKUP_DIR, exist_ok=True)

try:
    result = subprocess.run(
        ["mysqldump", "-u", DB_USER, f"-p{DB_PASSWORD}", DB_NAME],
        stdout=open(backup_file, 'w'),
        stderr=subprocess.PIPE,
        text=True
    )

    size = os.path.getsize(backup_file)
    with open(LOG_FILE, "a") as log:
        if result.returncode == 0:
            log.write(f"{timestamp} - SUCCESS - {backup_file} - {size} bytes\n")
        else:
            log.write(f"{timestamp} - ERROR - {result.stderr.strip()}\n")

except Exception as e:
    with open(LOG_FILE, "a") as log:
        log.write(f"{timestamp} - EXCEPTION - {str(e)}\n")
