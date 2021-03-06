import os
import sys
import subprocess
import argparse

# Constants
CUR_USER = os.getlogin()
PLATFORM = sys.platform

if PLATFORM == "darwin":
    PRIV_SSH_DIR = "/Users/%s/.ssh" % (CUR_USER)
elif PLATFORM == "linux":
    PRIV_SSH_DIR = "/home/%s/.ssh" % (CUR_USER)


def key_present():
    """Checks to see if there is an RSA already present. Returns a bool."""
    if "id_rsa" in os.listdir(PRIV_SSH_DIR):
        return True
    else:
        return False

print(key_present())

def show(msg):
    """Local print() function."""
    print(msg)


def gen_key():
    """Generate a SSH Key."""
    os.chdir(PRIV_SSH_DIR)
    if key_present():
        show("A key is already present.")
    else:
        # Genarate private key
        subprocess.call('ssh-keygen', shell=True)


def push_key(user, host, port=22):
    """Push a SSH Key to a remote server."""
    print(PRIV_SSH_DIR)
    os.chdir(PRIV_SSH_DIR)
    if key_present():
        if PLATFORM == "linux":
            command = "ssh-copy-id -p %s %s@%s" % (port, user, host)
            print(command)
            subprocess.call(command, shell=True)
        elif PLATFORM != "linux":
            if "ssh-copy-id" in os.listdir("/usr/local/bin"):
                show("SSH key found. Pushing key to remote server")
                command = "ssh-copy-id -p %s %s@%s" % (port, user, host)
                print(command)
                subprocess.call(command, shell=True)
            else:
                show(
                    "ssh-copy-id required for Mac Users. Use --help for more information.")
    else:
        show("A SSH key is required. Run script again with action set as GenKey")

def main():
    """Start of script."""
    parser = argparse.ArgumentParser(
        description="Uses the ssh-keygen and ssh-copy-id commands found on Mac and Linux systems. Mac Users will need to install ssh-copy-id before attempting to use this script. If you do not have Homebrew installed, please visit https://github.com/beautifulcode/ssh-copy-id-for-OSX for the install. If you do have Homebrew installed, run the command brew install ssh-copy-id in Terminal.")
    parser.add_argument("action", choices=[
                        "GenKey", "PushKey"], help="Action to be preformed")
    parser.add_argument("-u", "--user", help="SSH username")
    parser.add_argument("-s", "--host", help="IP or FQDN of server")
    parser.add_argument("-p", "--port", help="SSH port number")
    args = parser.parse_args()
    if (args.action == "GenKey"):
        gen_key()
    elif (args.action == "PushKey"):
        if args.user and args.host:
            if args.port:
                push_key(args.user, args.host, args.port)
            else:
                push_key(args.user, args.host)
        else:
            show("-u and -s are required for action PushKey. Use -h for Help.")

if __name__ == "__main__":
    main()
