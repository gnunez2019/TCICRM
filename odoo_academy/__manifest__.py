# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    
    'summary': """Academy app to mange Training""",
    
    'description': """
        Academy Module to mange Training:
        - Courses
        - Sessions
        - Attendees
    """,
    'author':'Odoo',
    
    'website':'http://www.odoo.com',
    
    'category':'Training',
    'version':'0.1',
    
    'license':'LGPL-3',
    
    'depends':['base'],
    
    'data':[
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        #'security/model_groups.xml',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
    ],
    'demo':[
        'demo/academy_demo.xml',
    
    ],
}