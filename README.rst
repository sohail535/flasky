======
Fasak
======

Trying to understand how python web frameworks work by copying the famous *flask* micro framework.

How to install?
---------------

Create a ``virtual env`` and install ``flit``

.. code-block::

    $ pip install flit
    $ git clone git@gitlab.com:sohailsha1/fasak.git
    $ cd fasak
    $ flit install --symlink

How to use it?
--------------

.. code-block:: python

    # hello.py
    from fasak import Fasak

    class Hello:
        def GET(self):
            return 'fasakkk!!'

    class Greet:
        def GET(self, message):
            return 'Hello ' + message + '!!'

    urls = [
        ('/', Hello),
        ('/greet/<message>', Greet)
    ]

    app = Fasak(urls)

    if __name__ == '__main__':
        app.debug = True
        app.run()

Now run ``python hello.py``
