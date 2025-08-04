"""
Setup script for video asset app.
"""
from setuptools import setup, find_packages

setup(
    name="video_asset_app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pgvector",
        "psycopg2-binary",
        "sqlalchemy",
        "fastapi",
        "numpy",
        "python-dotenv",
    ],
)
