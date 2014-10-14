# -*- coding: utf-8 -*-
import cherrypy
import jinja2
#import gettext
#import pkg_resources
from morfi import controls, loaders, rules


class SuperDuperForm (controls.Form):

    __template__ = 'Form'

    first_name = controls.Edit (title = u'Имя', rules = (rules.Required (u'Имя, сестра, имя!'),))
    last_name = controls.Edit (title = u'Фамилия')

    class _Subgroup (controls.GroupBox):

        __template__ = 'GroupBox'

        age = controls.Edit (title = u'Возраст', rules = (rules.Required (u'Напиши, чо уж там'), rules.Regexp (rules.int_pattern, message = u'Числом давай!')))
        sex = controls.ComboBox (title = u'Пол', items = ((0, u'Мужской'), (1, u'Женский')), default = 0, rules = (rules.Required (u'Я без полу не могу'),))

    info = _Subgroup (u'Всякое')

    def __init__ (self):
        super (SuperDuperForm, self).__init__ ('SuperDuperForm', loaders.cherrypy_loader, u'Сохранить')
        if self.submitted ():
            self.load ()


class Base (object):

    _cp_config = {
        'tools.jinja.loader': jinja2.PackageLoader (__package__, '__views__'),
        #'tools.jinja.gettext_translations': gettext.translation ('aurora', pkg_resources.resource_filename (__package__, 'locale'))
    }

    def __init__ (self):
        cherrypy.tools.jinja.env.filters ['dt'] = lambda value, format = '%d.%m.%Y %H:%M:%S': value.strftime (format) #@UndefinedVariable


class Example (Base):

    @cherrypy.expose
    @cherrypy.tools.jinja ()
    def index (self):
        return {
            'hello': u'Это тестовый контроллер, его корень',
            '__template__': 'example/index.tpl'
        }

    @cherrypy.expose
    @cherrypy.tools.jinja (template = 'example/form.tpl')
    def form (self, *args, **kwargs):
        form = SuperDuperForm ()
        if not form.submitted () or not form.check ():
            return {'form': form}
        else:
            return {'msg': u'Все вроде норм'}
