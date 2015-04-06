# -*- coding: utf-8 -*-

import sys
if sys.version [0] >= 3:
    unicode = str
import re


email_pattern = ur'^[a-z0-9_.-]{1,40}@(([a-z0-9-]+\.)+([a-z]{2,})|[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})$'
phone_pattern = ur'^((\+\d{1,3})|8)[\s\-]*(\(\d{3}\)|\d{3})[\s\-]*(\d{3}[\s\-]*\d{2}[\s\-]*\d{2})|(\d{2}[\s\-]*\d{2}[\s\-]*\d{3})|(\d{2}[\s\-]*\d{3}[\s\-]*\d{2})$'
numeric_pattern = ur'^(\-|\+)?\d+(\.\d+)?$'
int_pattern = ur'^(\-|\+)?\d+$'
bool_pattern = ur'^[0-1]$'


def to (type_, value, default):
    try:
        return type_ (value)
    except (ValueError, TypeError):
        return default


to_int = lambda v, d: to (int, v, d)


class Rule (object):

    def __init__ (self, message):
        self.message = message

    def set_control (self, value):
        pass

    def __call__ (self):
        raise NotImplementedError ('Rule.__call__() must be implemented')


class Required (Rule):
    '''
    Признак необходимости ввода значения
    '''
    def __init__ (self, message = u'Value required'):
        super (Required, self).__init__ (message)

    def set_control (self, control):
        super (Required, self).set_control (control)
        control.is_required = True

    def __call__ (self, control):
        return self.message if not to (bool, control.value, False) else None


class Regexp (Rule):
    '''
    Проверка значения на соответствие регулярному выражению
    '''
    def __init__ (self, pattern = email_pattern, flags = re.UNICODE + re.IGNORECASE, message = u'Invalid value'):
        super (Regexp, self).__init__ (message)
        self.pattern = pattern
        self._regexp = re.compile (pattern, flags)

    def set_control (self, control):
        if self.pattern == int_pattern:
            control.converters.append (lambda x: to (int, x, 0))
        elif self.pattern == numeric_pattern:
            control.converters.append (lambda x: to (float, x, 0.0))

    def __call__ (self, control):
        print unicode (control.value)
        print self._regexp.search (unicode (control.value))
        return None if unicode (control.value) == '' or self._regexp.search (unicode (control.value)) else self.message


class Equal (Rule):
    '''
    Проверка идентичности значений
    '''
    def __init__ (self, original_control, message = u'Values must be equal'):
        super (Equal, self).__init__ (message)
        self.original_control = original_control

    def __call__ (self, control):
        return None if control.value == self.original_control.value else self.message


class _HasItem (Rule):
    '''
    Внутреннее правило для списков
    '''
    def __call__ (self, control):
        return None if control.value in [str (item [0]) for item in control.items] else self.message


class _Captcha (Rule):
    '''
    Внутреннее правило для капчи
    '''
    def __call__ (self, control):
        _secure_text = control.captcha_text
        if not control.strict:
            _secure_text = _secure_text.lower ()
            value = control.value.lower ()
        return _secure_text == value
