from general_settings import *
CKEDITOR_UPLOAD_PATH = pth(MEDIA_ROOT, '/uploads/')
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full', # Other Option is 'Full'
        'toolbar_Full': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
            ['Image', 'Syntaxhighlight', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'], ['Source'],
            ],
        'extraPlugins': 'syntaxhighlight',
        'height': 300,
        'width': 0, # Full Width

    },
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine', # If Whoosh is used,
        #     pip install whoosh
        'PATH': pth(BASE_DIR,'bootlog/whoosh_index'),
        }
}

INSTALLED_APPS += (#'bootlog',
                   'ckeditor',)