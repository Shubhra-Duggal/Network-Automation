# Secure Shell

Introduction Again.

## Setup for SSH server and SSH client
Explain what client and server signify. [Link](ssh_setup.md)

## Talk about different kinds of authetication in SSH
 The OpenSSH SSH client supports SSH protocol 2. Mention we have a OpenSSH setup
 
 
 Available authentication methods are:
 1. [Public key authentication](public_key_authentication.md): Asymmetric keys are used to autheticatethe clients. The client generates a public-private key pair. RSA is used to implement this method of authentication. 
 2. Certificate authentication: A certification authority issues signed certificates for identification. It is a variation of public key authentication.
 3. Challenge-response authentication:  The server sends an arbitrary "challenge" text, and prompts for a response. BSD Authentication???
 4. [Password authentication](simple_ssh.md): The client is prompted for a password for the host.


References: https://www.ssh.com

--- 
