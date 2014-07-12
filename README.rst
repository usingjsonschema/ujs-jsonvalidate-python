=====================
JSON Validate Utility
=====================

Part of the
`Using JSON Schema <http://usingjsonschema.github.io>`_
project.

``jsonvalidate`` is a command line and library utility allowing JSON content
to be validated using JSON Schema content from local or remote sources, and
use of custom schema storage and URI access.

The utility uses the
`jsonschema <https://pypi.python.org/pypi/jsonschema>`_
library for the schema validation processing
(`GitHub repo <https://github.com/Julian/jsonschema>`_).

For command line/script use, a console message is displayed and the process
exits with 0 for success, 1 for failure.

.. image:: https://travis-ci.org/usingjsonschema/ujs-jsonvalidate-python.svg?branch=master
    :target: https://travis-ci.org/usingjsonschema/ujs-jsonvalidate-python

Command Line / Script Use
-------------------------

To run the validation (command line or script), use the ``validate``
command with a file name (path optional). For example, to check the file
``example.json`` against the schema ``example_schema.json``, use,

.. code:: bash

    validate example.json example_schema.json

Library Function Use
--------------------

**validate** (dataFile, schemaFile, refFiles, jsdbFile, callback)

| Arguments:
|     dataFile *String* File name of JSON data file (path optional)
|     schemaFile *String* File name of JSON Schema file (path optional)
|     refFiles *String[]* Array of file names for $ref files (path optional)
|     jsdbFile *String* File name for JSDB file (path optional)
|
| Returns:
|     code, data, message
|
|     - *code* is the validation result
|     - *data* is the validated JSON content from dataFile
|     - *message* is text message associated with the *code*

For example,

.. code:: python

    from jsonvalidate import validate, VALID

    dataFile = "example.json"
    schemaFile = "example_schema.json"
    refFiles = ["ref1_schema.json", "ref2_schema.json"]
    jsdbFile = None

    code, data, message = validate (dataFile, schemaFile, refFiles, jsdbFile)
    if code == VALID:
        print ("Valid JSON content");
    else:
        print ("Error: " + str (message))

Installation
------------

The program can be installed using ``pip``, with the command,

.. code:: bash

    pip install ujs-jsonvalidate

License
-------

MIT