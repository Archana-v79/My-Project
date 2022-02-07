from odoo import fields, models


class AcademicYear(models.Model):
    _name = "academic.year"
    _description = "accademic year"
    academic_year = fields.Selection(
        string='Accademic year',
        selection=[('2018-2021', '2018-2021'),('2019-2022', '2019-2022'), ('2020-2023','2020-2023'), ('2021-2024','2021-2024')],
        help=" Academic year is used to separate 2018-2021, ")