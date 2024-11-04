from odoo import fields, models, api

class Emprunt(models.Model):
    _name = 'emprunt'

    date_debut = fields.Date(string='Date de debut', required=True, default=fields.Date.context_today, readonly=True)
    date_fin = fields.Date(string='Date de fin', required=True)

    rendu = fields.Boolean(string='Rendu', compute='_compute_rendu')

    emprunteur_id = fields.Many2one('emprunteur', string='Emprunteur', required=True)
    empruntas_ids = fields.One2many('empruntas', 'emprunt_id', string='Lignes d\'emprunt', required=True)

    @api.depends('date_fin')
    def _compute_rendu(self):
        for record in self:
            if record.date_fin < fields.Date.today():
                record.rendu = True
            else:
                record.rendu = False