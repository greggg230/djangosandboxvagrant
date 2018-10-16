bind = "unix:{{ virtualenv_path }}/var/run/genesishealth_socket"
logfile = "{{ virtualenv_path }}/var/log/gunicorn/genesishealth.log"
workers = 5
timeout = 180
max_requests = 100
