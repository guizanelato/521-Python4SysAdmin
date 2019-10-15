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

commands = [

    'sudo apt update -y',
    'sudo apt install -y apache2',
    'sudo service apache2 start',
    'echo "{}" > /home/ubuntu/index.html'.format(arquivo),
    'sudo mv /home/ubuntu/index.html /var/www/html/index.html'

]

for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    if stdout.channel.recv_exit_status() == 0 :
        print(stdout.read().decode())
    else:
        print(stderr.read().decode())

client.close()
