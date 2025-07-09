# Create table token with sqlite3
import sqlite3

def create_table():
    with sqlite3.connect('token.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS token
                     (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      token TEXT NOT NULL)''')

        # Create index for token for faster lookups
        c.execute('CREATE INDEX IF NOT EXISTS idx_token ON token (token)')
        conn.commit()

def insert_token(user_id, token):
    with sqlite3.connect('token.db') as conn:
        c = conn.cursor()
        c.execute('INSERT INTO token (user_id, token) VALUES (?, ?)', (user_id, token))
        conn.commit()

def check_token_exists(token):
    with sqlite3.connect('token.db') as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM token WHERE token = ?', (token,))
        exists = c.fetchone() is not None
    return exists

if __name__ == "__main__":
    create_table()
    print("Table 'token' created successfully.")
    for i in range(1, 100_000):
        insert_token(i, f'example_token_{i}')
        if i % 100 == 0:
            print(f"Inserted {i} tokens.")
    print("Token inserted successfully.")
    # Check a specific token
    import time
    start_time = time.time()
    print(check_token_exists('example_token_99999'))  # Should return 'token_99999'
    end_time = time.time()
    print(f"Time taken to check token: {end_time - start_time} seconds")