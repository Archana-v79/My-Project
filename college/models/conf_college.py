from odoo import fields, models

class ConfCollege(models.Model):
    _name = "conf.college"
    _description = "conf college"


    name = fields.Char(required=True)
    Catogory = fields.Char()
    Duration_years = fields.Integer()
    semesters = fields.Char()
    Semester = fields.Char()