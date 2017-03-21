
from __future__ import unicode_literals
import frappe, os, json
from frappe.utils import cstr
from unidecode import unidecode

@frappe.whitelist(allow_guest=True)
def update_location(vehicle=None,lat=None,lon=None):
	vehicle = frappe.get_doc("Vehicle", vehicle)
	vehicle.flags.ignore_permissions = True
	vehicle.latitude = lat
	vehicle.longitude = lon
	vehicle.save(ignore_permissions=True)
	frappe.db.commit()
	return "updated location for " + vehicle.name