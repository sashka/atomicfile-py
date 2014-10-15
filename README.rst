AtomicFile
==========

.. image:: https://travis-ci.org/sashka/atomicfile.png?branch=master
        :target: https://travis-ci.org/sashka/atomicfile

.. image:: http://img.shields.io/gratipay/sashka.svg
        :target: https://www.gratipay.com/sashka/


Writeable file object that atomically updates a file.

All writes will go to a temporary file. Call ``close()`` explicitly when you are done writing, and AtomicFile will rename the temporary copy to the original name, making the changes visible. If the object is destroyed without being closed, all your writes are discarded.

AtomicFile is friendly to ``with`` statement. ::

    from atomicfile import AtomicFile

    with AtomicFile("panic.txt", "w") as f:
        f.write(json.dumps(big_data_array_100MB, sort_keys=True, indent=4))


Install
-------
To install AtomicFile, simply: ::

    pip install atomicfile

