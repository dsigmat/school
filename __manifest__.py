# -*- coding: utf-8 -*-
{
    'name': "School",

    'summary': """
        Some study here, others work.""",

    'description': """
        School is a small life in which every adult lives at the same time. This is one of the main stages of our lives. Everything in the world begins with small, everything is born small, and then grows: a small sprout turns into a big tree, a stream flows into a river, words turn into sentences and big novels, great melodies consist of several notes. And here we are: we begin to study life at school. And then, in adulthood, we rely on our mind and the knowledge we gained at school. Thus, general education is simply necessary.
    """,

    'author': "Denis Sidorov",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/data.xml',
        'views/teacher.xml',
        'views/student.xml',
        'views/academic_subject.xml',
        'views/school_notes.xml',
        'reports/report.xml',
        'reports/teacher_card.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
