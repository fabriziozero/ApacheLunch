#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

#pequeña modificación para probar mi nueva rama
#segunda modificación de comentario
#probando tercer comentario
#hago un cuarto comentario o sea modificacion
#intento de fusionar la rama miguel2 sobre master



def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ApacheLaunch.settingsProd')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
