py-serverdensity 1.x
===============================

About py-serverdensity
----------------------
``py-serverdensity`` is a lightweight object orientated Python library for the `Server Density API <http://developer.serverdensity.com/docs/>`_.

The library provides access to all the GET and POST methods in the SD API, takes care of authentication, allows you to post values as items in a dict, returns native Python objects from the service response, and raises exceptions for service errors.

Installation
------------
The library can be installed from PyPi using ``easy_install`` or ``pip``::

    easy_install py-serverdensity
    # or
    pip install py-serverdensity

Or cloned from `Github <http://www.github.com/>`_ using ``git``::

    git clone git://github.com/1stvamp/py-serverdensity.git
    cd py-serverdensity
    python setup.py install

Usage
-----
Once installed just import the class ``SDApi`` from the ``serverdensity.api`` module, instance the handler with your Server Density API account details, and then you can access methods on each section as attributes of the API handler::

    from serverdensity.api import SDApi, SDServiceError

    api = SDApi(
	'your_subdomain.serverdensity.com',
	'your_username',
	'your_password',
	'your_api_key'
    )
    api.alerts.getLast()
    try:
	api.devices.getByHostname({'hostName': 'myserver.somedomain.com'})
    except SDServiceError, e:
        print 'Error:', e
	print 'Response:', e.response


