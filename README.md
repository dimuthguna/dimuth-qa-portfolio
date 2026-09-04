# QA Portfolio — Dimuth Anjuka

QA Analyst (ISTQB® CTFL v4.0) building hands-on automation and testing
depth through a structured, self-paced upskilling plan alongside
full-time work.

## Status

This portfolio is being built progressively, phase by phase — each
item below is real, working content once checked off, not a placeholder.

- [x] Test case design & documentation (SauceDemo) — Login flow complete (5 test cases executed, 2 gaps identified for follow-up)
- [x] SQL data-validation queries — 8 queries covering filtering, joins (referential integrity), aggregation, and NULL handling, including 2 schema-verification errors caught and resolved
- [x] API test collection (Postman) — 5 requests (GET/POST/PUT/DELETE + 404 case), 3 with automated status-code assertions
- [x] Performance test (JMeter) — 10 concurrent users, 50 requests against JSONPlaceholder API, 0.00% error rate, 16ms average response time
- [x] Jira Scrum project (sprint planning, backlog, defect tracking) — active sprint with 5 issues (3 stories, 2 bugs), 2 groomed backlog items traced to identified test gaps, defects cross-linked to bug-reports/
- [x] Automated UI test suite (Playwright) — 5 test cases automating SauceDemo login scenarios from test-cases/, run across Chromium/Firefox/WebKit (15 total test runs, all passing) — see [saucedemo-playwright-tests](https://github.com/dimuthguna/saucedemo-playwright-tests)
- [x] CI pipeline (GitHub Actions) running the suite on every push — verified working, tests run automatically in the cloud on push
- [x] Python login checker — text-based login simulator with a three-attempt lockout, exit code and retry logic
- [x] SQLite test-results database — stores test name, pass/fail status, and timestamp using Python's sqlite3 library, queried back to confirm storage
- [x] Jira JQL queries — three saved queries (filter by status, filter by bug type, sort by priority) plus a named "Open Bugs" filter for ongoing defect triage
## About

Currently working as a QA Analyst validating deliverables for
wastewater treatment projects — defining acceptance criteria, running
functional and data-integrity checks, and maintaining a defect log
through to resolution. This repository is where the hands-on
automation and tooling side of that work is being built and
demonstrated.

Connect: [LinkedIn](https://linkedin.com/in/dimuthanjuka)
