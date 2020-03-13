# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import models, fields, api, _


# class StudentInherit(models.Model):
#     _inherit = 'sale.order'
#     subject_area = fields.Char(string="Subject area")


class teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def get_student_count(self):
        count = self.env['school.student'].search_count([('teacher_id', '=', self.id)])
        self.student_count = count

    name = fields.Char(string='Name', required=True)
    experience = fields.Integer(string="Experience")
    subject_area = fields.Char(string="Subject area", track_visibility='always')
    notes = fields.Text(string="Notes", track_visibility='always')
    image = fields.Binary(string="Image")
    name_seq = fields.Char(string='Teacher ID', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female'), ], required=True, )
    category = fields.Selection(string="Category", selection=[('first', 'First'), ('higher', 'Higher'), ],
                                required=True, )
    student_count = fields.Integer(string='Student', compute='get_student_count')
    active = fields.Boolean(string="Active", default=True)
    teacher_age = fields.Integer(compute='age_calc', store=True, string='Teacher Age')
    teacher_data = fields.Date(string="Date of Birth")
    teacher_email_id = fields.Char(string="Email")

    @api.depends('teacher_data')
    def age_calc(self):
        if self.teacher_data is not False:
            self.teacher_age = (int(datetime.today().year) - int(datetime.strftime(self.teacher_data, '%Y')))

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('school.teacher.sequence') or _('New')
        result = super(teacher, self).create(vals)
        return result

    @api.multi
    def open_teacher_student(self):
        return {
            'name': _('Student'),
            'domain': [('teacher_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'school.student',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

# добовляет вот так : name -- ST000
    @api.multi
    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s -- %s' % (rec.name, rec.name_seq)))
        return res
