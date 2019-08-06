#Creates Sets up client SSH configuration file
file_line { 'ssh_config':
    path     => '/etc/ssh/ssh_config',
    match    => 'PasswordAuthentication',
    line     => 'PasswordAuthentication no',
    multiple => 'true'
}
file_line { 'ssh_config_2':
    path     => '/etc/ssh/ssh_config',
    match    => 'IdentityFile',
    line     => 'IdentityFile ~/.ssh/holberton',
    multiple => 'true'
}
