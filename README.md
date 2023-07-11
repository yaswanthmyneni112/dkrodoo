# dkrodoo
Quick start odoo with docker for testing

If docker is not installed then install it
## Install docker-compose for ubuntu 20.04

```
sudo apt update
sudo apt install docker.io
sudo apt install docker-compose
```
verify that the docker compose is installed by running
```
sudo docker-compose version
```

## Clone repo and run odoo
create a new folder
goto that folder from terminal and run

```
git clone https://github.com/bharat0to/dkrodoo.git
cd dkrodoo
sudo docker-compose up
```

## Open Odoo shell for python interpreter
run below command in the terminal
```
docker exec -it dkrodoo_web_1 odoo shell -d sulaba
```

## Debug odoo addon
To debug the application run odoo server with debugger
```
docker-compose -f docker-compose.debug.yml up
```
Once the server got started press F5 in vscode editor then the debugger gets attached to the odoo server

You can set breakpoints in the vscode to debug

