from distutils.core import setup, Extension

module_spam = Extension('spam',sources=['spammodule.c'])
setup(
    name = 'School_Bell_Ring',
    version='1.0',
    py_modules=['School_Bell_Ring','noti','teller'],
    packages=['image','xml'],
    package_data = {'image': ['*.png'],'xml':['*.xml']},

    ext_modules=[module_spam]
)