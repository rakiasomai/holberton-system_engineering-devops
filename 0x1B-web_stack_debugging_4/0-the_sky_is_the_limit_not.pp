#  fix our stack so that we get to 0
exec {'number':
  provider => shell,
  path    => ['/usr/bin', '/bin'],
  command => "sudo sed -i 's/15/3000/g'  /etc/default/nginx;  sudo service nginx restart",
}
