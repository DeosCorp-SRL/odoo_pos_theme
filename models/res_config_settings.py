# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    logo_image = fields.Binary('POS Logo')
    theme_configuration_id = fields.Many2one('pos.theme.config',"Theme Configuration")
    floor_Background = fields.Binary('POS floor background')

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    pos_logo_image = fields.Binary(related='pos_config_id.logo_image',readonly=False) 
    pos_theme_configuration_id = fields.Many2one('pos.theme.config',"Theme Configuration",related='pos_config_id.theme_configuration_id',readonly=False)
    pos_floor_background = fields.Binary('POS floor background',related="pos_config_id.floor_Background",readonly=False)