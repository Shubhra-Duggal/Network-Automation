# Public Key Infrastructure

PKI overcomes the limitations of passwords. Keys are more secure than passwords. 

A key is a unique string of binary data that forms a digital identity. An SSH identity uses a pair of keys, one private and one public. The public key is  placed freely onto SSH server machines. During authentication, the SSH client and server exchange information about the user's private and public key. If they match, your identity is proven, and authentication succeeds.

The following setup is required for SSH:
1. Private key and a public key is required, which is known as a key pair. 
2. A secret passphrase is also needed to protect the private key.
3. Installation of public key on an SSH server machine.

## Key Management

### Generation
A key pair is supposed to be generated, consisting of a private key and a public key. The private key is the digital identity that sits on the client machine. The public key is present on the server machine.    
SSH key-gen program is used. It works differently in SSH1, SSH2 and OpenSSH. When you invoke it an RSA key pair is generated and a passphrase is asked.  

The OpenSSH version of ssh-keygen can produce either RSA or DSA keys. RSA is default. Its operation is similar to that of SSH1.  

Normally, ssh-keygen performs all necessary mathematics to generate a key. It creates your local SSH directory (~/.ssh for OpenSSH) if it doesn't already exist, and stores the private and public components of the generated key there. By default, their names are identity and identity.pub (OpenSSH) or id_dsa_1024_a and id_dsa_1024_a.pub (SSH2).    


