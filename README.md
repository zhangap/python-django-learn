# 目录结构：
HelloWorld/
├── apps/               # 推荐：存放所有自定义应用
│   └── blog/          # 示例应用
├── static/             # 静态文件（CSS/JS/图片）
├── media/              # 用户上传文件
├── templates/          # 全局模板目录
└── requirements.txt    # 项目依赖列表



# 关键配置项详解：
DEBUG = True  # 开发时设为True，显示详细错误；生产环境必须改为False
ALLOWED_HOSTS = []  # DEBUG=False时需指定允许访问的域名（如['example.com']）

INSTALLED_APPS = [
    'django.contrib.admin',    # 后台管理
    'django.contrib.auth',     # 认证系统
    'django.contrib.contenttypes',  # 内容类型框架
    'django.contrib.sessions', # 会话管理
    'django.contrib.messages', # 消息框架
    'django.contrib.staticfiles',  # 静态文件管理
    # 可添加自定义应用：'myapp.apps.MyAppConfig'
]

DATABASES = {  # 数据库配置
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # 使用 pathlib 语法
        # MySQL示例：
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'mydb',
        # 'USER': 'root',
        # 'PASSWORD': 'password',
    }
}

STATIC_URL = '/static/'  # 静态文件URL前缀
STATICFILES_DIRS = [BASE_DIR / 'static']  # 开发时静态文件搜索目录
MEDIA_URL = '/media/'   # 用户上传文件URL前缀
MEDIA_ROOT = BASE_DIR / 'media'  # 上传文件存储路径



#在后端接口已经允许跨域的情况下，浏览器要解决跨域操作，可以按如下进行配置
# Windows
chrome.exe --disable-web-security --user-data-dir="C:/ChromeDevSession"

# MacOS
open -n -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --args --user-data-dir="/tmp/chrome_dev_test" --disable-web-security

# Linux
google-chrome --disable-web-security --user-data-dir="/tmp/chrome_dev_test"