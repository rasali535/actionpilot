import paramiko
import sys

host = "216.128.155.55"
user = "root"

print(f"Deploying to {host}...")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Use the password to ensure connection works without local key mapping issues
    ssh.connect(host, username=user, password="3K%mcAGZV8eZ.sCr", timeout=10)
    print("Connected via SSH. Executing deployment script...")
    
    # We will run the init script which updates docker, clones the repo, and runs docker compose
    cmd = "curl -sSL https://raw.githubusercontent.com/rasali535/vantage_point/main/vultr-init.sh | sudo bash"
    
    stdin, stdout, stderr = ssh.exec_command(cmd)
    
    # Print the output in real-time
    for line in iter(stdout.readline, ""):
        print(line, end="")
    
    err = stderr.read().decode()
    if err:
        print("STDERR:", err)
        
    print("\n✅ Deployment initiated successfully!")
    
except Exception as e:
    print(f"Failed to connect or deploy: {e}")
finally:
    ssh.close()
