import frappe

__version__ = '1.0.0'

@frappe.whitelist()
def get_pdf_file(docname):
	f = frappe.get_doc('File', docname)
	frappe.local.response.filename = f.file_name
	frappe.local.response.filecontent = f.get_content()
	frappe.local.response.type = "pdf" 

@frappe.whitelist()
def download_file(docname):
	f = frappe.get_doc('File', docname)
	frappe.local.response.filename = f.file_name
	frappe.local.response.filecontent = f.get_content()
