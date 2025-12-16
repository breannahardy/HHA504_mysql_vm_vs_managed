# MySQL on VM vs Managed Service

## Overview
On Google Cloud Platform (GCP), I created and interacted with two MySQL databases. The first database was a self-managed MySQL instance running on a virtual machine, and the second was a managed MySQL instance using Cloud SQL. I connected to both databases using Python with SQLAlchemy, created a table, inserted sample data, and queried the results. The region used for this assignment was `us-east4`.

## Loom Link

<https://www.loom.com/share/d75b6d71fd4c4e7ebfedb03142fab44b>
---

## MySQL on a VM – Steps
1. Created a Compute Engine VM instance in GCP.
2. Configured firewall rules to allow inbound traffic on ports **22 (SSH)** and **3306 (MySQL)**.
3. Installed and configured MySQL server packages via the VM’s SSH terminal.
4. Created a database and user and granted appropriate privileges.
5. Verified the MySQL service was running.
6. Created a local `.env` file to store database credentials.
7. Ran a Python script using pandas and SQLAlchemy to create a table and read data.

---

## MySQL on a Managed Service – Steps
1. Created a Cloud SQL MySQL instance with a small tier.
2. Enabled public IP access and configured authorized networks.
3. Created a database and user in Cloud SQL.
4. Enabled automated backups and point-in-time recovery.
5. Connected to the instance using the MySQL client and tested access.
6. Stored credentials locally in a `.env` file.
7. Ran a Python script to insert and query data from the managed database.

---

## Connection URL Pattern
The following connection pattern was used consistently for both environments:

```text
mysql+pymysql://USER:PASS@HOST:PORT/DBNAME
```
---

## Example of Database Credentials

Database credentials were stored locally in a .env file and were not uploaded to GitHub.

### VM
```
VM_DB_HOST=....      
VM_DB_PORT=3306
VM_DB_USER=class_user
VM_DB_PASS=change_me
VM_DB_NAME=class_db
```
### Managed
```
MAN_DB_HOST=...
MAN_DB_PORT=3306
MAN_DB_USER=class_user
MAN_DB_PASS=change_me
MAN_DB_NAME=class_db
```
---

## Screenshots

### VM
- `vmcreation.png` – VM instance creation page
- `firewallrules.png` – Firewall rules allowing ports 22 and 3306
- `packages.png `– MySQL server and client installation
- `servicestatus.png` – MySQL service running (systemctl status mysql)
- `db_table.png` – MySQL CLI showing database and table
- `local_test.png` – Python script successfully connecting and querying

### Managed MySQL Screenshots

- `creation_summary.png` – Cloud SQL instance creation summary
- `connection info.png `– Public IP and instance connection details
- `VPC.png `– Authorized networks configuration
- `test.png` – Python script successfully inserting and reading data
