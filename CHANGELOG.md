# Changelog

## [Unreleased](https://github.com/Stranger6667/Flask-Postmark/compare/v0.3.1...HEAD)

### Added

- Support for Python 3.11–3.15.

### Changed

- Require Flask 3.0 or newer and postmarker 2.0 or newer.

### Removed

- Support for Python 3.5–3.10.

### Fixed

- `ImportError` on Flask 2.3+, where `_app_ctx_stack` was removed. [#20](https://github.com/Stranger6667/Flask-Postmark/issues/20)

## [0.3.1](https://github.com/Stranger6667/Flask-Postmark/compare/v0.3.0...v0.3.1) - 2020-08-29

### Fixed

- Documentation on Read The Docs.

## [0.3.0](https://github.com/Stranger6667/Flask-Postmark/compare/0.2.0...v0.3.0) - 2020-08-29

### Added

- Type annotations.

### Changed

- Raise `RuntimeError` if context stack is empty when you try to use `Postmark.client`.

### Removed

- Support for Python 2.6, 2.7, 3.3, 3.4.

## [0.2.0](https://github.com/Stranger6667/Flask-Postmark/compare/0.1.0...0.2.0) - 2017-06-10

### Added

- Register the extension on the app. [#6](https://github.com/Stranger6667/Flask-Postmark/issues/6)
- Use `self.app` as a fallback. [#5](https://github.com/Stranger6667/Flask-Postmark/issues/5)

## 0.1.0 - 2017-05-11

- Initial release.
