from src.vault_client import VaultClient
from src.logger import Logger

def init_vault():
    """Initialize Vault with MongoDB secrets"""
    logger = Logger(name="init_vault")
    
    try:
        # Initialize Vault client
        vault_client = VaultClient()
        
        # Enable KV secrets engine if not already enabled
        if 'secret/' not in vault_client.client.sys.list_mounted_secrets_engines():
            vault_client.client.sys.enable_secrets_engine(
                backend_type='kv',
                path='secret',
                options={'version': '2'}
            )
            logger.info("Enabled KV secrets engine")
            
        # Setup MongoDB secrets
        vault_client.setup_mongodb_secrets(
            username="admin",
            password="admin123",
            db_name="banknote_db"
        )
        
        logger.info("Successfully initialized Vault")
        
    except Exception as e:
        logger.error(f"Failed to initialize Vault: {str(e)}")
        raise

if __name__ == "__main__":
    init_vault() 