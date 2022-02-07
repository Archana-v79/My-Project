from odoo import fields, models


class SemesterCollege(models.Model):
    _name = "semester.college"
    _description = "semester college"


    semester_name = fields.Char()

    Number_Semesters = fields.Integer()
    Course = fields.Char()
    syllabus = fields.One2many('syllabus','syllabus_id')
class Syllabus(models.Model):
    _name = "syllabus"
    _description = "syllabus"

    syllabus_id = fields.Many2one('semester.college', string='syllabus')
    subject = fields.Char()
    max_mark = fields.Integer()

