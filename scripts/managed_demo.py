import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MAN_DB_HOST = os.getenv("MAN_DB_HOST")
MAN_DB_PORT = os.getenv("MAN_DB_PORT", "3306")
MAN_DB_USER = os.getenv("MAN_DB_USER")
MAN_DB_PASS = os.getenv("MAN_DB_PASS")
MAN_DB_NAME = os.getenv("MAN_DB_NAME")

print("[ENV] MAN_DB_HOST:", MAN_DB_HOST)
print("[ENV] MAN_DB_PORT:", MAN_DB_PORT)
print("[ENV] MAN_DB_USER:", MAN_DB_USER)
print("[ENV] MAN_DB_NAME:", MAN_DB_NAME)

# Build connection URL
db_url = (
    f"mysql+pymysql://{MAN_DB_USER}:{MAN_DB_PASS}"
    f"@{MAN_DB_HOST}:{MAN_DB_PORT}/{MAN_DB_NAME}"
)

engine = create_engine(db_url, pool_pre_ping=True)

# Create sample data
df = pd.DataFrame(
    [
        {"patient_id": 1, "visit_reason": "checkup"},
        {"patient_id": 2, "visit_reason": "followup"},
        {"patient_id": 3, "visit_reason": "lab"},
        {"patient_id": 4, "visit_reason": "consult"},
        {"patient_id": 5, "visit_reason": "discharge"},
    ]
)

# Write table
df.to_sql("visits", con=engine, if_exists="replace", index=False)

# Read back row count
with engine.connect() as conn:
    result = pd.read_sql(
        text("SELECT COUNT(*) AS n_rows FROM visits"),
        conn
    )

print(result)