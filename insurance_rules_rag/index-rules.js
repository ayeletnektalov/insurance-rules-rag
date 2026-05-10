import fs from "fs";
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

async function indexRules() {

  try {

    await db.connect();

    console.log("Connected to DB");

    const rulesText = fs.readFileSync(
      "../_Task_/rules.txt",
      "utf-8"
    );

    const rules = rulesText
      .split("\n")
      .map(line => line.trim())
      .filter(line => line.includes("if"));

    for (const rule of rules) {

      console.log(`Embedding: ${rule}`);

      const embeddingResponse =
        await openai.embeddings.create({

          model: "text-embedding-3-small",

          input: rule
        });

      const embedding =
        embeddingResponse.data[0].embedding;

      await db.query(
        `
        INSERT INTO rules
        (rule_text, embedding)
        VALUES ($1, $2)
        `,
        [rule, JSON.stringify(embedding)]
      );

      console.log("Inserted!");
    }

    console.log("All rules indexed!");

    await db.end();

  } catch (error) {

    console.error(error);
  }
}

indexRules();