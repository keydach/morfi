# -*- coding: utf-8 -*-

import pkg_resources
import cherrypy
from cherrypy import _cpconfig
from cherrybase import db
import cherrybase


__version__ = '0.0.1'


config = {
    '/' : {
        'tools.encode.on': True,
        'tools.gzip.on': True,
        'tools.gzip.mime_types': ['text/*'],
        'tools.staticdir.root': pkg_resources.resource_filename (__package__, '__static__'),
    },
    '/static' : {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': '',
    }
}


def use_db (*args, **kwargs):
    return db.use_db (__package__, *args, **kwargs)


def get_applications (mode, basename):
    import controllers

    _cpconfig.merge (
        config,
        pkg_resources.resource_filename (__package__, '__config__/%s.conf' % mode)
    )
    conf = config.get ('main', {})

    db.auto_config (config, __package__, '', 'db')
    #alchemy.wrap (__package__)

    app = cherrybase.Application (
        name = __package__,
        vhosts = conf.get ('vhosts', '.'.join ((__package__, basename))),
        config = config,
        routes = (
            ('/', controllers.SbrfImport (), None),
       )
    )
    return app
