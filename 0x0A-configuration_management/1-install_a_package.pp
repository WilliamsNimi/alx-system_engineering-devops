#installing Flask from pip3
class flask {
  package { 'flask':
    ensure => 'installed',
    provider => 'pip3',
  }
}