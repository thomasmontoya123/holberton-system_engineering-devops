# Nginx requests
exec { 'serverScale':
  command => "sed -i 's/15/5000/g' /etc/default/nginx; service nginx restart",
  path    => path    => '/bin',
}
