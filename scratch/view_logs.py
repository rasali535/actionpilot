import paramiko

host = "216.128.155.55"
user = "root"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(host, username=user, password="3K%mcAGZV8eZ.sCr", timeout=10)
    
    # Check docker containers
    print("--- Docker Containers ---")
    stdin, stdout, stderr = ssh.exec_command("sudo docker ps -a")
    out_containers = stdout.read().decode('utf-8', errors='ignore').encode('ascii', errors='replace').decode('ascii')
    print(out_containers)
    
    # Check backend API logs
    print("--- Vantage Point API Logs ---")
    stdin, stdout, stderr = ssh.exec_command("sudo docker logs --tail 100 actionpilot-api")
    out_logs = stdout.read().decode('utf-8', errors='ignore').encode('ascii', errors='replace').decode('ascii')
    print(out_logs)
    
except Exception as e:
    print(f"Failed: {e}")
finally:
    ssh.close()
