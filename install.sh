#!/bin/bash

# Turn off SSH Timeout
cat >> /etc/ssh/sshd_config << EOL

TCPKeepAlive yes
ClientAliveInterval 30
ClientAliveCountMax 99999
EOL

cat /etc/ssh/sshd_config


cat >> /etc/ssh/ssh_config << EOL
ServerAliveInterval 100
EOL

cat /etc/ssh/ssh_config

service ssh restart
# End turn off SSH Timeout

# Install Build Tools, git, and Python 3.6 #
sudo apt-get update
sudo apt-get -y install build-essential libssl-dev git mongodb virtualenv
sudo apt-get -y install python3-pip --upgrade
pip3 install --upgrade pip

# Add a user
adduser pgaines937
usermod -aG sudo pgaines937
su pgaines937
cd ~

# Install nvm
wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash
source ~/.profile

# Install Node.js
nvm install 7.7.2

# Install Meteor.js
curl https://install.meteor.com/ | sh

# Install mongoclient
git clone https://github.com/rsercano/mongoclient.git
cd mongoclient
meteor npm install

# Configure startmc command to start mongoclient easily
cd ~
cat >> startmc.sh << EOL
#!/bin/bash
cd mongoclient
meteor --port 3000
EOL

cat startmc.sh

cat >> .bash_aliases << EOL
alias startmc='bash startmc.sh'
EOL

cat .bash_aliases
source ~/.profile

# Install and Configure Scrapy
cd ~
virtualenv -p python3 scrapy_venv
cd scrapy_venv
sudo pip install --upgrade setuptools ez_setup
sudo pip install --upgrade scrapy pymongo newspaper3k textblob pandas
git clone https://github.com/pgaines937/news_articles.git 

mongo
use articles
exit