import secrets
import os
from pathlib import Path

def generate_vault_token():
    """Generate a secure random token for Vault"""
    # Generate a secure random token
    token = secrets.token_hex(32)
    
    # Create secrets directory if it doesn't exist
    secrets_dir = Path("vault/secrets")
    secrets_dir.mkdir(parents=True, exist_ok=True)
    
    # Write token to file
    token_file = secrets_dir / "vault_token.txt"
    with open(token_file, "w") as f:
        f.write(token)
    
    # Set appropriate permissions
    token_file.chmod(0o600)
    
    print(f"Generated Vault token and saved to {token_file}")
    print("Please make sure to backup this token securely!")

if __name__ == "__main__":
    generate_vault_token() 