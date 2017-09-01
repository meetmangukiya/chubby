chubby
======

Installation
------------

.. code:: bash

   pip install chubby

Features
--------

Issues
~~~~~~

.. code:: python

    # creating new issues
    chubby issue -t "This is the issue title" -d "This is the issue description" -r "meetmangukiya/chubby"
    # Edit issues
    chubby issue -t "This is the new issue title" -r "meetmangukiya/chubby" -n 23
    # get issue data
    chubby issue -n 23 -r "meetmangukiya/chubby"

For complete help, please use ``chubby issue -h``

Config
~~~~~~

Once you have installed chubby its time to configure it. Chubby uses GitHub
personal access tokens to carry out all this actions on behalf of the user.
Hence, you need to add it,

.. code:: bash

    chubby config -t "<this is your github acess token>"
    chubby config -h # to get help
