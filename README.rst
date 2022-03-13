Locust odoorpc
==============

Links
-----

* Locust: https://locust.io/
* Locust docs: https://docs.locust.io/
* OdooRPC: https://pythonhosted.org/OdooRPC/
* Source code: https://github.com/camptocamp/locustodoorpc
* Alternative: https://github.com/nseinlet/OdooLocust (using ``openerplib`` instead of ``odoorpc``)

Description
-----------

This is a clone from `locustodoorpc <https://github.com/camptocamp/locustodoorpc>`_ , i also updated the code because some classes in locust are deprecated and replaced by other classes.
Locust custom client integrating the `odoorpc <https://github.com/osiell/odoorpc>`_ library, so you can run load-testing on your odoo services. Have a look at the feature list of `locust <https://github.com/locustio/locust/#description>`_ to see what you can do.

Installation
------------

::

  virtualenv .env
  source .env/bin/activate
  pip install locustodoorpc

Usage
-----

For the general documentation on Locust, heads on https://docs.locust.io/en/latest/
A few options can be customized with environment variables:

+--------------+-------------------------------------------------------------+
|Name          |Usage                                                        |
+--------------+-------------------------------------------------------------+
|ODOO_DB_NAME  |Configure the name of the database to load-test              |
|              |(default: odoo)                                              |
+--------------+-------------------------------------------------------------+
|ODOO_LOGIN    |Login to use for the actions (default: admin)                |
+--------------+-------------------------------------------------------------+
|ODOO_PASSWORD |Password for the user (default: admin)                       |
+--------------+-------------------------------------------------------------+
|ODOO_VERSION  |Force an Odoo version (e.g. 9.0, 10.0, 11.0), normally       |
|              |automatically recognized                                     |
+--------------+-------------------------------------------------------------+

Examples::

  ODOO_DB_NAME=demo locust -f examples/locustfile.py --host http://localhost:8069
  ODOO_DB_NAME=testing locust --headless -f examples/locustfile.py -H http://localhost -r 1 -u 10 -t 60 --html report.html 


Using Dockerfile::

  Docker build . -t locustodoo
  docker run --env ODOO_DB_NAME=testing --network=host -v $PWD:/mnt/locust -w /mnt/locust locustodoo locust --headless -f examples/locustfile.py -H http://localhost -r 1 -u 10 -t 60 --html report.html



Check the `examples <https://gitlab.com/atarekmokhtar90/locustodoorpc/-/tree/main/examples>`_

.. image:: https://raw.githubusercontent.com/camptocamp/locustodoorpc/master/images/locustodoorpc.png

