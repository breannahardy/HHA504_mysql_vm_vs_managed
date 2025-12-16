import os
import time
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# --- 0) Load environment ---
load_dotenv()

VM_DB_HOST = os.getenv("VM_DB_HOST")
VM_DB_PORT = os.getenv("VM_DB_PORT", "3306")
VM_DB_USER = os.getenv("VM_DB_USER")
VM_DB_PASS = os.getenv("VM_DB_PASS")
VM_DB_NAME = os.getenv("VM_DB_NAME")

print("[ENV] VM_DB_HOST:", VM_DB_HOST)
print("[ENV] VM_DB_PORT:", VM_DB_PORT)
print("[ENV] VM_DB_USER:", VM_DB_USER)
print("[ENV] VM_DB_NAME:", VM_DB_NAME)

# --- 1) Ensure database exists ---
t0 = time.time()

server_url = (
    f"mysql+pymysql://{VM_DB_USER}:{VM_DB_PASS}"
    f"@{VM_DB_HOST}:{VM_DB_PORT}/{VM_DB_NAME}"
)

engine_server = create_engine(server_url, pool_pre_ping=True)

with engine_server.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{VM_DB_NAME}`"))
    conn.commit()

print(f"[OK] Database `{VM_DB_NAME}` exists.")

# --- 2) Connect to target database ---
engine = create_engine(server_url)

# --- 3) Create DataFrame and write table ---
table_name = "visits"

df = pd.DataFrame(
    [
        {"patient_id": 1, "visit_date": "2025-09-01", "bp_sys": 118, "bp_dia": 76},
        {"patient_id": 2, "visit_date": "2025-09-02", "bp_sys": 130, "bp_dia": 85},
        {"patient_id": 3, "visit_date": "2025-09-03", "bp_sys": 121, "bp_dia": 79},
        {"patient_id": 4, "visit_date": "2025-09-04", "bp_sys": 110, "bp_dia": 70},
        {"patient_id": 5, "visit_date": "2025-09-05", "bp_sys": 125, "bp_dia": 82},
    ]
)

df.to_sql(table_name, con=engine, if_exists="replace", index=False)

print(f"[OK] Wrote {len(df)} rows to `{table_name}`.")

# --- 4) Read back row count ---
with engine.connect() as conn:
    count_df = pd.read_sql(
        f"SELECT COUNT(*) AS n_rows FROM `{table_name}`", con=conn
    )

print(count_df)

elapsed = time.time() - t0
print(f"[DONE] VM demo completed in {elapsed:.1f}s at {datetime.utcnow().isoformat()}Z")