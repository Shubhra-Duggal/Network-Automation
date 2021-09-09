# Network Automation


Network automation has become a necessary aspect of Software Design Networking. Leveraging this, troubleshooting and configuration of systems can be automated to reduce cost.

## SSH Connection
[Secure Shell](SSH) is a protocol which is used to encrypt communication between client and server, and even perform authentication using public key cryptography. Implementation of SSH are available in almost all of the operating systems. Although SSH stands for Secure Shell, it is not a shell in the traditional sense of the word. It creates a tunnel to run a shell with end to end encryption between the two machines. 

## Python Modules


### Paramiko
[Paramiko](/Paramiko/paramiko.md) is a python implementation of the SSHv2 protocol. Paramiko simplifies the SSHv2 interaction with the remote device. Paramiko is only focused on SSHv2 and provides both client and server operations. Paramiko is the low-level SSH client behind the high-level automation framework Ansible for its network modules. 

### Pexpect

[Pexpect](/Pexpect/pexpect.md) is one the python modules that is used to control other applications. It 'spawns' a child application and responds to the expected pattern of queries, like a human user would do. It can be used for SSH, FTP, Telnet, etc. by automating scripts.

### Fabric
[Fabric](Fabric/README.md) is a library and set of command line tools that execute commands on a remote server. Fabric uses an SSH connection to connect to the server and then executes commands against it. Fabric is used in composing using Python modules and executing by the Fabric command line. 


## Puppet



## Ansible
[Ansible](Ansible) has SSH as the transport protocol. It has a decentralised, agentless architecture. It is operated in as a push model. Earlier it was used to run as hoc commands on servers, but now is able to automate tasks using 'playbooks' that perform idempotent tasks. These playbooks are written in YAML.
