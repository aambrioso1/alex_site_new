#Information on creating and executing shell scripts
#https://www.javatpoint.com/steps-to-write-and-execute-a-shell-script

#This script is used to updated the alex_site_new respository

#Consider adding commands to navigate to the correct directory
#cd /apps/alex_site_new
#Why is log file coming up when I execute this shell script?
git pull
systemctl sudo stop alex_site_new
systemctl sudo start alex_site_new
systemctl sudo enable alex_site_new
service sudo nginx restart