from odoo import models, fields, api

class Auteur(models.Model):
    _name = 'auteur'
    _rec_name = 'nom'

    nom = fields.Char(String="Nom", required=True)
    prenom = fields.Char(String="Prenom", required=True)
    date_naissance = fields.Date(String="Date de naissance")
    nationalite = fields.Char(String="Nationalite", default="Algerienne")
    sexe = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme')
    ])
    livre_ids = fields.Many2many('livre','auteur_ids', string="Livres")