from odoo import fields, models, api


class EmpruntAS(models.Model):
    _name = 'empruntas'

    isbn = fields.Char(string='ISBN')
    nbre_pages = fields.Integer(string='Nombre de pages')
    langue_livre = fields.Selection([
        ('francais', 'Francais'),
        ('arabe', 'Arabe'),
        ('anglais', 'Anglais'),
    ], string='Langue')
    livre_id = fields.Many2one('livre', string='Livre', required=True)
    emprunt_id = fields.Many2one('emprunt', string='Emprunt', required=True)

    @api.onchange('livre_id')
    def _onchange_livre_id(self):
        if self.livre_id:
            self.isbn = self.livre_id.isbn
            self.nbre_pages = self.livre_id.nbre_pages
            self.langue_livre = self.livre_id.langue_livre
