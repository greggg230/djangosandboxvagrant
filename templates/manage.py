#!/usr/bin/env python
import os
import os.path
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.conf.generic.settings")
    path = "{{ virtualenv_path }}/src/{{ project_name }}"
    sys.path.append(path)
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
