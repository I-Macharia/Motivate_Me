import { User, CreateUserRequest, UpdateUserRequest } from '@/types/user';
import sqlite3 from 'sqlite3';
import { open, Database } from 'sqlite';

let db: Database | null = null;

async function getDatabase(): Promise<Database> {
  if (db === null) {
    db = await open({
      filename: 'src/data/motivate_me.db',
      driver: sqlite3.Database
    });
  }
  return db;
}

export async function createUser(userData: CreateUserRequest): Promise<User> {
  const db = await getDatabase();
  const { username, email, civicPassId } = userData;
  const now = new Date().toISOString();

  const result = await db.run(
    `INSERT INTO users (username, email, civic_pass_id, created_at, updated_at)
     VALUES (?, ?, ?, ?, ?)`,
    [username, email, civicPassId, now, now]
  );

  return {
    id: result.lastID?.toString() || '',
    username,
    email,
    civicPassId,
    createdAt: new Date(now),
    updatedAt: new Date(now)
  };
}

export async function getUser(username: string): Promise<User | null> {
  const db = await getDatabase();
  const user = await db.get(
    `SELECT * FROM users WHERE username = ?`,
    [username]
  );

  if (!user) return null;

  return {
    id: user.id.toString(),
    username: user.username,
    email: user.email,
    civicPassId: user.civic_pass_id,
    createdAt: new Date(user.created_at),
    updatedAt: new Date(user.updated_at)
  };
}

export async function updateUser(username: string, updates: UpdateUserRequest): Promise<User | null> {
  const db = await getDatabase();
  const now = new Date().toISOString();
  
  const setClause = Object.entries(updates)
    .map(([key, _]) => `${key === 'civicPassId' ? 'civic_pass_id' : key} = ?`)
    .concat(['updated_at = ?'])
    .join(', ');
  
  const values = Object.values(updates).concat([now, username]);

  const result = await db.run(
    `UPDATE users SET ${setClause} WHERE username = ?`,
    values
  );

  if (result.changes === 0) return null;
  
  return getUser(username);
}

export async function deleteUser(username: string): Promise<boolean> {
  const db = await getDatabase();
  const result = await db.run(
    'DELETE FROM users WHERE username = ?',
    [username]
  );
  
  return (result.changes ?? 0) > 0;
}

// Initialize database with required tables
export async function initializeDatabase(): Promise<void> {
  const db = await getDatabase();
  await db.exec(`
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT UNIQUE NOT NULL,
      email TEXT,
      civic_pass_id TEXT,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL
    )
  `);
}
