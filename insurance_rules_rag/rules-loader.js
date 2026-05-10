import fs from "fs";

const rulesText = fs.readFileSync(
  "../_Task_/rules.txt",
  "utf-8"
);

const rules = rulesText
  .split("\n")
  .map(line => line.trim())
  .filter(line => line.includes("if"))
  .map((rule, index) => ({
    id: index + 1,
    text: rule.replace("- ", "")
  }));

const newRule =
  "if driver_country is israel then increase_premium";

console.log("\nNEW RULE:");
console.log(newRule);

const similarRules = rules.filter(rule =>
  rule.text.includes("driver_country")
);

let recommendation = "Low_Severity_Match";
let matchedRule = null;
let reason = "";

const exactMatch = similarRules.find(
  rule => rule.text === newRule
);

if (exactMatch) {
  recommendation = "Exact_Match";
  matchedRule = exactMatch;

  reason = "The exact same rule already exists.";
}

const includedMatch = similarRules.find(rule =>
  rule.text.includes("[israel, spain]") &&
  rule.text.includes("increase_premium")
);

if (includedMatch) {
  recommendation = "Duplicated_Add_to_list";
  matchedRule = includedMatch;

  reason =
    "The new rule is already semantically included inside an existing list rule.";
}

const contradiction = similarRules.find(rule =>
  rule.text.includes("is israel") &&
  rule.text.includes("approve_standard")
);

if (contradiction) {
  recommendation = "High_Severity_Match";
  matchedRule = contradiction;

  reason =
    "A rule with the same condition but different action already exists.";
}

console.log("\nRESULT:");

console.log({
  recommendation,
  matchedRule,
  reason
});