# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import models, fields, api, _


class CreateStudent(models.TransientModel):
    _name = 'create.student'

    teacher_id = fields.Many2one('school.teacher', string='Teacher')
    student_date = fields.Date(string="Student Date", required=False, )

    @api.multi
    def create_student(self, vals):
        print('Hello world')
        vals = {
            'teacher_id': self.teacher_id.id,
            'student_date': self.student_date
        }
        self.env['school.student'].create(vals)
