#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Meta (object):

    def __new__ (self, cls, clsname, bases, dict_):
        for name, field in dict_.items ():
            if isinstance (field, Field) and field.name is None:
                field.name = name
        return super (Meta, self).__new__ (cls, clsname, bases, dict_)


class Field (object):

    __metaclass__ = Meta

    _number = 0

    def __init__ (self, default = None, name = None, rules = ()):
        Field._number += 1
        self._number = self._number
        self.default = default
        self.name = name
        self.rules = list (rules)
        self.wrappers = []
        self.values = {}
        self.obj = None

    def fields (self):
        res = [attr for attr in (getattr (self, name, None) for name in dir (self)) if isinstance (attr, Field) and attr != self.obj]
        res.sort (key = lambda f: (f._number, f.name))
        for field in res:
            yield field

    def set_value (self, value):
        self.values [self.obj] = value

    def __get__ (self, obj, cls):
        self.obj = obj
        return self

    @property
    def value (self):
        return self.values.get (self.obj, self.default)

    @value.setter
    def value (self, val):
        self.set_value (val)

    def load (self, loader):
        self.value = loader (self.name)

    def check (self):
        self.errors = []
        for rule in self.rules:
            err = rule (self)
            if err:
                self.errors.append (err)
        return not self.errors


class Group (Field):

    def __init__ (self, *args, **kwargs):
        super (Group, self).__init__ (*args, **kwargs)

    def set_value (self, value):
        for field in self.fields ():
            field.set_value (value.get (field.name, field.default))

    def load (self, loader):
        for field in self.fields ():
            field.load (loader)

    def check (self):
        res = True
        for field in self.fields ():
            res = field.check () and res
        return res


class Titled (Field):

    def __init__ (self, title = None, **kwargs):
        super (Titled, self).__init__ (**kwargs)
        self.title = title


class Edit (Titled):

    def __init__ (self, maxlength = 0, **kwargs):
        super (Edit, self).__init__ (**kwargs)
        self.maxlength = maxlength


class Form (Group):

    def __init__ (self, loader):
        super (Form, self).__init__ ()
        self.loader = loader
        self.submitted = False

    def load (self, loader = None):
        super (Form, self).load (loader)
        self.submitted = self.loader ('__%s_submitted__' % self.name)
