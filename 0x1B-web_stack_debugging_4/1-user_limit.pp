# Access more files for user

exec {'holberton_user_file_access':
  provider => shell,
  command  => 'sudo sed -i "s/file 5/file 5120/" /etc/security/limits.conf; sudo sed -i "s/file 4/file 4096/" /etc/security/limits.conf'
}