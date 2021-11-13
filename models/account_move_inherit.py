# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _


class AccountMove(models.Model):
    _inherit='account.move'

    file = fields.Binary(string="File")
    file_name = fields.Char(string="File Name")

