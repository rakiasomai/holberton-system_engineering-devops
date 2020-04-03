# puppet advanced
package { 'nginx':
  ensure => installed,
}

file_line { 'X':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}

file { '/usr/share/nginx/html/index.html':
  content => 'Holberton School',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
