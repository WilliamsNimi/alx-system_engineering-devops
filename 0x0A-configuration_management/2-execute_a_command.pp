#using exec and pkill to kill a process
exec {'/usr/bin/pkill':
  command  => ['/usr/bin/pkill', '-g', '-f', 'killmenow'],
}