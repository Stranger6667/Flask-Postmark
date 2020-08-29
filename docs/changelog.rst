.. _changelog:

Changelog
=========

`Unreleased`_
-------------

`0.3.0`_ - 2020-08-29
---------------------

Added
~~~~~

- Type annotations.

Changed
~~~~~~~
- Raise `RuntimeError` if context stack is empty when you try to use `Postmark.client`.

Removed
~~~~~~~

- Support for Python 2.6, 2.7, 3.3, 3.4.

`0.2.0`_ - 2017-06-10
---------------------

Added
~~~~~

- Register the extension on the app. `#6`_
- Use ``self.app`` as a fallback. `#5`_

0.1.0 - 2017-05-11
------------------

- Initial release.

.. _Unreleased: https://github.com/Stranger6667/Flask-Postmark/compare/v0.3.0...HEAD
.. _0.3.0: https://github.com/Stranger6667/Flask-Postmark/compare/0.2.0...v0.3.0
.. _0.2.0: https://github.com/Stranger6667/Flask-Postmark/compare/0.1.0...0.2.0


.. _#6: https://github.com/Stranger6667/Flask-Postmark/issues/6
.. _#5: https://github.com/Stranger6667/Flask-Postmark/issues/5
