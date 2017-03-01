#!/usr/bin/env python3

from pathlib import Path
from subprocess import run, PIPE

HOSTS = 'hosts'
NGINX = 'nginx_site'
DOMAIN = 'upracmeslovensko'

config_files = [HOSTS, NGINX]

this_dir = Path(__file__).parent
nginx_sites_available = Path('/etc/nginx/sites-available')
if  not nginx_sites_available.is_dir():
    exit(f"Nginx config directory not found in {nginx_sites_available}. Do you have installed nginx?")

for name, config_file in [(name, (this_dir / 'nginx' / name).with_suffix('.php')) for name in config_files]:
    print(f"{name}: {config_file}")

    command = ['php', str(config_file)]
    process = run( command
                , check = True
                , stdout=PIPE
                , stderr=PIPE,
                )

    output = process.stdout.decode()
    err = process.stderr.decode()
    # print(output)
    config_output = config_file.with_suffix('')
    config_output.write_text(output, encoding='utf-8')

    if err:
        print(err)
        exit(f"Selhalo {' '.join(command)}: {err}")

    if name == HOSTS:
        run(['meld', config_output, '/etc/hosts'])
        # pass
    elif name == NGINX:
        nginx_config = nginx_sites_available / DOMAIN
        nginx_config.write_text(output, encoding='utf-8')

        nginx_sites_enabled = nginx_sites_available.parent / 'sites-enabled' / DOMAIN
        try:
            nginx_sites_enabled.symlink_to(nginx_config)
        except FileExistsError as e:
            assert nginx_sites_enabled.samefile(nginx_config)
            print(f"Link {nginx_sites_enabled} už jestvuje")

command = ['service', 'nginx', 'restart']
print(' '.join(command))
run( command )