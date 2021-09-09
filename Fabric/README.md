# Fabric

The fabric module is installed on Ubuntu using the following command.

```bash
sudo apt-get install fabric
```
![Screenshot 2021-09-09 at 11 24 58 AM](https://user-images.githubusercontent.com/42912140/132630891-8c3a5a3a-b5ea-4499-97db-dcd97b3eaafc.png)


The man pages of fab command are reviewed to summarise how to use of fabric.
![Screenshot 2021-09-09 at 11 23 42 AM](https://user-images.githubusercontent.com/42912140/132630881-2f3e356f-0ff1-4fc8-971f-fe8ff222bfe6.png)

A simple command is run to test the fabric running on the Ubuntu machine. The [SSH](/SSH) connection using public key authentication of the between the machines (Mac OS and Ubuntu) has been setup.
```bash
fab -H shubhraduggal@172.16.117.1 -- uname -a
```

The -H option indicates to the list of machines on which the following command has to be run. The command return the kernal information of the target machine (Mac OS).

![Screenshot 2021-09-09 at 11 27 31 AM](https://user-images.githubusercontent.com/42912140/132631147-1d781773-1c69-4f9c-bd04-8b3fb644dfc6.png)


