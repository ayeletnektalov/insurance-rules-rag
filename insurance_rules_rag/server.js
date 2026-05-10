import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import pg from "pg";
import OpenAI from "openai";

dotenv.config();

const app = express();

app.use(cors());
app.use(express.json());

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

await db.connect();

console.log("Connected to PostgreSQL!");

function parseRule(ruleText) {

  const clean = ruleText.replace("- ", "").trim();

  const parts = clean.split(" then ");

  if (parts.length < 2) {
    return null;
  }

  return {
    condition: parts[0].trim(),
    action: parts[1].trim(),
    fullText: clean
  };
}

app.post("/check-rule", async (req, res) => {

  try {

    const newRuleText = req.body.rule;

    const parsedNewRule =
      parseRule(newRuleText);

    const embeddingResponse =
      await openai.embeddings.create({

        model: "text-embedding-3-small",

        input: newRuleText
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

    const similarRules = result.rows;

    let recommendation =
      "Low_Severity_Match";

    let matchedRule = null;

    let reason =
      "No strong conflicts found.";

    for (const row of similarRules) {

      const parsedExistingRule =
        parseRule(row.rule_text);

      if (!parsedExistingRule) {
        continue;
      }

      if (
        parsedExistingRule.condition ===
          parsedNewRule.condition &&

        parsedExistingRule.action ===
          parsedNewRule.action
      ) {

        recommendation = "Exact_Match";

        matchedRule = parsedExistingRule;

        reason =
          "The exact same rule already exists.";

        break;
      }

      if (
        parsedExistingRule.condition ===
          parsedNewRule.condition &&

        parsedExistingRule.action !==
          parsedNewRule.action
      ) {

        recommendation =
          "High_Severity_Match";

        matchedRule =
          parsedExistingRule;

        reason =
          "A rule with the same condition but different action already exists.";

        break;
      }

      if (
        row.distance < 0.15
      ) {

        recommendation =
          "Duplicated_Add_to_list";

        matchedRule =
          parsedExistingRule;

        reason =
          "A semantically similar rule already exists.";

        break;
      }
    }

    res.json({
      recommendation,
      matchedRule,
      reason,
      similarRules
    });

  } catch (error) {

    console.error(error);

    res.status(500).json({
      error: error.message
    });
  }
});

app.listen(3000, () => {

  console.log(
    "Server running on port 3000"
  );
});