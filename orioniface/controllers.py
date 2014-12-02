# -*- coding: utf-8 -*-
import cherrypy
import jinja2
#import gettext
#import pkg_resources
from morfi import controls, loaders, rules

class ImportFileForm (controls.Form):

    __template__ = 'Form'

    file = controls.FileField ()

    def __init__ (self, name = 'impform'):
        super (ImportFileForm, self).__init__ ('ImportFileForm', loaders.cherrypy_loader, u'Импорт')
        self.name = name
        if self.submitted ():
            self.load ()

class Base (object):

    _cp_config = {
        'tools.jinja.loader': jinja2.PackageLoader (__package__, '__views__'),
    }

    def __init__ (self):
        cherrypy.tools.jinja.env.filters ['dt'] = lambda value, format = '%d.%m.%Y %H:%M:%S': value.strftime (format) #@UndefinedVariable

class SbrfImport (Base):

    def import_payments (self, form):
        print form.file.values

    @cherrypy.expose
    @cherrypy.tools.jinja (template = 'sbrfimport/form.tpl')
    def form (self, *args, **kwargs):
        form = ImportFileForm ()
        if not form.submitted () or not form.check ():
            return {'form': form}
        self.import_payments (form)
        return {'msg': u'Платежи успешно импортированны'}

