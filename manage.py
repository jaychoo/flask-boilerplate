#!/usr/bin/env python
import os
import re
import sys


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit("Please specify module name, e.g. python manage.py add-module NAME")

    module_name = sys.argv[2]
    if module_name in ('static', 'templates'):
        sys.exit("Please do not use reserved name for new module")

    # validate module name - no space, no special characters
    if not re.match('^[a-zA-Z0-9_]+$', module_name):
        sys.exit("Please use alphanumeric and underscore for module name")

    module_path = 'app/%s' % module_name
    if not os.path.exists(module_path):
        print "Creating module directory and files..."
        try:
            os.makedirs(module_path)
        except OSError:
            pass

        if os.path.exists(module_path):
            files = ('__init__.py', 'models.py', 'views.py', 'constants.py', 'utils.py')
            for e in files:
                file_path = '%s/%s' % (module_path, e)
                if not os.path.isfile(file_path):
                    print e
                    with open(file_path, 'a') as f:
                        f.write("# -*- coding: utf-8 -*-\n\n\n")

        print "Creating directory in templates folder..."
        try:
            os.makedirs('app/templates/%s' % module_name)
        except OSError:
            pass
