# Simple SSH

## Steps to SSH into computer on local network

Explain the setup for 2 (link to where the setup has been explained) machines.

Explain how SSH server has been setup and what it is.





![Screenshot 2021-08-15 at 8 27 13 PM](https://user-images.githubusercontent.com/42912140/129575124-7fd2f4bd-99ff-4382-89a9-0d72e91dd95e.png)


Check that the server is up and running

![Screenshot 2021-08-16 at 7 26 41 PM](https://user-images.githubusercontent.com/42912140/129575325-c6759575-3397-49d2-83a2-6ab3653adf82.png)



The SSH client setup on Mac OS. Explain about it and configuration on the system.
![Screenshot 2021-08-16 at 7 27 53 PM](https://user-images.githubusercontent.com/42912140/129575502-c69d0c4c-2e7d-4b46-83d4-18cc5b243ee3.png)


The SSH connection from Mac machine to Ubuntu machine

The hostname and ip address is determined

Hostname->
![Screenshot 2021-08-16 at 7 31 46 PM](https://user-images.githubusercontent.com/42912140/129576125-d6de2205-5227-4b97-9c06-febf9766b8e3.png)

IP Address ->
![Screenshot 2021-08-15 at 8 25 02 PM](https://user-images.githubusercontent.com/42912140/129575204-5fb7308c-98d4-43b9-b28f-b790ec5cfb04.png)




![Screenshot 2021-08-16 at 7 29 01 PM](https://user-images.githubusercontent.com/42912140/129575695-32632541-e740-4154-a688-2538566dc6dd.png)

## Talk about different kinds of authetication in SSH
 The OpenSSH SSH client supports SSH protocol 2.
 
 
 Available authentication methods are:
 1. GSSAPI-based authentication
 2. Host-based authentication: If the machine the user logs in from is listed in
     /etc/hosts.equiv or /etc/shosts.equiv on the remote machine, and the user names are the same on both
     sides, or if the files ~/.rhosts or ~/.shosts exist in the user's home directory on the remote machine
     and contain a line containing the name of the client machine and the name of the user on that machine,
     the user is considered for login.  Additionally, the server must be able to verify the client's host
     key (see the description of /etc/ssh/ssh_known_hosts and ~/.ssh/known_hosts, below) for login to be
     permitted.  This authentication method closes security holes due to IP spoofing, DNS spoofing, and
     routing spoofing.  [Note to the administrator: /etc/hosts.equiv, ~/.rhosts, and the rlogin/rsh proto-
     col in general, are inherently insecure and should be disabled if security is desired.]
 3. [Public key authentication](public_key_authenication.md): The scheme is based on public-key cryptography, using
     cryptosystems where encryption and decryption are done using separate keys, and it is unfeasible to
     derive the decryption key from the encryption key.  The idea is that each user creates a public/pri-
     vate key pair for authentication purposes.  The server knows the public key, and only the user knows
     the private key.  ssh implements public key authentication protocol automatically, using one of the
     DSA, ECDSA, Ed25519 or RSA algorithms.  The HISTORY section of ssl(8) contains a brief discussion of
     the DSA and RSA algorithms.
 4. A variation on public key authentication is available in the form of certificate authentication:
     instead of a set of public/private keys, signed certificates are used.  This has the advantage that a
     single trusted certification authority can be used in place of many public/private keys.  See the CER-
     TIFICATES section of ssh-keygen(1) for more information.
 5. Challenge-response authentication
 6. Password authentication

The file ~/.ssh/authorized_keys lists the public keys that are permitted for logging in.
The user creates his/her key pair by running ssh-keygen(1).  This stores the private key in
     ~/.ssh/id_dsa (DSA), ~/.ssh/id_ecdsa (ECDSA), ~/.ssh/id_ed25519 (Ed25519), or ~/.ssh/id_rsa (RSA) and
     stores the public key in ~/.ssh/id_dsa.pub (DSA), ~/.ssh/id_ecdsa.pub (ECDSA), ~/.ssh/id_ed25519.pub
     (Ed25519), or ~/.ssh/id_rsa.pub (RSA) in the user's home directory.  The user should then copy the
     public key to ~/.ssh/authorized_keys in his/her home directory on the remote machine.  The
     authorized_keys file corresponds to the conventional ~/.rhosts file, and has one key per line, though
     the lines can be very long.  After this, the user can log in without giving the password.

     

     The most convenient way to use public key or certificate authentication may be with an authentication
     agent.  See ssh-agent(1) and (optionally) the AddKeysToAgent directive in ssh_config(5) for more
     information.

     Challenge-response authentication works as follows: The server sends an arbitrary "challenge" text,
     and prompts for a response.  Examples of challenge-response authentication include BSD Authentication
     (see login.conf(5)) and PAM (some non-OpenBSD systems).
     
     Finally, if other authentication methods fail, ssh prompts the user for a password.  The password is
     sent to the remote host for checking; however, since all communications are encrypted, the password
     cannot be seen by someone listening on the network.

     ssh automatically maintains and checks a database containing identification for all hosts it has ever
     been used with.  Host keys are stored in ~/.ssh/known_hosts in the user's home directory.  Addition-
     ally, the file /etc/ssh/ssh_known_hosts is automatically checked for known hosts.  Any new hosts are
     automatically added to the user's file.  If a host's identification ever changes, ssh warns about this
     and disables password authentication to prevent server spoofing or man-in-the-middle attacks, which
     could otherwise be used to circumvent the encryption.  The StrictHostKeyChecking option can be used to
     control logins to machines whose host key is not known or has changed.

     When the user's identity has been accepted by the server, the server either executes the given command
     in a non-interactive session or, if no command has been specified, logs into the machine and gives the
     user a normal shell as an interactive session.  All communication with the remote command or shell
     will be automatically encrypted.

     If an interactive session is requested ssh by default will only request a pseudo-terminal (pty) for
     interactive sessions when the client has one.  The flags -T and -t can be used to override this behav-
     iour.

     If a pseudo-terminal has been allocated the user may use the escape characters noted below.

     If no pseudo-terminal has been allocated, the session is transparent and can be used to reliably
     transfer binary data.  On most systems, setting the escape character to ``none'' will also make the
     session transparent even if a tty is used.

     The session terminates when the command or shell on the remote machine exits and all X11 and TCP con-
     nections have been closed.

     
