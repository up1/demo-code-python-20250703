# Create table token by user with sqlite3
import sqlite3

def create_table():
    """Create a SQLite database and a table for storing tokens."""
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    
    # Create table if it does not exist
    c.execute('''CREATE TABLE IF NOT EXISTS token
                 (id INTEGER PRIMARY KEY,
                  user TEXT,
                  token TEXT)''')
    
    # create index for faster lookup
    c.execute('CREATE INDEX IF NOT EXISTS idx_user ON token (user)')
    
    conn.commit()
    conn.close()

# Insert a sample token
def insert_token(user, token):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("INSERT INTO token (user, token) VALUES (?, ?)", (user, token))
    conn.commit()
    conn.close()

# Check token for a user
def check_token(user):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT token FROM token WHERE user=?", (user,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None


# Example usage
# create_table()
# insert_token('somkiat', 'sample_token_123')
# print(check_token('somkiat'))  # Should return 'sample_token_123'

# Add 100,000 tokens
# for i in range(100000):
#     insert_token(f'user_{i}', f'token_{i}')

# Check a specific token with a large number of entries
# Performance test
if __name__ == "__main__":
    create_table()
    # Insert 100,000 tokens for performance testing
    for i in range(100000):
        insert_token(f'user_{i}', f'token_{i}')
    print("Inserted 100,000 tokens.")
    # Check a specific token
    import time
    start_time = time.time()
    print(check_token('user_99999'))  # Should return 'token_99999'
    end_time = time.time()
    print(f"Time taken to check token: {end_time - start_time} seconds")

