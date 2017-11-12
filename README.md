[![Build Status](https://travis-ci.org/z00nx/git-credential-keepasshttp.svg?branch=master)](https://travis-ci.org/z00nx/git-credential-keepasshttp)[![Maintainability](https://api.codeclimate.com/v1/badges/65e6ab4cce993efd9eae/maintainability)](https://codeclimate.com/github/z00nx/git-credential-keepasshttp/maintainability)
# git-credential-keepasshttp
A git credential helper to integrate with keepass using keepasshttp

# Requirements
* python 2 or 3
* python3-keepasshttp for python 3 (https://github.com/MarkusFreitag/python3-keepasshttp.git)
* python-keepasshttp for python 2 (https://github.com/romankh/python-keepasshttp)

# Installation
```shell
pip install --process-dependency-links git+https://github.com/z00nx/git-credential-keepasshttp
```

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
