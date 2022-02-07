{
    'name': 'College',
    'depends': ['base','mail'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/student_college_views.xml',
        'views/admission_college_views.xml',
        'views/class_college_views.xml',
        'views/conf_college_views.xml',
        'views/semester_college_views.xml',
        'views/exam_college_views.xml',

        'views/email1_college_views.xml',
        'views/email2_college_views.xml',

        'views/college_menu.xml',

    ]
}
