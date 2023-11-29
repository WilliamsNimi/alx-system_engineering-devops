#using exec and pkill to kill a process
exec {'killmenow':
  command  => "'/usr/bin/pkill', '-g', '-f', 'killmenow'",
}