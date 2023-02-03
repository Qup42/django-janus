from setuptools import setup, find_packages
from janus import __version__


setup(
    name="django-janus",
    version='.'.join(str(x) for x in __version__),
    license="BSD",
    description="Janus is a Single sign-on (SSO) system based on django.",
    author="Daniel Leinfelder",
    author_email="daniel@smart-lgt.com",
    url="https://github.com/smartlgt/django-janus",
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=3.2,<4.1",
        "django-oauth-toolkit @ git+https://github.com/Qup42/django-oauth-toolkit@feature/oidc-rp-initiated-logout#egg=django-oauth-toolkit==2.2.0",
        "django-cors-middleware>=1.5.0",
        "django-allauth>=0.48.0",
        "django-fakeinline>=0.1.1",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        "Framework :: Django",
    ]
)
