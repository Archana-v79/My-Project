from odoo import fields, models, api


class ClassCollege(models.Model):
    _name = "class.college"
    # _rec_name = 'semester_name'
    _description = "class college"

    semester_name = fields.Many2one('semester.college', string="Semester Name")
    academic_year = fields.Many2one('admission.college',string="Academic Year")
    Course = fields.Many2one('admission.college',string="Course")
    # name = fields.Char(string="Name",compute='_compute_name')

    # name = fields.Char(compute='_compute_name', store="True")
    #
    #
    # @api.depends('semester_name', 'accademic_year')
    # def _compute_name(self):
    #     for record in self:
    #         record.name = record.semester_name + record.accademic_year

