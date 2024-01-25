# Fix error in opening large amounts of files

exec {'update-file-limit-restart':
  provider => shell,
  command  => 'sudo sed -i "/^#ULIMIT=/{s/^#//}" /etc/default/nginx;sudo service nginx restart'
}