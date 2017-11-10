[![Build Status](https://travis-ci.org/z00nx/git-credential-keepasshttp.svg?branch=master)](https://travis-ci.org/z00nx/git-credential-keepasshttp)[![Maintainability](https://api.codeclimate.com/v1/badges/65e6ab4cce993efd9eae/maintainability)](https://codeclimate.com/github/z00nx/git-credential-keepasshttp/maintainability)
# git-credential-keepasshttp
A git credential helper to integrate with keepass using keepasshttp

# Requirements
* python 3
* python3-keepasshttp (pip3 install git+https://github.com/MarkusFreitag/python3-keepasshttp.git)

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
