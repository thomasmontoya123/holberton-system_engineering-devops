# Script to fix phpp problem
exec { 'server execution':
  provider => shell,
  command  => 'sudo sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php; sudo service apache2 restart;',
}
