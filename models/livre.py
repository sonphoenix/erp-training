from odoo import fields, models, api


class Livre(models.Model):
    _name = 'livre'
    _rec_name = 'titre'

    titre = fields.Char(string='Titre', required=True)
    langue_livre = fields.Selection([
        ('francais', 'Français'),
        ('arabe', 'Arabe'),
        ('anglais', 'Anglais'),
    ], string='Langue')
    isbn = fields.Char(string='ISBN')
    nbre_pages = fields.Integer(string='Nombre de pages')
    image_livre = fields.Char(string='Image')

    auteur_ids = fields.Many2many('auteur', 'livre_ids', string='Auteurs', required=True)
    empruntas_ids = fields.One2many('empruntas', 'livre_id', string='Lignes d\'emprunt', required=True)