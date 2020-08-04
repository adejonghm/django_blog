import os
import sys
from distutils.version import LooseVersion

if sys.version_info.major < 3:
    print('[!] You are running an old version of Python. This project requires Python 3.')

    sys.exit(1)

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    reqs = f.readlines()

pkg_names = {
    'Django': 'django',
    'Pillow': 'PIL', 
    'django-crispy-forms': 'crispy_forms',
    'lazy-object-proxy': 'lazy_object_proxy',
    'typed-ast': 'typed_ast'
}

packages = []

for req in reqs:
    pkg, ver = req.split('==')
    packages.append((pkg.strip(), ver.strip()))

for (pkg, version_wanted) in packages:
    module_name = pkg_names.get(pkg, pkg)
    try:
        m = __import__(module_name)
        version_installed = m.__version__
        status = '✓'
    except ImportError as e:
        m = None
        version_installed = 'Not installed'
        status = 'X'

    if m is not None:
        version_installed = m.__version__
        if LooseVersion(version_wanted) > LooseVersion(version_installed):
            status = 'X'
    print('[{}] {} {}'.format(status, pkg.ljust(25), version_installed))
