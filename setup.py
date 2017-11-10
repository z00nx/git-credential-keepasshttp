import sys
from setuptools import setup
install_requires = ["keepasshttp"]
if sys.version_info[0:2] < (3, 0):
    dependency_links = ["git+https://github.com/romankh/python-keepasshttp#egg=keepasshttp-0.1.0"]
else:
    dependency_links = ["git+https://github.com/MarkusFreitag/python3-keepasshttp#egg=keepasshttp-0.2.0"]

setup(
    name='git-credential-keepasshttp',
    version='1.0',
    description='A git credential helper to integrate with keepass using keepasshttp',
    url='https://github.com/z00nx/git-credential-keepasshttp',
    author='z00nx 0',
    license='???',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='git credential keepass keepasshttp',
    scripts=['bin/git-credential-keepasshttp'],
    dependency_links=dependency_links,
    install_requires=install_requires,
)
