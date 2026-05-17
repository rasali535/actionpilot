import paramiko

host = "216.128.155.55"
user = "root"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(host, username=user, password="3K%mcAGZV8eZ.sCr", timeout=10)
    
    # Let's run a directory check first to find the correct project folder
    stdin, stdout, stderr = ssh.exec_command("ls -la /root")
    print("Files in /root:\n", stdout.read().decode())
    
    # Determine the directory
    # Based on git repository redirect, it moved to vantage_point
    # We will try both
    print("--- Running git pull and docker compose rebuild ---")
    cmd = """
    cd /root/actionpilot || cd /root/vantage_point
    git pull
    sudo docker compose up --build -d backend
    """
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print("STDOUT:", stdout.read().decode('utf-8', errors='ignore'))
    print("STDERR:", stderr.read().decode('utf-8', errors='ignore'))
    
except Exception as e:
    print(f"Failed: {e}")
finally:
    ssh.close()
