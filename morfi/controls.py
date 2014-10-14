# -*- coding: utf-8 -*-

from morfi.base import Field, Group
import morfi.rules as mrules


class Form (Group):

    submitted_field = '__submitted__'

    def __init__ (self, name, loader, submit = u'Submit'):
        super (Form, self).__init__ (name)
        self.loader = loader
        self.submit = submit

    def load (self):
        super (Form, self).load (self.loader)

    def submitted (self):
        return self.loader (self.submitted_field, None) == 'submitted'


class Titled (Field):

    def __init__ (self, title = None, **kwargs):
        super (Titled, self).__init__ (**kwargs)
        self.title = title


class StaticText (Titled):
    pass


class Edit (Titled):

    def __init__ (self, maxlength = 0, **kwargs):
        super (Edit, self).__init__ (**kwargs)
        self.maxlength = maxlength

    def set_value (self, value):
        value = unicode (value)
        if self.maxlength:
            value = value [:self.maxlength]
        super (Edit, self).set_value (value)


class CheckBox (Titled):
    pass


class ComboBox (Titled):

    def __init__ (self, items = (), **kwargs):
        super (ComboBox, self).__init__ (**kwargs)
        self.items = items
        self.rules.append (mrules._HasItem (u'Invalid item'))


class GroupBox (Group):

    def __init__ (self, title = None):
        super (GroupBox, self).__init__ ()
        self.title = title


#class CheckList (Titled):
#
#    def __init__ (self, name, title = '', default = [], items = ()):
#        super (CheckList, self).__init__ (name, title, default)
#        self.items = items
#
#    def _load_value (self):
#        self.value = [item for item in self.listItems if item [0] in cherrypy.request.params]


