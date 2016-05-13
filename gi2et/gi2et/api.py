# MN Technique and contributors GPL v3 see license.txt
from __future__ import unicode_literals
import frappe, requests, re
from frappe import _

@frappe.whitelist()
def get_gh_issues(gh_url=None):
	if gh_url:
		search_url = re.search('^https:\/\/github\.com\/(.*)\/(.*)', gh_url)
		owner = search_url.group(1)
		repo = search_url.group(2)
		r = requests.get("https://api.github.com/repos/{owner}/{repo}/issues?state=all&per_page=100".format(owner=owner, repo=repo))
		if r.headers.get("Link"):
			header_link = re.search('.*page=(.+?)>; rel=\"last\"', r.headers.get("Link")).group(1)
	else :
		frappe.msgprint(_("Please enter Github url for the Project"))
