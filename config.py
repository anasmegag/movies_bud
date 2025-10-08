import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:ofKbORlNNUNiKNhdCUotWXFsfXSzrgMF@interchange.proxy.rlwy.net:44424/railway"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False