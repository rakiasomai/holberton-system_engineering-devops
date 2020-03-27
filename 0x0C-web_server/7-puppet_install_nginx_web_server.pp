# Install ngnix with puppet and configurate a server

exec {'update':
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'sudo apt-get -y update',
}

exec {'install':
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'sudo apt-get -y install nginx',
}

exec {'html':
  provider => shell,
  command  => 'sudo echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html',
}

exec {'sedConfig':
  provider => shell,
  command  => 'sudo sed -i "/server_name _;/ a\\\trewrite ^/redirect_me http://www.youtube.com permanent;" /etc/nginx/sites-available/default',
}

exec {'start':
  provider => shell,
  command  => 'sudo service nginx start',
}
