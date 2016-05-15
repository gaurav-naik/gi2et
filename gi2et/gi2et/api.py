# MN Technique and contributors GPL v3 see license.txt
from __future__ import unicode_literals
import frappe, requests, re, dateutil.parser, datetime, ast
from frappe import _

@frappe.whitelist()
def get_gh_issues(gh_url=None):
	out = []
	headers = {'Authorization': 'token %s' % frappe.db.get_single_value("Gi2Et Settings", "api_token")}
	if gh_url:
		search_url = re.search('^https:\/\/github\.com\/(.*)\/(.*)', gh_url)
		owner = search_url.group(1)
		repo = search_url.group(2)
		r = requests.get("https://api.github.com/repos/{owner}/{repo}/issues?state=all&per_page=100".format(owner=owner, repo=repo), headers=headers if headers else None)
		if r.headers.get("Link"):
			total_pages = int(re.search('.*page=(.+?)>; rel=\"last\"', r.headers.get("Link")).group(1))
		else:
			total_pages = 1

		for x in xrange(total_pages):
			r_page = requests.get("https://api.github.com/repos/{owner}/{repo}/issues?state=all&per_page=100&{page}".format(owner=owner, repo=repo, page=x+1), headers=headers if headers else None)
			out_dict = r_page.json()
			for issue in out_dict:
				if not issue.get("pull_request"):
					out.append(
						{
							"subject": issue.get("title"),
							"status": issue.get("state").title(),
							"exp_start_date": str(dateutil.parser.parse(issue.get("created_at")).date()),
							"description": issue.get("body"),
							"closing_date": str(dateutil.parser.parse(issue.get("closed_at")).date()) if issue.get("closed_at") else "",
							"github_id": issue.get("id"),
							"github_number": issue.get("number")
						})
	else :
		frappe.msgprint(_("Please enter Github url for the Project"))
	return out

@frappe.whitelist()
def add_update_task(project=None, task=None):
	generation_status = ""
	task = ast.literal_eval(task)
	task_list = frappe.get_list("Task", ["name", "subject", "status", "exp_start_date", "exp_end_date", "description", "closing_date", "github_id", "github_number"], {"project": project}) or []
	gh_id_list = []
	
	for tsk in task_list:
		gh_id_list.append(tsk["github_id"])

	if len(task_list) != 0:
		for t in task_list:
			if t.get("github_id") == str(task["github_id"]):
				update_task = frappe.get_doc("Task", t.get("name"))
				update_task.update({
					"subject": task["subject"],
					"status": task["status"],
					"exp_start_date": task["exp_start_date"],
					"exp_end_date": task["exp_end_date"],
					"description": task["description"],
				})
				update_task.flags.ignore_links = True
				update_task.flags.from_project = True
				update_task.flags.ignore_feed = True
				update_task.save(ignore_permissions = True)	
				frappe.db.commit()
				generation_status = _("SUCCESS : Updated Tasks")
	# elif len(task_list) == 0:
	# 	create_new_task(project, task)
	# 	generation_status = _("SUCCESS : Created Tasks")

	if str(task["github_id"]) not in gh_id_list:
		create_new_task(project, task)
		generation_status = _("SUCCESS : Created Tasks")
		
	return generation_status

def create_new_task(project, task):
		new_task = frappe.new_doc("Task")
		new_task.project = project

		new_task.update({
			"subject": task["subject"],
			"status": task["status"],
			"exp_start_date": task["exp_start_date"],
			"exp_end_date": task["exp_end_date"],
			"description": task["description"],
			"github_id": task["github_id"],
			"github_number": task["github_number"]
		})

		new_task.flags.ignore_links = True
		new_task.flags.from_project = True
		new_task.flags.ignore_feed = True
		new_task.save(ignore_permissions = True)
		frappe.db.commit()
