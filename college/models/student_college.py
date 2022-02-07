from odoo import fields, models

class StudentCollege(models.Model):
    _name = "student.college"
    _description = "student college"


    admission_no = fields.Char()
    admission_date = fields.Date()
    first_name = fields.Char(required=True)
    second_name = fields.Char(required=True)
    father = fields.Char()
    mother = fields.Char()
    communication_address = fields.Char()
    permanent_address = fields.Char()
    used = fields.Boolean(string='Same as Communication Address')
    phone = fields.Char()
    email = fields.Char()



