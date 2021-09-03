# Secure Shell

Introduction Again.

## Setup for SSH server and SSH client
Explain what client and server signify. [Link](ssh_setup.md)

## Protocol vs Product
SSH is a protocol that can be implemented by a variety of products to secure communication between end machines. OpenSSH (used here) is a product from OpenBSD project which implements both versions of the protocol- SSH-1 and SSH-2.
 
 
 ## Authentication
 1. [Public key authentication](public_key_authentication.md): Asymmetric keys are used to autheticatethe clients. The client generates a public-private key pair. RSA is used to implement this method of authentication. 
 2. [Password authentication](ssh_setup.md): The client is prompted for a password for the host.


References: https://www.ssh.com

--- 
