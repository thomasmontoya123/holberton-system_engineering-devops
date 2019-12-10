# Add config to client
file_line { 'append PasswordAuthentication':
    ensure => present,
    line   => 'PasswordAuthentication no',
    path   => '/etc/ssh/ssh_config'
  }
file_line { 'append IdentityFile':
    ensure => present,
    line   => 'IdentityFile ~/.ssh/holberton',
    path   => '/etc/ssh/ssh_config'
  }