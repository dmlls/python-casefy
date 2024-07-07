Casefy — String casing utilities
================================

Casefy is a lightweight Python package to convert the casing of strings. It has
no dependencies and supports Unicode characters.

You can find the project repository on `GitHub
<https://github.com/dmlls/python-casefy>`_. Any improvements are welcome!

Installation
------------

The latest release can be installed using `pip <https://pypi.org/project/pip/>`_:

.. code-block:: shell

   pip install -U casefy


Examples
--------

.. note::

   For more details, you can check the :ref:`api`.

.. code-block:: python

   import casefy

   # camelCase
   string = casefy.camelcase("foo_bar")
   print(string)  # fooBar

   string = casefy.camelcase("FooBar")
   print(string)  # fooBar

   string = casefy.camelcase("FOO BAR")
   print(string)  # fooBar

   # snake_case
   string = casefy.snakecase("fooBar")
   print(string)  # foo_bar
    
   string = casefy.snakecase("fooBARbaz", keep_together=["bar"])
   print(string)  # foo_bar_baz
   
   string = casefy.snakecase("FOO BAR")
   print(string)  # foo_bar

   # CONST_CASE
   string = casefy.constcase("fooBar")
   print(string)  # FOO_BAR
   
   # kebab-case
   string = casefy.kebabcase("fooBar")
   print(string)  # foo-bar
   
   # separator case
   string = casefy.separatorcase("fooBar", separator="/")
   print(string)  # foo/bar

   string = casefy.separatorcase("fooBARbaz", separator="%", keep_together=["bar"])
   print(string)  # foo%bar%baz

   # Sentence case
   string = casefy.sentencecase("fooBar")
   print(string)  # Foo bar


Contents
--------

.. toctree::
   :maxdepth: 2

   api


License
-------
This project is distributed under the `MIT
<https://github.com/dmlls/python-casefy/blob/main/LICENSE>`_ license.
