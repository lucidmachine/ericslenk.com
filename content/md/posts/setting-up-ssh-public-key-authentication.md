{:title "Setting Up SSH Public Key Authentication", :date "2019-02-25", :tags ["ssh" "cryptography" "keys" "linux"], :description "Do you have a computer to compute on, but it's all the way over there? Use SSH, stupid! With keys!"}


Do you have a computer to compute on, but it's *all* the way over *there*? Use SSH, stupid! With keys!

# 0. Have Access to a Remote Computer with an SSH Server
Before you can set up key-based authentication you should have:

* A remote computer.
* A user account with a password on that remote computer.
* A SSH server installed on that remote computer which is:
    * Configured to allow your remote user account to log in and
    * **Running**

These all sound obvious, but I almost never have all 5 at once, so there you go.

For our examples we'll assume that your local user is `groundcontrol` on the local host named `earth`, trying to log in as the remote user `majortom` to the remote host `tincan`.

# 1. Generate Your Key Pair
First you need to make a key pair. Run `ssh-keygen` to create a public and private key.

```text
groundcontrol@earth:~$ ssh-keygen

Enter file in which to save the key (/home/groundcontrol/.ssh/id_rsa): /home/groundcontrol/.ssh/tincan
Enter passphrase (empty for no passphrase): [redacted]
Enter same passphrase again: [redacted]
Your identification has been saved in /home/groundcontrol/.ssh/tincan.
Your public key has been saved in /home/groundcontrol/.ssh/tincan.pub.
The key fingerprint is:
SHA256:6qhMpF/b62Zt63i/SVH6fZqqzB7uQc2kyryIwvR+FsQ groundcontrol@earth
```

Here we've elected to make a key pair with the name of our remote machine, `tincan`. It lives in the `.ssh` subdirectory of the user `groundcontrol`'s home directory. The private key stays on your local machine, and the public key gets sent to your remote machine.

`ssh-keygen` will request an optional passphrase, which it will use to encrypt your private key when it's not being used. Use one.

# 2. Upload the Public Key to your Remote Machine
Now you must tell your remote SSH server that `majortom` can be authenticated using your private key, `/home/groundcontrol/.ssh/tincan`. To do so, you must append the contents of your public key, `/home/groundcontrol/.ssh/tincan.pub`, to the `authorized_keys` file for your remote user, `/home/majortom/.ssh/authorized_keys`. We'll do this using `ssh-copy-id`, but you can accomplish the same task with `scp` or some other file transfer utility if it's not available.

```text
groundcontrol@earth:~$ ssh-copy-id -i ~/.ssh/tincan.pub majortom@192.168.1.2

/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/groundcontrol/.ssh/tincan.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
majortom@192.168.1.2's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'majortom@129.168.1.2'"
and check to make sure that only the key(s) you wanted were added.
```

# 3. Configure an SSH Host
Would you rather type `ssh tincan` or `ssh majortom@192.168.1.2` to log in to your remote machine? To accomplish the former, append the following to the file `/home/groundcontrol/.ssh/config`:

```text
Host tincan
    user majortom
    HostName 192.168.1.2
    IdentityFile /home/groundcontrol/.ssh/tincan
```

The Host value, `tincan`, is the alias for your remote machine. The user value is the name of the user on the remote machine you'll log in as, `majortom`. The HostName can be either a DNS name or an IP address for the remote machine. Here it's a local IP, `192.168.1.2`. The IdentityFile is the path to the private key you'll use to authenticate to the server, `/home/groundcontrol/.ssh/tincan`.

# 4. Verify
Now go log in to your remote box.

```text
groundcontrol@earth:~$ ssh tincan

Enter passphrase for key '/home/groundcontrol/.ssh/tincan': [redacted]

majortom@tincan:~$ cat ~/.ssh/authorized_keys
```

** DONE. **