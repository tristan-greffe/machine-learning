import { withMermaid } from 'vitepress-plugin-mermaid'

export default withMermaid({
  base: '/machine-learning',
  title: 'Machine Learning',
  ignoreDeadLinks: true,
  appearance: false,
  head: [
    ['link', { href: 'https://cdnjs.cloudflare.com/ajax/libs/line-awesome/1.3.0/line-awesome/css/line-awesome.min.css', rel: 'stylesheet' }],
    ['link', { rel: 'icon', href: '/machine-learning/favicon.ico' }]
  ],
  markdown: {
    math: true
  },
  locales: {
    root: {
      label: 'English',
      lang: 'en'
    },
    fr: {
      label: 'French',
      lang: 'fr',
      themeConfig: {
        outline: { label: 'Sur cette page' },
        nav: [
          { text: 'A propos', link: '/fr/about/introduction' },
          { text: 'Apprentissage', link: '/fr/learning/introduction' },
          { text: 'Ateliers', link: '/fr/labs/introduction' },
          { text: 'Ressources', link: '/fr/resources/introduction' }
        ],
        sidebar: {
          '/fr/about/': getAboutSidebar('fr'),
          '/fr/learning/': getLearningSidebar(),
          '/fr/labs/': getLabsSidebar()
        },
        docFooter: {
          prev: 'Page précédente',
          next: 'Page suivante'
        }
      }
    }
  },
  themeConfig: {
    logo: '/machine-learning.png',
    socialLinks: [
      { icon: 'github', link: 'https://github.com/tristan-greffe' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/tristan-greffe' }
    ],
    nav: [
      { text: 'About', link: '/about/introduction' },
      { text: 'Learning', link: '/learning/introduction' },
      { text: 'Labs', link: '/labs/introduction' },
      { text: 'Resources', link: '/resources/introduction' }
    ],
    sidebar: {
      '/about/': getAboutSidebar()
    },
    footer: {
      copyright: 'MIT Licensed | Copyright © 2024 Tristan Greffe'
    }
  }
})

function getAboutSidebar (lang = 'en') {
  if (lang === 'en') {
    return [
      { text: 'About', link: '/about/introduction' },
      { text: 'Contributing', link: '/about/contributing' },
      { text: 'License', link: '/about/license' }
    ]
  }
  return [
    { text: 'A propos', link: '/fr/about/introduction' },
    { text: 'Contribuer', link: '/fr/about/contributing' },
    { text: 'Licence', link: '/fr/about/license' }
  ]
}

function getLearningSidebar () {
  return [
    { text: 'Parcours Data Science & Machine Learning', link: '/fr/learning/introduction' },
    { text: 'Mathématiques',
      collapsed: true,
      items: [
        { text: 'Introduction', link: '/fr/learning/mathematics/introduction' },
        { text: 'Vecteurs',
          collapsed: true,
          items: [
            { text: 'Introduction', link: '/fr/learning/mathematics/vectors/introduction' },
            { text: 'Notions de base', link: '/fr/learning/mathematics/vectors/basic-concepts' },
            { text: 'Opérations Fondamentales', link: '/fr/learning/mathematics/vectors/operation' },
            { text: 'Produit Scalaire', link: '/fr/learning/mathematics/vectors/dot-product' },
            { text: 'Projection', link: '/fr/learning/mathematics/vectors/projection' },
            { text: 'Base vectorielle', link: '/fr/learning/mathematics/vectors/basis' }
          ]
        }
      ]
    },
    { text: 'Bibliothèques',
      collapsed: true,
      items: [
        { text: 'NumPy', link: '/fr/learning/libraries/numpy' },
        { text: 'Pandas',
          collapsed: true,
          items: [
            { text: 'Introduction', link: '/fr/learning/libraries/pandas/introduction' },
            { text: 'Series', link: '/fr/learning/libraries/pandas/series' },
            { text: 'DataFrames', link: '/fr/learning/libraries/pandas/data-frames' },
            { text: 'Filtrage conditionnel', link: '/fr/learning/libraries/pandas/conditional-filtering' },
            { text: 'Useful methods', link: '/fr/learning/libraries/pandas/useful-methods' },
            { text: 'Missing data', link: '/fr/learning/libraries/pandas/missing-data' },
            { text: 'GroupBy operation', link: '/fr/learning/libraries/pandas/groupby-operation' },
            { text: 'DataFrame combination', link: '/fr/learning/libraries/pandas/data-frames-combination' },
            { text: 'Inpu & output', link: '/fr/learning/libraries/pandas/introduction' }
          ]
        },
        { text: 'Matplotlib',
          collapsed: true,
          items: [
            { text: 'Introduction', link: '/fr/learning/libraries/matplotlib/introduction' },
          ]
        },
        { text: 'Seaborn',
          collapsed: true,
          items: [
            { text: 'Introduction', link: '/fr/learning/libraries/seaborn/introduction' },
          ]
        },
      ]
    }
  ]
}

function getLabsSidebar () {
  return [
    { text: 'Ateliers', link: '/fr/labs/introduction' }
  ]
}