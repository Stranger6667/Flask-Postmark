---
name: Bug report
about: Create a report to help us improve
title: "[BUG]"
labels: 'Status: Review Needed, Type: Bug'
assignees: Stranger6667

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
A minimal test that reproduces the problem, and the full traceback if there is one.

```python
from flask import Flask
from flask_postmark import Postmark

app = Flask(__name__)
app.config["POSTMARK_SERVER_TOKEN"] = "..."
postmark = Postmark(app)
```

**Expected behavior**
A clear and concise description of what you expected to happen.

**Environment (please complete the following information):**

- OS: [e.g. Linux or Windows]
- Python version: [e.g. 3.13.1]
- Flask version: [e.g. 3.1.3]
- Postmarker version: [e.g. 3.0]
- Flask-Postmark version: [e.g. 1.0.0]

**Additional context**
Add any other context about the problem here.
