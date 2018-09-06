======
Flasky
======

Trying to understand how python web frameworks work by copying the famous `flask` micro framework.

How to install?
---------------

**This is not supposed to be used anywhere**, so install it on your own interest.

Make sure you use it in a **virtual env**.

.. code-block::

    pip install flit
    git clone git@gitlab.com:sohailsha1/flasky.git
    cd flasky
    flit install --symlink
    
How to use it?
--------------

.. code-block:: python

    # hello.py
    from flasky import Flasky
    
    class Hello:
        def GET(self):
            return 'Hello world!!'
    
    class Greet:
        def GET(self, message):
            return 'Hello ' + message + '!!'
            
    urls = [
        ('/', Hello),
        ('/greet/<message>', Greet)
    ]
    
    app = Flasky(urls)
    
    if __name__ == '__main__':
        app.debug = True
        app.run()

Now run ``python hello.py``
