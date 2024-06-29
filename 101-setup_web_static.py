#This file configures a server to link to our static webpages
exec {'update':
  command  => 'sudo apt -y update',
  provider => shell,
  before   => Package['nginx'],
}
package {'nginx':
  name     => 'nginx',
  provider => apt,
  before   => Exec['create test directory'],
}
exec {'create test directory':
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  provider => shell,
  before   => Exec['create shared directory'],
}
exec {'create shared directory':
  command  => 'sudo mkdir -p /data/web_static/shared/',
  provider => shell,
  before   => Exec['create test file'],
}
exec {'create test file':
  command  => 'echo "Hello Madness" | sudo tee /data/web_static/releases/test/index.html',
  provider => shell,
  before   => Exec['delete old symlink'],
}
exec {'delete old symlink':
  command  => 'sudo rm -f /data/web_static/current',
  provider => shell,
  before   => Exec['create new symlink'],
}
exec {'create new symlink':
  command  => 'sudo ln -s /data/web_static/releases/test/ /data/web_static/current',
  provider => shell,
  before   => File['/data/'],
}
file {'/data/':
  ensure   => directory,
  owner    => 'ubuntu',
  group    => 'ubuntu',
  recurse  => true,
  before   => Exec['Edit config file'],
}
exec {'Edit config file':
  command  => 'sudo sed -i \'38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n\' /etc/nginx/sites-available/default',
  provider => shell,
  before   => Exec['restart server'],
}
exec {'restart server':
  command  => 'sudo service nginx restart',
  provider => shell,

}
