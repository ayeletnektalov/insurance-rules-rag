import pg from "pg";
import dotenv from "dotenv";

dotenv.config();

const { Client } = pg;

const client = new Client({
  host: process.env.PGHOST,
  port: process.env.PGPORT,
  user: process.env.PGUSER,
  password: process.env.PGPASSWORD,
  database: process.env.PGDATABASE
});

async function setupDatabase() {

  try {

    await client.connect();

    console.log("Connected!");

    await client.query(`
      CREATE EXTENSION IF NOT EXISTS vector;
    `);

    await client.query(`
      CREATE TABLE IF NOT EXISTS rules (
        id SERIAL PRIMARY KEY,
        rule_text TEXT,
        embedding vector(1536)
      );
    `);

    console.log("Rules table created!");

    await client.end();

  } catch (error) {

    console.error(error);
  }
}

setupDatabase();