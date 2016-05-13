# MN Technique and contributors GPL v3 see license.txt
from __future__ import unicode_literals
import frappe, requests, re
from frappe import _

@frappe.whitelist()
def get_gh_issues(gh_url=None):
	out = []
	if gh_url:
		search_url = re.search('^https:\/\/github\.com\/(.*)\/(.*)', gh_url)
		owner = search_url.group(1)
		repo = search_url.group(2)
		r = requests.get("https://api.github.com/repos/{owner}/{repo}/issues?state=all&per_page=100".format(owner=owner, repo=repo))
		if r.headers.get("Link"):
			total_pages = int(re.search('.*page=(.+?)>; rel=\"last\"', r.headers.get("Link")).group(1))
		else:
			total_pages = 1

		for x in xrange(total_pages):
			r_page = requests.get("https://api.github.com/repos/{owner}/{repo}/issues?state=all&per_page=100&{page}".format(owner=owner, repo=repo, page=x+1))
			out_dict = r_page.json()
			for issue in out_dict:
				out.append(
					{
						"subject": issue.get("title"),
						"status": issue.get("state"),
						"exp_start_date": issue.get("created_at"),
						"description": issue.get("body"),
						"closing_date": issue.get("closed_at")
					})
	else :
		frappe.msgprint(_("Please enter Github url for the Project"))
	return out
