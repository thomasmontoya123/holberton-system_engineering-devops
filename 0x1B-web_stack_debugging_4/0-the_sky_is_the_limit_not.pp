# handle more requets
exec { 'server_scale':
  command => "sed -i 's/15/5000/g' /etc/default/nginx; service nginx restart",
  path    => [ '/bin/', '/sbin/', '/usr/bin', '/usr/sbin/' ]
}
