# Setup Notes — Managed MySQL (Cloud SQL)

## 1. Create Cloud SQL Instance
- Provider: Google Cloud Platform
- Service: Cloud SQL
- Engine: MySQL 8.0
- Tier: Small (development tier)
- Region: us-east4
- High availability: Single-zone
- Automatic backups: Enabled by default


## 2. Networking
- Public IP enabled
- Authorized networks configured to allow external access
  - For demonstration purposes, `0.0.0.0/0` was used
- SSL enforcement disabled to simplify connectivity for coursework

## 3. Users and Database
- Default admin user: `root`
- Application user created: `class_user`
- Database created: `class_db`
- User granted full access to application database
- Created password manually

## 4. Application Connectivity
- Connected via public IP over TCP port 3306
- Python connected using SQLAlchemy with PyMySQL driver
- Credentials stored in `.env` (not committed)
```
MAN_DB_HOST=<cloud_sql_public_ip>
MAN_DB_PORT=3306
MAN_DB_USER=class_user
MAN_DB_PASS=password_here
MAN_DB_NAME=class_db
```

## 5. Validation
- Installed required Python packages:
```
pip install sqlalchemy pymysql pandas python-dotenv
```
- Run Python script (`managed_demo.py`):
  - Connected to Cloud SQL instance
  - Created a table using pandas `to_sql`
  - Inserted 5 rows
  - Queried row count using `read_sql`

 ## 6. Troubleshooting
 - Error 1045 (Access denied): Resolved by recreating the database user with host % and resetting the password.
 - Repeated authentication failures: Traced to Cloud SQL SSL enforcement; resolved by disabling required SSL.
 - Connection issues during local execution: Ensured the .env file was present and environment variables were loaded correctly.

## Elapsed Time
- Cloud SQL instance provisioning: ~10 minutes
- Networking and security configuration: ~10 minutes
- Troubleshooting and Python validation: ~20 minutes
Total elapsed time: ~40 minutes
