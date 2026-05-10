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

async function testConnection() {

  try {

    await client.connect();

    console.log("Connected to PostgreSQL!");

    const result = await client.query(
      "SELECT NOW()"
    );

    console.log(result.rows);

    await client.end();

  } catch (error) {

    console.error(error);
  }
}

testConnection();