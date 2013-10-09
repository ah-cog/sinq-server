SINQ
====
SINQ (Scientific INQuery) is a project from the Human-Computer Interaction Lab at the University of Maryland, College Park.



## 1. Installation

### 1.1 Get Requirements

The SINQ server environment requires several packages to be installed.  They are:

- PostgreSQL
- Apache HTTP Server
	- mod_wsgi
- Python
	- Django
	- Python Imaging Library (PIL)
	- PyGreSQL


The [`mod_wsgi`](http://code.google.com/p/modwsgi/) module provides Apache with the [Web Server Gateway Interface](http://wsgi.readthedocs.org/en/latest/). 
Apache uses this interface to talk to Django, as described in [PEP 333](http://www.python.org/dev/peps/pep-0333/).


### 1.2. Download SINQ

Download this project.  On POSIX, Linux, or OS X, we recommend downloading to this location:  

	/usr/local/django/sinq/

The directory should contain the following:

	./assets/
	./media/
	./sinq/
	./sinq3/
	./static/
	./templates/
	./README.md
	./manage.py


## 2. Configuration

Once you’ve got the requirements installed, they must be configured for SINQ.


### 2.1. Configure Django

* **Recommended:**
    - Create `./sinq/local_settings.py`
* **(experts only) Alternative:**
	- Edit `./sing/settings.py`
	- Unless you _really_ know what you’re doing, you probably shouldn’t do this. <br />
	  _Choose this method at your own risk.  You’ve been warned._


#### 2.2. Configuration Apache

Apache’s configuration file is `httpd.conf`.  You’ll need to make a few modifications to it.  

On OS X 10.7 (Lion), this file is at the following location `/etc/apache2/httpd.conf`.

Add the following to `httpd.conf`:

	Alias /robots.txt /usr/local/django/sinq/robots.txt
	Alias /favicon.ico /usr/local/django/sinq/favicon.ico
	Alias /media/ /usr/local/django/sinq/media/
	Alias /assets/ /usr/local/django/sinq/assets/
	Alias /static/ /usr/local/django/sinq/static/

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

	WSGIScriptAlias / /usr/local/django/sinq/sinq/wsgi.py
	WSGIPythonPath /usr/local/django/sinq

	<Directory /usr/local/django/sinq/sinq/>
	<Files wsgi.py>
	Order deny,allow
	Allow from all
	</Files>
	</Directory>


#### 2.3. Restart Apache

The `apachectl` (“Apache Control”) program is used to control Apache. (Surprising, huh?)
On my system, it’s located at `/usr/sbin/apachectl`.

Run the following:

	sudo apachectl restart

----

## RESTful HTTP API

...
