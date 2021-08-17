# Network Programming


Network automation has become a necessary aspect of Software Design Networking. Leveraging this, troubleshooting and configuration of systems can be automated to reduce cost.

## SSH Connection
Introduction to SSH and how it works and link to file of [SSH](SSH).

## Python Modules


### Paramiko
[Paramiko](/Paramiko/paramiko.md) is a python implementation of the SSHv2 protocol. Paramiko simplifies the SSHv2 interaction with the remote device. Paramiko is only focused on SSHv2 and provides both client and server operations. Paramiko is the low-level SSH client behind the high-level automation framework Ansible for its network modules. 

### Pexpect

[Pexpect](/Pexpect/pexpect.md) is one the python modules that is used to control other applications. It 'spawns' a child application and responds to the expected pattern of queries, like a human user would do. It can be used for SSH, FTP, Telnet, etc. by automating scripts.


## Puppet



## Ansible
Ansible has SSH as the transport protocol. It has a decentralised, agentless architecture. It is operated in as a push model. Earlier it was used to run as hoc commands on servers, but now is able to automate tasks using 'playbooks' that perform idempotent tasks. These playbooks are written in YAML.
