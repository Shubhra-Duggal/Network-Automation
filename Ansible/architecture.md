# Architecture
<p align = "center">
<img src = "https://user-images.githubusercontent.com/42912140/131787288-1e2286b2-ca01-4f52-b1d7-44f79cec0c3e.png">
</p>     

> Note: Windows is not supported as Ansible engine. Python is needed on the machines for Ansible to work.

## Ansible Master
![Screenshot 2021-09-02 at 10 55 25 AM](https://user-images.githubusercontent.com/42912140/131787301-02eae3c8-c6e3-46bf-8e5b-9d1fb65d4959.png)     


![Screenshot 2021-09-02 at 11 41 53 AM](https://user-images.githubusercontent.com/42912140/131795496-d99bdeb2-1acb-48d5-8c04-ce843269de37.png)      


Ansible is installed on the Mac OS machine using [yum](/yum.md) or [pip](/pip.md) command.

![Screenshot 2021-09-02 at 12 16 14 PM](https://user-images.githubusercontent.com/42912140/131795735-13d3c3ef-3123-4485-8a2b-acbe619f46c4.png)     


## Ansible Client

![Screenshot 2021-09-02 at 10 53 30 AM](https://user-images.githubusercontent.com/42912140/131787430-15eed2b0-f32a-4498-ae23-2a3cc3957ac6.png)      

Ansible client is agentless hence, it does not require any installation at the client side. Ansible uses SSH to push required changes to the client. This reduces the need of python interpreter. Ansible uses the push model for configuration management.

## SSH Connection


![Screenshot 2021-09-02 at 12 12 39 PM](https://user-images.githubusercontent.com/42912140/131795466-cc3722e7-1893-419d-9bf7-8c1d449fe246.png)


SSH connection between the engine and client using OpenSSH. A key is created on the Ansible engine and push it to the Ansible client for automatic authentication.

---
