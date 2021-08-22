# Public Key Authentication

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

![Screenshot 2021-08-17 at 1 53 16 AM](https://user-images.githubusercontent.com/42912140/130352774-6d32c2ae-e1bf-4335-9f22-65b9ddb58429.png)

The public and private keys go into the ~/.ssh folder on the client machine.    
![Screenshot 2021-08-22 at 4 55 02 PM](https://user-images.githubusercontent.com/42912140/130353315-766e0dca-dacc-4474-8682-cda2485ec6de.png)



### Copying the Key to Server

After the key has been generated the ssh-copy-id command is used to install it as an authorised key on the server. Now, the server grants access without a password.

![Screenshot 2021-08-17 at 1 53 40 AM](https://user-images.githubusercontent.com/42912140/130352802-eb70f95b-2f41-4cec-b9df-ed64fcb0f1db.png).    

This logs into the server host, and copies keys to the server, and configures them to grant access by adding them to the authorized_keys file. For OpenSSH, the entry is created in the file ~/.ssh/authorized_keys.    
Note: The private key should never be copied to another machine.   

![Screenshot 2021-08-22 at 5 23 01 PM](https://user-images.githubusercontent.com/42912140/130354103-18d23e2b-f8d0-4db4-8120-d0778808ce6e.png).  

Now the connection can be made without using the password to the server machine.   

![Screenshot 2021-08-22 at 5 22 26 PM](https://user-images.githubusercontent.com/42912140/130354122-254d881d-e8ac-4a87-9edf-0771293c8a8d.png)




