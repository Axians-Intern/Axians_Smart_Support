class Config:
    DEBUG = True  # Enable debug mode
    TESTING = False  # Disable testing mode
    CSRF_ENABLED = True  # Enable CSRF protection
    CSRF_SESSION_KEY = 'your-csrf-session-key'  # Used for CSRF protection
    SESSION_COOKIE_NAME = 'your-session-cookie-name'  # Name of the session cookie
    SESSION_COOKIE_SECURE = False  # Set to True if using HTTPS
    SECRET_KEY = 'your-secret-key'  # Used for sessions and security
    SESSION_TYPE = 'filesystem'  # Use filesystem for session storage
    SESSION_PERMANENT = True  # Make sessions permanent
    SESSION_USE_SIGNER = True  # Sign session cookies
    SESSION_KEY_PREFIX = 'your-session-key-prefix'  # Prefix for session keys
    SESSION_FILE_DIR = '/tmp/flask_session'  # Directory for session files
    SQLALCHEMY_DATABASE_URI = 'sqlite:////app.db'  # SQLite database file
    SQLALCHEMY_BINDS = {
        'default': 'sqlite:////app.db',  # Default database
        'other': 'sqlite:////other.db'  # Example of another database bind
    }
    SQLALCHEMY_ECHO = False  # Log SQL queries to console
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 10,  # Size of the connection pool
        'max_overflow': 5,  # Maximum overflow connections
        'pool_timeout': 30,  # Timeout for getting a connection from the pool
        'pool_recycle': 1800,  # Recycle connections after this many seconds
        'connect_args': {'check_same_thread': False}  # SQLite specific option
    }
    SQLALCHEMY_NATIVE_UNICODE = True  # Use native Unicode support
    SQLALCHEMY_RECORD_QUERIES = True  # Record queries for debugging
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # Commit changes at the end of each request
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking
    UPLOAD_FOLDER = 'static/uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}  # Allowed file extensions for uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Maximum upload size (16 MB)    
    LANGCHAIN_TRACING_V2 = True  # Enable LangChain tracing
    LANGCHAIN_TRACING_INTEGRATION = True  # Enable tracing integration
    LANGCHAIN_TRACING_DIR = "langchain_traces"  # Directory for storing LangChain traces
    LANGCHAIN_TRACING_CONFIG = {
        "enabled": True,  # Enable tracing
        "tracing_integration": True,  # Enable tracing integration
        "tracing_dir": "langchain_traces",  # Directory for storing traces
        "tracing_endpoint": "http://localhost:8000",  # Endpoint for LangChain tracing
        "tracing_api_key": "your-langchain-api-key",  # API
        "tracing_project": "your-langchain-project",  # Project name for LangChain tracing
        "tracing_run_name": "your-langchain-run-name"  # Run name for
    }
    LANGCHAIN_TRACING_V2 = True  # Enable LangChain tracing v2
    LANGCHAIN_ENDPOINT = "http://localhost:8000"  # LangChain server endpoint
    LANGCHAIN_API_KEY = "your-langchain-api-key"  # API key for LangChain
    LANGCHAIN_PROJECT = "your-langchain-project"  # Project name for LangChain
    LANGCHAIN_RUN_NAME = "your-langchain-run-name"  # Run name for LangChain
    LANGCHAIN_TRACING_INTEGRATION = True  # Enable tracing integration
    LANGCHAIN_TRACING_DIR = "langchain_traces"  # Directory for storing LangChain traces
    LANGCHAIN_TRACING_CONFIG = {
        "enabled": True,  # Enable tracing
        "tracing_integration": True,  # Enable tracing integration
        "tracing_dir": "langchain_traces",  # Directory for storing traces
        "tracing_endpoint": "http://localhost:8000",  # Endpoint for LangChain tracing
        "tracing_api_key": "your-langchain-api-key",  # API
        "tracing_project": "your-langchain-project",  # Project name for LangChain tracing
        "tracing_run_name": "your-langchain-run-name"  # Run name for LangChain tracing
    }
    LANGCHAIN_TRACING_V2 = True  # Enable LangChain tracing v2
   