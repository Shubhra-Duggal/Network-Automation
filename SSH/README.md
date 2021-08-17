# Secure Shell

Introduction Again.

## Setup for SSH server and SSH client
Explain what client and server signify. [Link](ssh_setup.md)

## Talk about different kinds of authetication in SSH
 The OpenSSH SSH client supports SSH protocol 2.
 
 
 Available authentication methods are:
 1. GSSAPI-based authentication
 2. Host-based authentication: If the client machine is listed in /etc/hosts.equiv or /etc/shosts.equiv on the server machine, and the client name is the same on both sides, or if the files ~/.rhosts or ~/.shosts exist in the client's home directory on the server machine and contain a line containing the client and client machine name on that server machine, the user is considered for login.  Additionally, the server must be able to verify the client's host key for login to be permitted. This closes security holes due to IP spoofing, DNS spoofing, and routing spoofing.
 3. [Public key authentication](public_key_authenication.md): Asymmetric keys are used to autheticatethe clients. The client generates a public-private key pair. RSA is used to implement this method of authentication. 
 4. Certificate authentication: A certification authority issues signed certificates for identification. It is a variation of public key authentication.
 5. Challenge-response authentication:  The server sends an arbitrary "challenge" text, and prompts for a response. BSD Authentication???
 6. [Password authentication](simple_ssh.md): The client is prompted for a password for the host.


* SSH automatically maintains and checks a database containing identification for all hosts it has ever been used with.
* Host keys are stored in ~/.ssh/known_hosts in the user's home directory.  
* Additionally, the file /etc/ssh/ssh_known_hosts is automatically checked for known hosts.  
* Any new hosts are automatically added to the user's file.  
* If a host's identification ever changes, ssh warns about this and disables password authentication to prevent server spoofing or man-in-the-middle attacks, which could otherwise be used to circumvent the encryption.  
* The StrictHostKeyChecking option can be used to control logins to machines whose host key is not known or has changed.
* When the user's identity has been accepted by the server, the server either executes the given command in a non-interactive session or, if no command has been specified, logs into the machine and gives the user a normal shell as an interactive session.
* All communication with the remote command or shell will be automatically encrypted.
* If an interactive session is requested, ssh by default will only request a pseudo-terminal (pty) for interactive sessions when the client has one. The flags -T and -t can be used to override this behaviour.
* If a pseudo-terminal has been allocated the user may use the escape characters noted below.
* If no pseudo-terminal has been allocated, the session is transparent and can be used to reliably transfer binary data.  
* On most systems, setting the escape character to ''none'' will also make the session transparent even if a tty is used.
* The session terminates when the command or shell on the remote machine exits and all X11 and TCP connections have been closed.


