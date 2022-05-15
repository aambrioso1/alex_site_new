#Information on creating and executing shell scripts
#https://www.javatpoint.com/steps-to-write-and-execute-a-shell-script

#This script is used to updated the alex_site_new respository

#Consider adding commands to navigate to the correct directory
#cd /apps/alex_site_new
git pull
systemctl stop alex_site_new
systemctl start alex_site_new
systemctl enable alex_site_new
service nginx restart