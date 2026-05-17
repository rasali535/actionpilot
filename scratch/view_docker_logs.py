import paramiko

host = "216.128.155.55"
user = "root"
password = "3K%mcAGZV8eZ.sCr"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(host, username=user, password=password, timeout=10)
    print("Connected to Vultr VM!")
    
    # View the last 50 lines of logs for actionpilot-api
    cmd = "sudo docker logs --tail 50 actionpilot-api"
    stdin, stdout, stderr = ssh.exec_command(cmd)
    
    print("DOCKER LOGS:")
    print(stdout.read().decode('utf-8', errors='ignore').encode('ascii', errors='ignore').decode())
    print("DOCKER ERRORS:")
    print(stderr.read().decode('utf-8', errors='ignore').encode('ascii', errors='ignore').decode())
    
except Exception as e:
    print(f"Failed: {e}")
finally:
    ssh.close()
