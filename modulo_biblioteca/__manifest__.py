{
    'name': 'Biblioteca',
    'version': '1.0',
    'summary': 'Módulo de gestión de biblioteca',
    'category': 'Library',
    'author': 'Tu Nombre',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_author_views.xml',
        'views/library_book_views.xml',
        'views/library_category_views.xml',
        'views/library_loan_views.xml',
        'views/library_user_views.xml',
        'views/views.xml',
        'views/library_menu.xml',
        'report/report_books_available.xml',
        'report/report_active_loans.xml',
        'report/report_loan_history.xml',
        'report/report_registered_users.xml',
       
       
],

   
    'installable': True,
    'application': True,
    'auto_install': False,
}
