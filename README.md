# Ansible
**$How to use the Dynamic Inventory Script Generator$**\
Copy the same code from DynamicInventory.py and create a python script on your ansible master mode with copying this code.\
Make Sure to replace the "access key" , "secret access key" and "dafault region" as per your need. \
You can run the script and validate if it's producing the correct ip address in json format. \
Once script is ready , run usual ansible playbook run command work on this dynamic inventory file.For example: \
**ansible-playbook -i /etc/ansible/getEc2.py InstallNginx.yml --private-key=/etc/ansible/privateKeyName.pem**
