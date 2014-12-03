# -*- coding: utf-8 -*-
import cherrypy
import jinja2
from morfi import controls, loaders, rules
import pgpxmlrpc
import os.path as osp
import xmlrpclib
import time


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

    mess = u'Платежи успешно импортированны'

    def import_payments (self, form):
        payments = [row.split (',') for row in form.file.values [form].split ('\n')]

        try:
            _states = (
                'UNPROCESSED',  # 0
                'PROCESSING',   # 1
                'DONE',         # 2
                'ERROR'         # 3
            )

            platon = pgpxmlrpc.Service (
                'http://platon.rc-online.ru/xmlrpc',
                'B762029B069573A5EE5523E095EA1074518A6414',
                osp.join ('/home/pmerzlyakov/git/morfi/orioniface/__keyring__'),
                'EF214DC11B673FD9C01643042AE30391CBB7A173', # ID КЛЮЧА ДИОГЕНА
                'vbclxtncvlg' # ПАРОЛЬ КЛЮЧА ДИОГЕНА
            )

            for payment in payments:

                IdTrnsctn = payment [0],
                PayDate = payment [1],
                PrsnlAccnt = payment [2],
                PaySum = payment [3],
                Paysource = payment [4],
                Branch = payment [5],
                Source = payment [6].split (':')

                try:
                    payment_id = platon.diogenes.create (
                        'billing-online',
                        'TEST_PAYMENT_%d' % int (time.time () * 1000),          # external_id (50 chars max, unique)
                        int (time.time ()),                                     # payment time (unix timestamp)
                        PrsnlAccnt,                                             # account
                        PaySum,                                                # sum
                        {                                                       # additional parameters, service-based payment distribution example
                            'billing_reseller_665': 1234.56,                    # All of the sum to reseller with ID = 704
                            'distribute_group_service_50': 535.67,              #        - 535.67 roubles to service with ID = 8389910
                        }                                                       #        - and rest of the sum (1234.56 - 535.67 - 200 = 498,89) will be processed as usual
                    )
                    print 'Payment created, id:', payment_id

                    s = platon.diogenes.state (payment_id)
                    print 'Payment state after creation:', _states [s ['state']], 'error:', s ['error']

                    print 'Waiting for processing...'
                    while platon.diogenes.state (payment_id) ['state'] in (0, 1):
                        time.sleep (1)

                    s = platon.diogenes.state (payment_id)
                    print 'Payment state after procession:', _states [s ['state']], 'error:', s ['error']

                except xmlrpclib.Fault as e:
                    print 'Error %d: %s' % (e.faultCode, e.faultString)

        except:
            self.mess = u'Ошибка при разборе файла, импорт не удался!'

        del form.file.values [form] # Разобраться!!!

    @cherrypy.expose
    @cherrypy.tools.jinja (template = 'sbrfimport/form.tpl')
    def form (self, *args, **kwargs):
        form = ImportFileForm ()
        if not form.submitted () or not form.check ():
            return {'form': form}
        self.import_payments (form)
        return {'msg': self.mess}

