#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


def main ():
    setup (
        name = 'morfi',
        version = '0.0.1',
        description = 'RC Online services library',
        long_description = 'RC Online services library',
        author = 'Pavel Merzlyakov',
        author_email = 'merzlyakovpavel@gmail.com',
        url = 'https://github.com/keydach/morfi',
        license = 'LGPLv3',
        packages = ('morfi', 'orioniface'),
        install_requires = ['jinja2 >= 2.7.3', 'cherrypy >= 3.3.0']
    )


if __name__ == "__main__":
    main ()
