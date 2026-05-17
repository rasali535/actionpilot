import paramiko

host = "216.128.155.55"
user = "root"
password = "3K%mcAGZV8eZ.sCr"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(host, username=user, password=password, timeout=10)
    print("Connected to Vultr VM!")
    
    # We will try both paths
    cmd = """
    cd /root/actionpilot || cd /root/vantage_point
    pwd
    if [ -f .env ]; then
        echo "Found .env file. Updating TRADING_PAIR to BTC/USD..."
        # Replace TRADING_PAIR=... with TRADING_PAIR=BTC/USD in .env
        sed -i 's|^TRADING_PAIR=.*|TRADING_PAIR=BTC/USD|g' .env
        echo "Updated .env:"
        grep "^TRADING_PAIR=" .env
        
        echo "Rebuilding and restarting docker backend service..."
        sudo docker compose up --build -d backend
    else
        echo "ERROR: .env file not found in current directory!"
    fi
    """
    
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print("STDOUT:")
    print(stdout.read().decode('utf-8', errors='ignore'))
    print("STDERR:")
    print(stderr.read().decode('utf-8', errors='ignore'))
    
except Exception as e:
    print(f"Failed: {e}")
finally:
    ssh.close()
