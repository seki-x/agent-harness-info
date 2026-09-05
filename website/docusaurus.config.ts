import type {Config} from '@docusaurus/types';
import type {Options, ThemeConfig} from '@docusaurus/preset-classic';

const siteUrl = process.env.SITE_URL ?? 'https://agent-harness-info.pages.dev';

const config: Config = {
  title: 'AI Agent Knowledge',
  tagline: 'A living knowledge base for AI Agent and Agent Harness engineering',
  favicon: 'img/favicon.svg',

  url: siteUrl,
  baseUrl: '/',
  organizationName: 'seki-x',
  projectName: 'agent-harness-info',

  onBrokenLinks: 'throw',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
    localeConfigs: {
      en: {
        label: 'English',
        htmlLang: 'en',
      },
    },
  },

  presets: [
    [
      'classic',
      {
        docs: {
          path: '../knowledge',
          routeBasePath: '/',
          sidebarPath: './sidebars.js',
          includeCurrentVersion: true,
          lastVersion: 'current',
          editUrl:
            'https://github.com/seki-x/agent-harness-info/edit/main/knowledge/',
          showLastUpdateAuthor: false,
          showLastUpdateTime: true,
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Options,
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'AI Agent Knowledge',
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'knowledgeSidebar',
          position: 'left',
          label: 'Knowledge',
        },
        {
          type: 'docsVersionDropdown',
          position: 'right',
        },
        {
          href: 'https://github.com/seki-x/agent-harness-info',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'light',
      copyright:
        'Living Knowledge Base · Built ' + new Date().getFullYear(),
    },
  } satisfies ThemeConfig,
};

export default config;
