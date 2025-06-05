import sqlite3 from "sqlite3";
import { open } from "sqlite";

export async function getDatabaseConnection() {
  return open({
    filename: "./src/data/motivate_me.db",
    driver: sqlite3.Database,
  });
}
