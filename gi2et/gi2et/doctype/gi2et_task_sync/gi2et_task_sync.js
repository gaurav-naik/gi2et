// Copyright (c) 2016, MN Technique and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gi2Et Task Sync', {
	refresh: function(frm) {
		frm.disable_save();
	},
	get_issues: function(frm){
		pull_gh_issues(frm);
	},
	generate_tasks: function(frm){
		if (frm.doc.github_issues.length == 0) {
			frappe.msgprint(__("Get Issues first"))
		}
		else if (frm.doc.github_issues.length > 0) {
			github_issues = frm.doc.github_issues;
			for (var i = 0; i < github_issues.length; i++) {
				if (frm.doc.github_issues[i].subject === undefined) {
					frm.set_value("task_generation_status", "ERROR : Remove Manually added Row in Github Issues ...");
				}
				else{
					frappe.call({
						method: "gi2et.gi2et.api.add_update_task",
						args:{
							project: frm.doc.project,
							task: frm.doc.github_issues[i],
							issue_list_len: github_issues.length
						},
						callback: function (data) {
							frm.set_value("task_generation_status", data.message);
						}
					});
				}
			}
		}
	}
});

cur_frm.add_fetch("project", "github_repo", "github_repo");

pull_gh_issues = function (frm) {
	frappe.call({
		method: "gi2et.gi2et.api.get_gh_issues",
		args: {
			gh_url: cur_frm.doc.github_repo
		},
		callback: function (data) {
			add_new_gh_issues(frm, data);
			cur_frm.refresh_field("github_issues");
		}
	});
}

add_new_gh_issues = function (frm, data) {
	frm.clear_table("github_issues");
	$.each(data.message, function(i, d) {
		var c = frappe.model.add_child(cur_frm.doc, "Gi2Et Task Sync Issue", "github_issues");
		c.subject = d.subject;
		c.status = d.status;
		c.exp_start_date = d.exp_start_date;
		c.description = d.description;
		c.exp_end_date = d.closing_date;
		c.github_id = d.github_id;
		c.github_number = d.github_number;
	});
	cur_frm.refresh_field("github_issues");
}
