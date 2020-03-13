# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import models, fields, api, _


class student(models.Model):
    _name = 'school.student'
    _description = 'Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'
    _rec_name = 'full_name'

    full_name = fields.Char(string='Name', required=True)
    address = fields.Text(string="Address", required=False, track_visibility='always')
    phone = fields.Text(string="Phone", required=False, )
    student_data = fields.Date(string="Date of Birth")
    resume_student = fields.Text(string="Note", required=False, track_visibility='always')
    active = fields.Boolean(string="Active", default=True)
    image = fields.Binary(string="Image")
    name_seq = fields.Char(string='Student ID', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    student_age = fields.Integer(compute='age_calc', store=True, string='Student Age')
    teacher_id = fields.Many2one(comodel_name="school.teacher", string="Classroom Teacher", required=True, )
    teacher_age = fields.Integer(string="Age", related='teacher_id.teacher_age')
    teacher_image = fields.Binary(string="Image", related='teacher_id.image')
    student_lines = fields.One2many("school.student.lines", "student_id",
                                    string="Student Lines", required=False, )
    student_email_id = fields.Char(string="Email")



    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('school.student.sequence') or _('New')
        result = super(student, self).create(vals)
        return result

    @api.depends('student_data')
    def age_calc(self):
        if self.student_data is not False:
            self.student_age = (int(datetime.today().year) - int(datetime.strftime(self.student_data, '%Y')))


class SchoolStudentLines(models.Model):
    _name = 'school.student.lines'
    _description = 'Student Lines'

    notes_id = fields.Many2one("school.notes", string="Notes")
    student_id = fields.Many2one("school.student", string="Student ID")
    notes_data = fields.Date(string="Date of Note")
