import paramiko

host = "216.128.155.55"
user = "root"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(host, username=user, password="3K%mcAGZV8eZ.sCr", timeout=10)
    
    # 1. Run paper status command
    print("--- Executing paper status ---")
    cmd_status = "sudo docker exec -e KRAKEN_API_KEY=E+9/rW06Nb3mOuRxS1betW9IWXfW37tTw5UGhBkx1TrU7rcsqGMvJtkO -e KRAKEN_API_SECRET=yLKQKk4gpLNt1BCVaFo95HnkU2gw4wbHr+TXcY/24M3GEjPUnWlvFNKeyuD+pOvgyH+oEgh+Y4Pq7a8knmeUOA== actionpilot-api kraken paper status"
    stdin, stdout, stderr = ssh.exec_command(cmd_status)
    print("STDOUT:", stdout.read().decode('utf-8', errors='ignore').encode('ascii', errors='replace').decode('ascii'))
    print("STDERR:", stderr.read().decode('utf-8', errors='ignore').encode('ascii', errors='replace').decode('ascii'))
    
    # 2. Run paper buy command
    print("--- Executing paper buy of AAPL/USD ---")
    cmd_buy = "sudo docker exec -e KRAKEN_API_KEY=E+9/rW06Nb3mOuRxS1betW9IWXfW37tTw5UGhBkx1TrU7rcsqGMvJtkO -e KRAKEN_API_SECRET=yLKQKk4gpLNt1BCVaFo95HnkU2gw4wbHr+TXcY/24M3GEjPUnWlvFNKeyuD+pOvgyH+oEgh+Y4Pq7a8knmeUOA== actionpilot-api kraken paper buy AAPL/USD 10 --yes"
    stdin, stdout, stderr = ssh.exec_command(cmd_buy)
    print("STDOUT:", stdout.read().decode('utf-8', errors='ignore').encode('ascii', errors='replace').decode('ascii'))
    print("STDERR:", stderr.read().decode('utf-8', errors='ignore').encode('ascii', errors='replace').decode('ascii'))
    
except Exception as e:
    print(f"Failed: {e}")
finally:
    ssh.close()
