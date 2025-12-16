## Setup Notes
This document outlines the steps taken to install, configure, and validate a self-managed MySQL database on a Google Cloud virtual machine.

---
### 1. Create and Access VM
- Provider: Google Cloud Platform
- Service: Compute Engine
- OS: Ubuntu 22.04 LTS
- Region/Zone: us-east4-b

SSH into the VM:
```bash
gcloud compute ssh assignment4 --zone us-east4-b

### 2. Install MySQL Server
- Update packages and install MySQL
```sudo apt update
sudo apt install mysql-server mysql_client -y
```
- Verify MYSQL is running
```sudo systemctl status mysql
```
## 3. Create Database and User

Log into MySQL as root:

```bash
sudo mysql

CREATE DATABASE class_db;
CREATE USER 'class_user'@'%' IDENTIFIED BY 'password_here';
GRANT ALL PRIVILEGES ON class_db.* TO 'class_user'@'%';
FLUSH PRIVILEGES;
EXIT;

## 4. Review MySQL Configuration

Edit the MySQL configuration file:

```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf

The MySQL configuration file was reviewed but not modified.
## 5. Python Validation

Install required Python dependencies:

``pip install sqlalchemy pymysql pandas python-dotenv
``
Run the demo script from the project root:
python3 scripts/vm_demo.py
The output confirmed successful table creation and row count retrieval.

## Troubleshooting

- Access denied errors: Resolved by recreating the MySQL user and reapplying database privileges
- Connection issues: Verified MySQL service status and confirmed local bind address configuration.
- Environment variables not loading: Fixed by ensuring the .env file existed and scripts were run from the project root.

## Elapsed Time

VM creation and SSH access: ~10 minutes

MySQL installation and configuration: ~20 minutes

Python validation and troubleshooting: ~30 minutes

Total elapsed time: ~1 hour