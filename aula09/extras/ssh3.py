import paramiko 

key = paramiko.RSAKey.from_private_key_file('guilherme.pem') 

client = paramiko.SSHClient() 
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

opts = {
    'hostname': '52.33.174.218',
    'username': 'ubuntu',
    'pkey':  key

}

client.connect(**opts)

with open('index.html', 'r') as f:
    arquivo = f.read()
# arquivo = ''.join(line for line in f.readlines())

uri = 'https://github.com/LucasRicciardi/dashboard.git'


commands = [
    'sudo apt update && sudo apt install -y python3-pip',
    'git clone {} '.format(uri),
    'pip3 install -r dashboard/requirements.txt',
    'python3 dashboard dashboard/app &'
    
]

for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    if stdout.channel.recv_exit_status() == 0 :
        print(stdout.read().decode())
    else:
        print(stderr.read().decode())

client.close()
