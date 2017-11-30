======
Flasky
======

This is a reference implementation of `Flask
<https://github.com/pallets/flask>`_, not to be used in any **production** code.

Im doing this so as to get to know how web frameworks are build in python.

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

.. code-block::

    # hello.py
    from flasky import Flasky
    
    class Hello:
        def GET(self):
            return 'Hello world!!'
    
    urls = [
        ('/', Hello)
    ]
    
    app = Flasky(urls)
    
    if __name__ == '__main__':
        app.debug = True
        app.run()

Now run ``python hello.py``