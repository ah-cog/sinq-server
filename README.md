SINQ
====

SINQ (Sientific INQuery) is a project from the Human-Computer Interaction Lab at the University of Maryland, College Park.

Configure Server
================

The SINQ server depends on several software packages.  These are the Apache HTTP Server, PostgreSQL, Python, mod_wsgi, Django, Python Imaging Library (PIL), PyGreSQL.  These must be installed on the server envirnoment.  Once these are installed, they must be configured for SINQ.

Configure Django
================

Once Django has been installed and configured on your system, you must download and place this SINQ Django project on your system.  For example, on my machine, I placed it at the following location:

	/usr/local/django/sinq/

This directory contains the following:

	./README.md
	./manage.py
	./assets/
	./media/
	./sinq/
	./sinq3/
	./static/
	./templates/

To configure the Django project, create the following file:

	./sinq/local_settings.py

Alternatively, modify the settings in the file:

	./sing/settings.py

I recommend creating a the <code>./sinq/local_settings.py</code>.

Configure Apache Server
=======================

Apache must be configured for Django.  On my machine, I conifgured APache for Django by installing mod_wsgi (http://code.google.com/p/modwsgi/).  mod_wsgi is software that allows Apache to host Python web applications such as Django.  mod_wsgi does this by providing Apache an interface to Python as specified by the Web Server Gateway Interface (http://wsgi.readthedocs.org/en/latest/index.html) in PEP 333 document (http://www.python.org/dev/peps/pep-0333/).

Add the following lines to your Apache configuration file httpd.conf.

On Mac OS 10.7.5 (Lion), this file is at the following location:

	/etc/apache2/httpd.conf

The full path to this location is the following:

	/private/etc/apache2/httpd.conf

Add the following lines to your configuration file:

	Alias /robots.txt /usr/local/django/sinq/robots.txt
	Alias /favicon.ico /usr/local/django/sinq/favicon.ico
	Alias /media/ /usr/local/django/sinq/media/
	Alias /assets/ /usr/local/django/sinq/assets/
	Alias /static/ /usr/local/django/sinq/static/

Add the following:

	<Directory /usr/local/django/sinq/media/>
	Order deny,allow
	Allow from all
	</Directory>

	<Directory /usr/local/django/sinq/assets/>
	Order deny,allow
	Allow from all
	</Directory>

	<Directory /usr/local/django/sinq/static/>
	Order deny,allow
	Allow from all
	</Directory>

Add the following:

	WSGIScriptAlias / /usr/local/django/sinq/sinq/wsgi.py
	WSGIPythonPath /usr/local/django/sinq

	<Directory /usr/local/django/sinq/sinq/>
	<Files wsgi.py>
	Order deny,allow
	Allow from all
	</Files>
	</Directory>

Restart the Apache web server using the following command:

	sudo apachectl restart

(For your reference, on my system, apachectl is located at /usr/sbin/apachectl.)

RESTful HTTP API
================

