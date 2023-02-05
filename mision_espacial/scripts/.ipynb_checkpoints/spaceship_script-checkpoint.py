from xmlrpc import client

url = 'https://wesolveuy-odoo-curso-16-0-naveespacial-7147191.dev.odoo.com/'
db = 'wesolveuy-odoo-curso-16-0-naveespacial-7147191'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db, uid, password,
                                'mision_espacial.spaceship', 'check_access_rights',
                                ['write'], {'raise_exception': False})
print(model_access)

spaceship_fields = models.execute_kw(db, uid, password,
                                  'mision_espacial.spaceship', 'fields_get',
                                  [],{'attributes': ['string', 'type', 'required']})
print(spaceship_fields)

new_spaceship = models.execute_kw(db, uid, password,
                               'mision_espacial.spaceship', 'create',
                               [
                                   {
                                       'name': 'Millenium Falcon',
                                       'type': 'freighter',
                                       'model': 'YT-1300F light freighter',
                                       'capacity_passenger': 30,
                                       'length': 114,
                                       'width': 94,
                                       'height': 26,
                                       'fuel_type': 'solid_fuel',
                                   }
                               ]
                               )
print(new_spaceship)
