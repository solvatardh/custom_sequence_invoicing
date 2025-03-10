{
    'name': 'Custom Invoice Sequence Test',
    'version': '16.0',
    'author': 'Solvatar',
    'category': 'Accounting',
    'depends': ['account'],
    'data': [
        'views/account_move_view.xml',
        'data/sequence.xml',
    ],
    'installable': True,
    'auto_install': False,
}
