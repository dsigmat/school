# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class AcademicSubject(models.Model):
    _name = 'school.academic'
    _description = 'Academic Subject'

    name = fields.Char(string='Name')