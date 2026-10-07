import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INSTANCE_PATH = PROJECT_ROOT / 'instance'
INSTANCE_PATH.mkdir(exist_ok=True)

load_dotenv(PROJECT_ROOT / '.env')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123-change-in-production'
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY') or ""
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID') or ""
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET') or ""
    GITHUB_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID') or ""
    GITHUB_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET') or ""
    ADMIN_EMAILS = {email.strip().lower() for email in os.environ.get('ADMIN_EMAILS', '').split(',') if email.strip()}
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', '').lower() == 'true'
    UPLOAD_FOLDER = str(INSTANCE_PATH / 'uploads')
    RESUME_UPLOAD_FOLDER = str(INSTANCE_PATH / 'uploads' / 'resumes')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = str(INSTANCE_PATH / 'flask_session')
    
    # Allowed file extensions
    ALLOWED_EXTENSIONS = {'pdf', 'txt', 'docx'}
    
    # Interview settings
    QUESTION_TIME_LIMIT = 120  # seconds
    CODING_TIME_LIMIT = 600  # seconds
    
    # Database
    DATABASE = str(INSTANCE_PATH / 'database.sqlite')
    
    # Gemini model
    GEMINI_MODEL = 'gemini-2.5-flash'  # Using the latest flash model
