import os

CREDS_ENV_KEY = "SCOOPBOT_CREDS"

def load_creds() -> str:
    env_creds = os.getenv(CREDS_ENV_KEY)
    if not env_creds:
        raise EnvironmentError(f"Env key {CREDS_ENV_KEY} not found")
    return env_creds
