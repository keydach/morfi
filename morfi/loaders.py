# -*- coding: utf-8 -*-

try:
    import cherrypy

    def cherrypy_loader (field_name, default):
        return cherrypy.request.params.get (field_name, default)

except ImportError:
    pass

