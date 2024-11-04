from odoo import fields, models, api

class Emprunteur(models.Model):
    _name = 'emprunteur'
    _rec_name = 'nom'

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prenom', required=True)
    date_naissance = fields.Date(string='Date de naissance', required=True)
    state = fields.Char(string='Etat')
    sexe = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    ])
    nbr_emprunt = fields.Integer(string='Nombre d\'emprunts', compute='_compute_nbr_emprunt')

    emprunt_ids = fields.One2many('emprunt', 'emprunteur_id', string='Emprunts', required=True)
    @api.depends('emprunt_ids')
    def _compute_nbr_emprunt(self):
        for record in self:
            print("record", record)
            record.nbr_emprunt = len(record.emprunt_ids)