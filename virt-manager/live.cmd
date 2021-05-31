https://gist.github.com/ishad0w/788555191c7037e249a439542c53e170

sudo apt-get install virt-manager
sudo apt update
sudo apt install qemu-kvm libvirt-daemon-system
sudo adduser $USER libvirt
newgrp libvirt
