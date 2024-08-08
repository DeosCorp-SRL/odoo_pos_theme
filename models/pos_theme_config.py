from odoo import api, fields, models


class PosThemeConfig_view(models.Model):
    """Model for storing configuration settings related to the theme"""
    _name = 'pos.theme.config'
    _description = "Model for storing configuration settings related to the " \
                   "theme"

    name = fields.Char(string="Name")
    theme_primary_color = fields.Char(related="p_color_picker",string="Primary color", help="Primary color")
    p_color_picker = fields.Char(string="Color Picker")
    theme_secondary_color = fields.Char(related="s_color_picker",string="Secondary color", help="Secondary color")
    s_color_picker = fields.Char(string="Color Picker")
    theme_active = fields.Boolean(string="Active",default=False)

    def action_deactive_theme(self): 
        for rec in self:
            rec.theme_active = False
    
    def action_active_theme(self):  
        for rec in self:
            rec.theme_active = True
    
