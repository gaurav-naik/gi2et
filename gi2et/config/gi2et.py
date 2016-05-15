from frappe import _

def get_data():
	return [
		{
			"label": _("Setup"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Gi2Et Settings",
					"description": _("Github API Token"),
				}
			]
		},
		{
			"label": _("Tools"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Gi2Et Task Sync",
					"description": _("Tool to pull and update Tasks from Github Issues"),
				}
			]
		}
	]
