
**Application under test:** https://www.saucedemo.com/
**Feature:** Login
**Technique applied:** Equivalence Partitioning, supported by decision-table analysis
**Author:** Dimuth Anjuka
**Date:** 25 Aug 2026

## Note on technique choice

Boundary Value Analysis was considered but not applied here — the login fields have no
documented length or character constraints to test boundaries against. BVA will be applied
later against fields that do have defined limits (e.g. quantity fields at checkout).

## Input analysis

**Username — equivalence classes identified:**

| Class | Description | Example |
|---|---|---|
| Valid & active | Listed username, account not locked | `standard_user`, `problem_user`, `performance_glitch_user`, `error_user`, `visual_user` |
| Valid & locked | Listed username, account locked | `locked_out_user` |
| Invalid / unrecognized | Not in the listed set | `foo` |
| Empty | No value entered | *(blank)* |

**Password — equivalence classes identified:**

| Class | Description |
|---|---|
| Correct | Matches `secret_sauce` |
| Incorrect | Any non-matching value |
| Empty | No value entered |

## Decision table

| # | Username class | Password class | Expected result | Verified? |
|---|---|---|---|---|
| 1 | Empty | Empty | "Epic sadface: Username is required" | Yes |
| 2 | Invalid/unrecognized | Any | "Epic sadface: Username and password do not match any user in this service" | Yes |
| 3 | Valid & active | Incorrect | Same generic "do not match" error as row 2 | Yes |
| 4 | Valid & locked | Correct | "Epic sadface: Sorry, this user has been locked out." | Yes |
| 5 | Valid & active | Correct | Login succeeds — Products page displayed | Yes |
| 6 | Valid & locked | Incorrect | Not yet determined — does locked-out check win, or does password check? | **Not yet executed** |
| 7 | Valid & active | Empty | Not yet determined | **Not yet executed** |

Rows 6 and 7 are identified gaps in coverage, included here deliberately rather than left
out, since spotting untested combinations is part of the exercise.

## Test cases

### TC-LOGIN-01 — Login fails with empty username and password
- **Preconditions:** Browser open at https://www.saucedemo.com/
- **Test data:** Username: *(blank)*, Password: *(blank)*
- **Steps:**
  1. Leave both fields empty
  2. Click "Login"
- **Expected result:** Error message displayed: "Epic sadface: Username is required"
- **Actual result:** As expected
- **Status:** Pass

### TC-LOGIN-02 — Login fails with an unrecognized username
- **Preconditions:** Browser open at https://www.saucedemo.com/
- **Test data:** Username: `foo`, Password: `randompass`
- **Steps:**
  1. Enter the test data above
  2. Click "Login"
- **Expected result:** Error message displayed: "Epic sadface: Username and password do not match any user in this service"
- **Actual result:** As expected
- **Status:** Pass

### TC-LOGIN-03 — Login fails with a valid username and incorrect password
- **Preconditions:** Browser open at https://www.saucedemo.com/
- **Test data:** Username: `standard_user`, Password: `wrongpass123`
- **Steps:**
  1. Enter the test data above
  2. Click "Login"
- **Expected result:** Error message displayed: "Epic sadface: Username and password do not match any user in this service" (identical message to TC-LOGIN-02, confirming the system does not reveal whether a username exists)
- **Actual result:** As expected
- **Status:** Pass

### TC-LOGIN-04 — Login fails for a valid but locked-out user
- **Preconditions:** Browser open at https://www.saucedemo.com/
- **Test data:** Username: `locked_out_user`, Password: `secret_sauce`
- **Steps:**
  1. Enter the test data above
  2. Click "Login"
- **Expected result:** Error message displayed: "Epic sadface: Sorry, this user has been locked out."
- **Actual result:** As expected
- **Status:** Pass

### TC-LOGIN-05 — Login succeeds with a valid, active user
- **Preconditions:** Browser open at https://www.saucedemo.com/
- **Test data:** Username: `standard_user`, Password: `secret_sauce`
- **Steps:**
  1. Enter the test data above
  2. Click "Login"
- **Expected result:** User is redirected to the Products page
- **Actual result:** As expected
- **Status:** Pass

### TC-LOGIN-06 — Login attempt for a locked-out user with an incorrect password *(not yet executed)*
- **Test data:** Username: `locked_out_user`, Password: `wrongpass123`
- **Expected result:** Unconfirmed — open question is whether the "locked out" message or the generic "do not match" message takes priority
- **Status:** Not run

### TC-LOGIN-07 — Login attempt for a valid user with an empty password *(not yet executed)*
- **Test data:** Username: `standard_user`, Password: *(blank)*
- **Expected result:** Unconfirmed — likely a "Password is required" message, by analogy with TC-LOGIN-01, but not yet verified
- **Status:** Not run
