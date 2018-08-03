"""
Django settings for lg project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os, sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
sys.path.insert(0, os.path.join(BASE_DIR, "extra_apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pgw1j$wc9l#v2ghoyh^gne8gbz)z^q2bykbp7hu2q_yd#fs5vf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# 替换系统的用户
AUTH_USER_MODEL = "users.UserProfile"

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DjangoUeditor',  # 富文本
    'xadmin',
    'crispy_forms',
    'users.apps.UsersConfig',
    'goods.apps.GoodsConfig',
    'trade.apps.TradeConfig',
    'user_operation.apps.UserOperationConfig',
    'rest_framework',
    'django_filters',
    'corsheaders',  # 支持跨域请求
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 允许跨域请求
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'lg.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lg.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 使用mysql
        'NAME': 'lg',  # 数据库名称
        'USER': 'root',  # 连接数据库的账号
        'PASSWORD': 'mysql',  # 连接数据库的密码
        'HOST': '127.0.0.1',  # 或者localhost，主机
        'PORT': 3306,  # 端口

    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
# 配置静态资源路径
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# 配置media的url
MEDIA_URL = "/media/"
# 加入到环境变量
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# 以后REST_FRAMEWORK的配置都在这里
REST_FRAMEWORK = {
    # rest_framework目录下的pagination.py文件PageNumberPagination类
    'DEFAULT_PAGINATION_CLASS': "rest_framework.pagination.PageNumberPagination",
    # 每页显示10条数据
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}
