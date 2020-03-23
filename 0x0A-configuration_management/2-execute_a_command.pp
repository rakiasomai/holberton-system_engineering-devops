#Using Puppet, create a manifest that kills "killmenow".
exec { 'killmenow':
command => 'pkill -f killmenow',
path    => '/usr/bin',
}
