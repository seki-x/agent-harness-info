# Cloudflare Pages Setup

This file is an operator checklist. The website is a presentation layer over
the canonical Markdown in ../knowledge.

## Git integration

1. Create a Cloudflare Pages project.
2. Connect the GitHub repository seki-x/agent-harness-info.
3. Set the production branch to main.
4. Keep the repository root available to the build because Docusaurus is under
   website/ but consumes sibling knowledge/.
5. Use this build command:

       npm --prefix website ci && npm --prefix website run build

   Before website/package-lock.json exists, temporarily use:

       npm --prefix website install && npm --prefix website run build

6. Set the build output directory to:

       website/build

7. Configure SITE_URL to the final Pages URL or custom domain.

## Preview deployments

Keep preview deployments enabled for pull-request branches:

    Codex branch
        ↓
    GitHub pull request
        ↓
    GitHub build status + Cloudflare preview
        ↓
    Human review
        ↓
    Merge to main
        ↓
    Production deployment

Only main is production. Do not make Codex branches production branches.

## Security

If repository or preview knowledge should not be public, configure Cloudflare
Access for preview deployments.

## Custom domain

Add the final domain, update SITE_URL, and update repository metadata if needed.

## Do not

Do not copy Markdown into a Cloudflare-specific content directory. Cloudflare
deploys the Docusaurus projection; knowledge/ remains canonical.
