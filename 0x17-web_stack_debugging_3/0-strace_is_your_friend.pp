# solution Apache return 500
file { '/var/www/html/wp-includes/class-wp-locale.phpp':
ensure => present,
source => '/var/www/html/wp-includes/class-wp-locale.php',
}
