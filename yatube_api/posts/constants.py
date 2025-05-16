"""Константы для приложения posts."""

# Models
GROUP_TITLE_MAX_LENGTH = 200
COMMENT_STR_LENGTH = 15
POST_IMAGE_UPLOAD_PATH = 'posts/'

# Field Names
POSTS_RELATED_NAME = 'posts'
COMMENTS_RELATED_NAME = 'comments'
FOLLOWS_RELATED_NAME = 'follows'

# Model Verbose Names
POST_PUB_DATE_VERBOSE = 'Дата публикации'
COMMENT_CREATED_VERBOSE = 'Дата добавления'

# Admin
EMPTY_VALUE_DISPLAY = '-пусто-'

# Follow Model Constraints
UNIQUE_FOLLOW_CONSTRAINT = 'unique_follow'
