{
    'name': 'gestion de bibliotheque',
    'description': "yes",
    'category':'bibliotheque',
    'author': 'Omar Ferradj',
    'depends': ['project'],
    'version': '1.0',
    'data': [
        'security/ir.model.access.csv',
        'views/emprunt.xml',
        'views/auteur.xml',
        'views/livre.xml',
        'views/emprunteur.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}