# Storefront deployment — handoff to Cougar Curds

From: the storefront vendor
To: Cougar Curds IT

This repository is how we deploy the storefront app for every client we support. It is yours now. Copy it into
your own **private** repository and keep your copy as the one true version of how your store gets deployed.

## What is in here

| File | What it is |
|---|---|
| `deploy_storefront.yml` | The playbook. Installs the container engine, copies the app, builds the image, runs the container, checks the page. |
| `inventory.example` | A sample inventory. Copy it to `inventory.ini` and fill in your own servers. |
| `group_vars/appservers.yml` | Settings for your app servers: where your database is and which login the app uses. |
| `files/store.py` | The app, version 2.0. New in this version: a footer showing the version and which server served the page. |
| `files/Dockerfile` | The image recipe. |
| `.gitignore` | Files that must never be committed. |

## Before you run it

1. Copy `inventory.example` to `inventory.ini` and fill in your servers and login name.
2. Edit `group_vars/appservers.yml` with your database endpoint and login.
3. Make sure your database is running.

## Run it

    ansible-playbook -i inventory.ini deploy_storefront.yml

You will be asked for the database password. We never store it, and you should not either. It does not belong
in this repository, in any file you commit, or in an email to us.

## Notes

- Tested on our Ubuntu 22.04 and 24.04 hosts.
- Safe to run again. A second run with nothing changed reports no changes.
