# Digitalocean Lazy Deploy

Base deployment script for DO droplet configuration (minus API calls for droplet creation), modular for ease of future project customization
* Configures a new Digital Ocean droplet running Ubuntu 16.04 with a new user, non-default ssh port, firewalld, fail2ban, ntp, and nignx
* Includes option to clone a project from a github repo for rapid deployment
TODOs: 
* Include DO API call to create a droplet and get its IP, making entire process manual
* Support pip installation of a requirements.txt file for python projects, and virtual environment creation
* Allow uwsgi setup/congifuration to automate full project deployment with Flask for small-scale python projects