#LOCAL 
ssh-keygen
sh-copy-id user@hostname

# AFTER LOGIN OR DIRECTLY
chmod 755 ~
logout



#PROBLEMS
/etc/init.d/ssh restart
systemctl restart sshd

# MAKE SURE

## LOACAL
chmod 644 ~/.ssh/id_rsa.pub
chmod 600 ~/.ssh/id_rsa
### Check ###
ssh-add
ssh-add -l

## SERVER
chmod 700 /home/uname/
chmod 700 /home/uname/.ssh/authorized_keys
chmod 600 /home/uname/.ssh/authorized_keys
