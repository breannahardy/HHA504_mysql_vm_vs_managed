# Setup Notes — Managed MySQL (Cloud SQL)

## Environment
- Cloud provider: Google Cloud Platform (GCP)
- Service: Cloud SQL
- Engine: MySQL 8.0
- Region: us-east4

## Instance Configuration
- Tier: Small (Sandbox / minimal development tier)
  - ~2 vCPUs
  - ~8 GB RAM
- High Availability: Single-zone (default)
- Automatic backups: Enabled

## Networking
- Public IP enabled
- Authorized networks configured to allow external access
  - For demonstration purposes, `0.0.0.0/0` was used
- SSL enforcement disabled to simplify connectivity for coursework

## Users and Database
- Default admin user: `root`
- Application user created: `class_user`
- Database created: `class_db`
- User granted full access to application database

## Application Connectivity
- Connected via public IP over TCP port 3306
- Python connected using SQLAlchemy with PyMySQL driver
- Credentials stored in `.env` (not committed)

## Validation
- Python script (`managed_demo.py`) successfully:
  - Connected to Cloud SQL instance
  - Created a table using pandas `to_sql`
  - Inserted 5 rows
  - Queried row count using `read_sql`