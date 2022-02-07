from odoo import fields, models, exceptions


class AdmissionCollege(models.Model):
    _name = "admission.college"
    _description = "admission college"

    admission_no = fields.Char()
    _sql_constraints = [('admission_no', 'unique(admission_no)',
                         'admission_no must be unique!')]
    admission_date = fields.Date()
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    father = fields.Char()
    mother = fields.Char()
    communication_address = fields.Char()
    permanent_address = fields.Char()
    used = fields.Boolean(string='Same as communication address')
    phone = fields.Char()
    email = fields.Char()
    Course = fields.Selection(
        string='Course',
        selection=[('bsc', 'BSC'), ('msc', 'MSC'), ('b-tech', 'B-TECH'), ],
        help="Course is used to separate BSC,MSC,B-TECH")
    application_date = fields.Date(default=fields.Date.context_today)
    academic_year = fields.Integer()
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company.id)
    previous_educational_qualification = fields.Char()
    educational_institute = fields.Char()
    transfer_certificate = fields.Binary("Transfer certificate")
    state = fields.Selection(
        string='State',
        selection=[('draft', 'Draft'), ('application', 'Application'),
                   ('approved', 'Approved'), ('reject', 'Reject'),
                   ('done', 'Done')],
        help="state is used to separate Draft,Application,Approved,Reject,Done",
        default='draft')

    def action_confirm(self):

        if self.transfer_certificate == False:
            raise exceptions.UserError("Please Add Attachment")
        if self.state == 'draft':
            self.state = 'application'
        elif self.state == 'application':
            # Send Email for Admission
            self.env.ref('college.admission_application_email_template'
                         ).send_mail(self.id, force_send=True)
            self.state = 'done'

    def button_rejected(self):
        self.write({'state': 'reject'})
        # Send Email for Rejection
        self.env.ref('college.admission_reject_email_template').send_mail(
            self.id, force_send=True)
