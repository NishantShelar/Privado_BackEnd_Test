# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["te"]
mycol = mydb["templates"]

data1 = [{
	"type": "system",
	"entity": "entity",
	"customerId": "system",
	"law": "CCPA",
	"fields": [{
			"field": "representative_contact_details",
			"label": "Representative Contact Details",
			"data_type": "long-text",
			"default": "Type contact details here..",
			"field_type": "contact_details",
			"field_type_label": "Contact Details",
			"is_removable": "false",
			"mandatory": "false"
		},
		{
			"field": "data_protection_officer",
			"label": "Data Protection Officer",
			"data_type": "options",
			"default": "Type the data protection officer name here..",
			"field_type": "contact_details",
			"field_type_label": "Contact Details",
			"is_removable": "false",
			"mandatory": "false",
			"options_url": {
				"url": "dm/customer/<customer_id>/users",
				"request_type": "GET"
			}
		},
		{
			"field": "dpo_contact_details",
			"label": "Data Protection Officer Contact Details",
			"data_type": "long-text",
			"default": "Type contact details here..",
			"field_type": "contact_details",
			"field_type_label": "Contact Details",
			"is_removable": "false",
			"mandatory": "false"
		}
	]
}]

data2= [{
	"type": "system",
	"entity": "entity",
	"customerId": "system",
	"law" : "GDPR",
	"fields" : [ 
		{ "field" : "address", "label" : "Address", "data_type" :"long-text", "default" : "Type address here..", "field_type":	"contact_details", "field_type_label":	"Contact Details", "is_removable" : "false", "mandatory": "false"},
		{ "field" : "representative", "label" : "Representative", "data_type" :"options", "default" : "Type the representative name here..", "field_type":	"contact_details", "field_type_label":	"Contact Details", "is_removable" : "false", "mandatory": "false",
			"options_url": {
				"url" : "dm/customer/<customer_id>/users",
				"request_type" : "GET"
			}
		}
	]
}
]

data3=[{
	"type": "system",
	"entity": "entity",
	"customerId": "system",
	"law": "base",
	"fields": [{
			"field": "name",
			"label": "Name",
			"data_type": "short-text",
			"default": "Type name here..",
			"field_type": "basic_details",
			"field_type_label": "Basic Details",
			"is_removable": "false",
			"mandatory": "true"
		},
		{
			"field": "description",
			"label": "Description",
			"data_type": "long-text",
			"default": "Type description here..",
			"field_type": "basic_details",
			"field_type_label": "Basic Details",
			"is_removable": "false",
			"mandatory": "false"
		},
		{
			"field": "entity_type",
			"label": "Entity Type",
			"data_type": "options",
			"default": "",
			"field_type": "basic_details",
			"field_type_label": "Basic Details",
			"is_removable": "false",
			"mandatory": "false",
			"options_list": [
				"Affiliate", "Client", "Holding Company", "Regulatory Body", "Subsidiary"
			]
		},
		{
			"field": "location",
			"label": "Location",
			"data_type": "options",
			"default": "",
			"field_type": "basic_details",
			"field_type_label": "Basic Details",
			"is_removable": "false",
			"mandatory": "false",
			"options_url": {
				"url": "dm/geos",
				"request_type": "GET"
			}
		}
	]
}]
mycol.insert_many(data1)
mycol.insert_many(data2)
mycol.insert_many(data3)
