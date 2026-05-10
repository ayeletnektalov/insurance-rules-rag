import pg from "pg";
import dotenv from "dotenv";
import OpenAI from "openai";

dotenv.config();

const { Client } = pg;

const db = new Client({
  host: process.env.PGHOST,
  port: process.env.PGPORT,
  user: process.env.PGUSER,
  password: process.env.PGPASSWORD,
  database: process.env.PGDATABASE
});

const openai = new OpenAI({
  baseURL: "https://openrouter.ai/api/v1",
  apiKey: process.env.OPENROUTER_API_KEY
});

async function searchRules() {

  try {

    await db.connect();

    console.log("Connected!");

    const newRule =
      "if driver_country is israel then increase_premium";

    console.log("\nSearching for:");
    console.log(newRule);

    const embeddingResponse =
      await openai.embeddings.create({

        model: "text-embedding-3-small",

        input: newRule
      });

    const embedding =
      embeddingResponse.data[0].embedding;

    const result = await db.query(
      `
      SELECT
        id,
        rule_text,
        embedding <=> $1 AS distance
      FROM rules
      ORDER BY distance
      LIMIT 5
      `,
      [JSON.stringify(embedding)]
    );

    console.log("\nMOST SIMILAR RULES:\n");

    console.table(result.rows);

    await db.end();

  } catch (error) {

    console.error(error);
  }
}

searchRules();