# dkrodoo
Quick start odoo with docker for testing

## Install docker-compose

```
mkdir -p ~/.docker/cli-plugins/
curl -SL https://github.com/docker/compose/releases/download/v2.3.3/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose
chmod +x ~/.docker/cli-plugins/docker-compose
```

## Clone repo and run odoo
create a new folder
goto that folder from terminal and run

```
git clone https://github.com/bharat0to/dkrodoo.git
sudo docker compose up
```