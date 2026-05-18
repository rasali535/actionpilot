import paramiko

host = "216.128.155.55"
user = "root"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(host, username=user, password="3K%mcAGZV8eZ.sCr", timeout=10)
    stdin, stdout, stderr = ssh.exec_command("cat /root/vantage_point/.env")
    print("--- Remote .env ---")
    print(stdout.read().decode('utf-8', errors='ignore'))
except Exception as e:
    print(f"Failed: {e}")
finally:
    ssh.close()
