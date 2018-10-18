# #!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flightbooking.settings')
    try:
        from django.core.management import execute_from_command_line
        is_testing = 'test' in sys.argv

        
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
    if is_testing:
            import coverage
            cov = coverage.coverage(source=['seats', 'flight', 'user', 'bookings','payment'], omit=['*tests.py','*migrations/*', '*urls.py', '*apps.py', '*forms.py', '*views.py*','*serializers.py*'])
            cov.erase()
            cov.start()

    execute_from_command_line(sys.argv)

    if is_testing:
        cov.stop()
        cov.save()
        cov.report()

#!/usr/bin/env python
# import os
# import sys

# if __name__ == '__main__':
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flightbooking.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)

# import os
# import sys

# if __name__ == "__main__":
#     # ...
#     from django.core.management import execute_from_command_line

#     is_testing = 'test' in sys.argv

#     if is_testing:
#         import coverage
#         cov = coverage.coverage(source=['package1', 'package2'], omit=['*/tests/*'])
#         cov.erase()
#         cov.start()

#     execute_from_command_line(sys.argv)

#     if is_testing:
#         cov.stop()
#         cov.save()
#         cov.report()