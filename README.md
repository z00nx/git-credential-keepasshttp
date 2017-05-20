# git-credential-keepasshttp
A git credential helper to integrate with keepass using keepasshttp

# Requirements
* python 2
* python-keepasshttp

# Installation
Copy git-credential-keepasshttp into a location into a directory included in $PATH e.g. /usr/local/bin

# Usage
You can set git's credential helper on a per repo basis repository using:
```shell
git config credential.helper keepasshttp
```
Or globally using:
```shell
git config --global credential.helper keepasshttp
```

# Notes:
* Only the get operation is supported
* It will return the first set of credentials found
* Minimal testing has been performed
