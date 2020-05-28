# fix the limit
exec { 'fix hard':
  provider => shell,
  path     => ['/bin', '/usr/bin', '/usr/sbin'],
  command  => 'sudo sed -i \'s/nofile 5/nofile 40000/\' /etc/security/limits.conf',
}
exec { 'fix soft':
  provider => shell,
  path     => ['/bin', '/usr/bin', '/usr/sbin'],
  command  => 'sudo sed -i \'s/nofile 4/nofile 40000/\' /etc/security/limits.conf',
}
