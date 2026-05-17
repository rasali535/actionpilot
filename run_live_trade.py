import paramiko

host = "216.128.155.55"
user = "root"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(host, username=user, password="3K%mcAGZV8eZ.sCr", timeout=10)
    
    # 1. Initialize paper account if needed
    print("--- Initializing Paper Account if needed ---")
    cmd_init = "sudo docker exec -e KRAKEN_API_KEY=E+9/rW06Nb3mOuRxS1betW9IWXfW37tTw5UGhBkx1TrU7rcsqGMvJtkO -e KRAKEN_API_SECRET=yLKQKk4gpLNt1BCVaFo95HnkU2gw4wbHr+TXcY/24M3GEjPUnWlvFNKeyuD+pOvgyH+oEgh+Y4Pq7a8knmeUOA== actionpilot-api kraken paper init --balance 100000 --currency USD --yes"
    ssh.exec_command(cmd_init)
    
    # 2. Execute paper buy
    print("--- Executing paper buy ---")
    cmd_buy = "sudo docker exec -e KRAKEN_API_KEY=E+9/rW06Nb3mOuRxS1betW9IWXfW37tTw5UGhBkx1TrU7rcsqGMvJtkO -e KRAKEN_API_SECRET=yLKQKk4gpLNt1BCVaFo95HnkU2gw4wbHr+TXcY/24M3GEjPUnWlvFNKeyuD+pOvgyH+oEgh+Y4Pq7a8knmeUOA== actionpilot-api kraken paper buy BTC/USD 0.1 --yes -o json"
    stdin, stdout, stderr = ssh.exec_command(cmd_buy)
    print("STDOUT:", stdout.read().decode('utf-8', errors='ignore').encode('ascii', errors='replace').decode('ascii'))
    print("STDERR:", stderr.read().decode('utf-8', errors='ignore').encode('ascii', errors='replace').decode('ascii'))
    
    # 3. Check paper status to see if balance changed
    print("--- Verifying paper status ---")
    cmd_status = "sudo docker exec -e KRAKEN_API_KEY=E+9/rW06Nb3mOuRxS1betW9IWXfW37tTw5UGhBkx1TrU7rcsqGMvJtkO -e KRAKEN_API_SECRET=yLKQKk4gpLNt1BCVaFo95HnkU2gw4wbHr+TXcY/24M3GEjPUnWlvFNKeyuD+pOvgyH+oEgh+Y4Pq7a8knmeUOA== actionpilot-api kraken paper status -o json"
    stdin, stdout, stderr = ssh.exec_command(cmd_status)
    print("STDOUT:", stdout.read().decode('utf-8', errors='ignore').encode('ascii', errors='replace').decode('ascii'))
    print("STDERR:", stderr.read().decode('utf-8', errors='ignore').encode('ascii', errors='replace').decode('ascii'))
    
except Exception as e:
    print(f"Failed: {e}")
finally:
    ssh.close()
