
variable in settings
#
#
#
#

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'blog/templates/blog_static'),
    os.path.join(BASE_DIR, 'templates/css'),
)
	'blog',
	'sorl.thumbnail',
    'ckeditor',

in template
{% block head %}  {% endblock %}