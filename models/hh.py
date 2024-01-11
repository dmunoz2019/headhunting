from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class HeadHuntingClient(models.Model):
    _name = 'headhunting.client'
    _description = 'headhunting.client'
    _inherits = {'res.partner': 'res_partner_id'}

    res_partner_id = fields.Many2one('res.partner', string='Related Partner', required=True, ondelete='cascade', index=True, copy=False)
    contract_ids = fields.One2many('headhunting.contract', 'client_id', string='Contracts')


class HeadHuntingdepartment(models.Model):
    _name = 'headhunting.department'
    _description = 'headhunting.department'
    _inherits = {'hr.department': 'hr_department_id'}

    hr_department_id = fields.Many2one('hr.department', string='hr_department_id', required=True, ondelete='cascade', index=True, copy=False)
    contract_ids = fields.One2many('headhunting.contract', 'hr_department_id', string='Contracts')
    candidate_ids = fields.One2many('headhunting.candidate', 'hr_department_id', string='Candidates')
    job_position_ids = fields.One2many('headhunting.job_position', 'hr_department_id', string='Job Positions')

class HeadHuntingContract(models.Model):
    _name = 'headhunting.contract'
    _description = 'headhunting.contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    client_id = fields.Many2one('headhunting.client', string='Client', required=True, ondelete='cascade', index=True, copy=False)
    job_positions = fields.One2many('headhunting.job_position', 'contract_id', string='Job Positions')
    hr_department_id = fields.Many2one('headhunting.department', string='Department', required=True, ondelete='cascade', index=True, copy=False)
class HeadHuntingJobPosition(models.Model):
    _name = 'headhunting.job_position'
    _description = 'headhunting.job_position'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    contract_id = fields.Many2one('headhunting.contract', string='Contract', required=True, ondelete='cascade', index=True, copy=False)
    candidate_ids = fields.Many2many('headhunting.candidate', 'job_position_candidate_rel', 'job_position_id', 'candidate_id', string='Candidates')
    hr_department_id = fields.Many2one('headhunting.department', string='Department', required=True, ondelete='cascade', index=True, copy=False)

class HeadHuntingCandidate(models.Model):
    _name = 'headhunting.candidate'
    _description = 'headhunting.candidate'
    _inherits = {'hr.applicant': 'hr_applicant_id'}
    partner_email = fields.Char(string='Email', required=True, index=True, copy=False, related='partner_id.email', store=True)
    hr_applicant_id = fields.Many2one('hr.applicant', string='Applicant', required=True, ondelete='cascade', index=True, copy=False)
    job_position_ids = fields.Many2many('headhunting.job_position', 'job_position_candidate_rel', 'candidate_id', 'job_position_id', string='Job Positions')
    applicant_document_ids = fields.One2many('headhunting.candidate.documents', 'candidate_id', string='Documents')
    hr_department_id = fields.Many2one('headhunting.department', string='Department', required=True, ondelete='cascade', index=True, copy=False)
    partner_linkedin = fields.Char(string='Linkedin', required=True, index=True, copy=False, store=True)
    partner_github = fields.Char(string='Github', required=True, index=True, copy=False, store=True)

class HeadHuntingCandidateDocuments(models.Model):
    _name = 'headhunting.candidate.documents'
    _description = 'headhunting.candidate.documents'
    _inherits = {'documents.document': 'document_id'}

    documents_folder_id = fields.Many2one('documents.folder', string='Documents Folder', required=True, ondelete='cascade', index=True, copy=False)
    candidate_id = fields.Many2one('headhunting.candidate', string='Candidate', required=True, ondelete='cascade', index=True, copy=False)

# Los modelos de HeadhuntingInterviewer y HeadhuntingRecruiter parecen estar bien estructurados.

class HeadhuntingInterviewer(models.Model):
    _name = 'headhunting.interviewer'
    _description = 'headhunting.interviewer'
    _inherits = {'hr.employee': 'hr_employee_id'}

    hr_employee_id = fields.Many2one('hr.employee', string='hr_employee_id', required=True, ondelete='cascade', index=True, copy=False)
    contract_ids = fields.Many2many('headhunting.contract', string='contract_ids', required=True, ondelete='cascade', index=True, copy=False)
    interview_ids = fields.Many2many('headhunting.interview', string='interview_ids', required=True, ondelete='cascade', index=True, copy=False)

class HeadhuntingRecruiter(models.Model):
    _name = 'headhunting.recruiter'
    _description = 'headhunting.recruiter'
    _inherits = {'hr.employee': 'hr_employee_id'}

    hr_employee_id = fields.Many2one('hr.employee', string='hr_employee_id', required=True, ondelete='cascade', index=True, copy=False)
    contract_ids = fields.Many2many('headhunting.contract', string='contract_ids', required=True, ondelete='cascade', index=True, copy=False)
    interview_ids = fields.Many2many('headhunting.interview', string='interview_ids', required=True, ondelete='cascade', index=True, copy=False)

class HeadhuntingInterview(models.Model):
    _name = 'headhunting.interview'
    _description = 'headhunting.interview'
    _inherits = {'calendar.event': 'calendar_event_id'}

    calendar_event_id = fields.Many2one('calendar.event', string='calendar_event_id', required=True, ondelete='cascade', index=True, copy=False)
    candidate_id = fields.Many2one('headhunting.candidate', string='candidate_id', required=True, ondelete='cascade', index=True, copy=False)
    interviewer_ids = fields.Many2many('headhunting.interviewer', string='interviewer_ids', required=True, ondelete='cascade', index=True, copy=False)
    recruiter_ids = fields.Many2many('headhunting.recruiter', string='recruiter_ids', required=True, ondelete='cascade', index=True, copy=False)
    contract_id = fields.Many2one('headhunting.contract', string='contract_id', required=True, ondelete='cascade', index=True, copy=False)

#  We need to create a documents.folder record for each headhunting.contract record.
