#!/usr/bin/env node

/*
 * Markdown-aware DeepL translation adapter.
 *
 * This intentionally fails closed until the Markdown parser and glossary
 * protection rules are implemented. A future implementation must preserve:
 *
 * - YAML frontmatter keys and machine-readable values;
 * - code fences and inline code;
 * - URLs, reference IDs, and explicit heading IDs;
 * - canonical terms from _meta/glossary.yaml;
 * - the exact relative path under website/i18n/<locale>/...
 */

console.error(
  'Translation is disabled. Implement scripts/translate.mjs before setting ENABLE_TRANSLATION=true.',
);
process.exit(1);
