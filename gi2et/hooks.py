# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "gi2et"
app_title = "Gi2Et"
app_publisher = "MN Technique"
app_description = "Pull Github Issues into Project Tasks"
app_icon = "octicon octicon-mark-github"
app_color = "#87cefa"
app_email = "support@castlecraft.in"
app_version = "0.0.1"
app_license = "GPL v3"

fixtures = ["Custom Field", "Custom Script"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gi2et/css/gi2et.css"
# app_include_js = "/assets/gi2et/js/gi2et.js"

# include js, css files in header of web template
# web_include_css = "/assets/gi2et/css/gi2et.css"
# web_include_js = "/assets/gi2et/js/gi2et.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "gi2et.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "gi2et.install.before_install"
# after_install = "gi2et.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gi2et.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"gi2et.tasks.all"
# 	],
# 	"daily": [
# 		"gi2et.tasks.daily"
# 	],
# 	"hourly": [
# 		"gi2et.tasks.hourly"
# 	],
# 	"weekly": [
# 		"gi2et.tasks.weekly"
# 	]
# 	"monthly": [
# 		"gi2et.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "gi2et.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "gi2et.event.get_events"
# }

