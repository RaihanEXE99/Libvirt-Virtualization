sudo passwd root

sudo nano /etc/ssh/sshd_config
PermitRootLogin yes

sudo service ssh restart
