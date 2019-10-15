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

#leitura de saídas

stdin, stdout, stderr = client.exec_command('ls -la')

if stdout.channel.recv_exit_status() == 0 :
    print(stdout.read().decode())
else:
    print(stderr.read().decode())


stdin, stdout, stderr = client.exec_command('read x \n echo $x')

stdin.write(input('Digite um nome:') + '\n')
stdin.flush()

if stdout.channel.recv_exit_status() == 0 :
    print(stdout.read().decode())
else:
    print(stderr.read().decode())


client.close()
