## S W TO PKEY U C ACCESS TM
ssh-keygen -t rsa -b 4096

# Check Keys
cd ~/.ssh

#send keys to remote server
scp ~/.ssh/id_rsa.pub uname@host:/home/uname/.ssh/id_rsa.pub


#REMOTE MECHINE
cat ~/.ssh/id_rsa.pub >> authorized_keys

# Check
cat ~/.ssh/authorized_keys

# SET PERMISSIONS
chmod 700 ~/.ssh/

chmod 600 ~/.ssh/*
