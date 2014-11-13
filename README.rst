python-autocast-decorator
=========================

Decorator for automatically casting string inputs to their most likely Python data types.

This implementation runs ``ast.literal_eval()`` on all inputs. This is simple and reliable, but fairly slow, and therefore probably inappropriate for code that must run fast.

This decorator uses `wrapt <https://github.com/GrahamDumpleton/wrapt>`__ to enable signature-preserving decoration.

For more discussion, see https://stackoverflow.com/questions/7019283/automatically-type-cast-parameters-in-python

.. code:: python

    from autocast import autocast
    
    @autocast
    def my_function(arg):
        print(type(arg))
        
    >>> my_function('3')
    <type 'int'>

Contribute
----------

If you like this module, please contribute! I welcome patches,
documentation, issues, ideas, and so on.
