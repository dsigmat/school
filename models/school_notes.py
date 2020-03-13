# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SchoolNotes(models.Model):
    _name = 'school.notes'
    _description = 'Memorable Notes'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'full_name'

    full_name = fields.Char(string='Name', required=True)
    notes = fields.Text(string="Notes", required=False, )

