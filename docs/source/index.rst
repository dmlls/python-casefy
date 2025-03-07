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

   # Alphanum3ric case (removes non-alphanumeric chars)
   string = casefy.alphanumcase("foo - 123 ; bar!")
   print(string)  # foo123bar

   # camelCase
   string = casefy.camelcase("foo_bar")
   print(string)  # fooBar

   string = casefy.camelcase("FooBar")
   print(string)  # fooBar

   string = casefy.camelcase("FOO BAR")
   print(string)  # fooBar

   # Capital Case
   string = casefy.capitalcase("fooBar")
   print(string)  # FooBar

   # CONST_CASE
   string = casefy.constcase("fooBar")
   print(string)  # FOO_BAR

   # kebab-case
   string = casefy.kebabcase("fooBar")
   print(string)  # foo-bar

   # lowercase
   string = casefy.lowercase("fooBar")
   print(string)  # foobar

   # PascalCase
   string = casefy.pascalcase("foo_bar")
   print(string)  # FooBar

   string = casefy.pascalcase("fooBar")
   print(string)  # FooBar

   # Sentence case
   string = casefy.sentencecase("fooBar")
   print(string)  # Foo bar

   # Separator case
   string = casefy.separatorcase("fooBar", separator="/")
   print(string)  # foo/bar

   string = casefy.separatorcase("fooBARbaz", separator="%", keep_together=["BAR"])
   print(string)  # foo%bar%baz

   # snake_case
   string = casefy.snakecase("fooBar")
   print(string)  # foo_bar

   string = casefy.snakecase("fooBARbaz", keep_together=["BAR"])
   print(string)  # foo_bar_baz

   string = casefy.snakecase("FOO BAR")
   print(string)  # foo_bar

   # Title Case
   string = casefy.titlecase("fooBarBaz")
   print(string)  # Foo Bar Baz

   # UPPERCASE
   string = casefy.uppercase("fooBar")
   print(string)  # FOOBAR

   # UPPER-KEBAB-CASE
   string = casefy.upperkebabcase("fooBar")
   print(string)  # FOO-BAR

Contents
--------

.. toctree::
   :maxdepth: 2

   api


License
-------
This project is distributed under the `MIT
<https://github.com/dmlls/python-casefy/blob/main/LICENSE>`_ license.
