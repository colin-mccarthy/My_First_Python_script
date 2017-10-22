import paramiko
import time

ip = '192.168.161.2'
username = 'colin-mccarthy'
password = 'omited'

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, username=username, password=password)
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(5000)

remote_conn.send("conf t \n")
time.sleep(3)

remote_conn.send("int range gi0/1-24 \n")
time.sleep(3)

remote_conn.send("no ip access-group 100 in \n")
time.sleep(3)

remote_conn.send("exit \n")
time.sleep(3)

remote_conn.send("no access-list 100 deny udp any any eq bootpc \n")
time.sleep(3)

remote_conn.send("no access-list 100 permit ip any any \n")
time.sleep(3)

remote_conn.send("exit \n")
time.sleep(3)

remote_conn.send("wr mem \n")
time.sleep(3)

output = remote_conn.recv(65535)
print output
remote_conn_pre.close()
