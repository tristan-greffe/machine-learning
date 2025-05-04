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
        { text: 'NumPy', link: '/fr/learning/libraries/numpy/introduction' },
        { text: 'Pandas',
          collapsed: true,
          items: [
            { text: 'Introduction', link: '/fr/learning/libraries/pandas/introduction' },
            { text: 'Series', link: '/fr/learning/libraries/pandas/series' },
            { text: 'DataFrames', link: '/fr/learning/libraries/pandas/data-frames' },
            { text: 'Données manquantes', link: '/fr/learning/libraries/pandas/missing-data' },
            { text: 'Input & output', link: '/fr/learning/libraries/pandas/input-output' },
            { text: 'Projet', link: '/fr/learning/libraries/pandas/project' }
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
    },
    { text: 'Concepts',
      collapsed: true,
      items: [
        { text: 'Introduction', link: '/fr/learning/concepts/introduction' }
      ]
    },
    { text: 'Algorithmes d’apprentissage supervisé',
      collapsed: true,
      items: [
        { text: 'Introduction', link: '/fr/learning/algorithms/introduction' },
        { text: 'Régression linéaire',
          collapsed: true,
          items: [
            { text: 'Introduction', link: '/fr/learning/algorithms/linear-regression/introduction' }
          ]
        },
        { text: 'Régression logistique',
          collapsed: true,
          items: [
            { text: 'Introduction', link: '/fr/learning/algorithms/logistic-regression/introduction' }
          ]
        },
        { text: 'KNN (K-Nearest Neighbors)',
          collapsed: true,
          items: [
            { text: 'Introduction', link: '/fr/learning/algorithms/knn/introduction' }
          ]
        },
        { text: 'SVM (Support Vector Machine)',
          collapsed: true,
          items: [
            { text: 'Introduction', link: '/fr/learning/algorithms/svm/introduction' }
          ]
        },
        { text: 'Arbre de décision',
          collapsed: true,
          items: [
            { text: 'Introduction', link: '/fr/learning/algorithms/decision-tree/introduction' }
          ]
        },
        { text: 'Random Forest',
          collapsed: true,
          items: [
            { text: 'Introduction', link: '/fr/learning/algorithms/random-forest/introduction' }
          ]
        },
        { text: 'Méthodes de Boosting',
          collapsed: true,
          items: [
            { text: 'Introduction', link: '/fr/learning/algorithms/boosting/introduction' }
          ]
        },
        
      ]
    },
    { text: 'Deep Learning',
      collapsed: true,
      items: [
        { text: 'Introduction', link: '/fr/learning/deep-learning/introduction' }
      ]
    },
    { text: 'Fine-Tuning',
      collapsed: true,
      items: [
        { text: 'Introduction', link: '/fr/learning/fine-tuning/introduction' }
      ]
    },
    { text: 'RAG (Retrieval-Augmented Generation)',
      collapsed: true,
      items: [
        { text: 'Introduction', link: '/fr/learning/rag/introduction' }
      ]
    }
  ]
}

function getLabsSidebar () {
  return [
    { text: 'Ateliers', link: '/fr/labs/introduction' },
    { text: 'Détecteur de visage',
      collapsed: true,
      items: [
        { text: 'Introduction', link: '/fr/labs/introduction' }
      ]
    },
    { text: 'Classificateur d\'images',
      collapsed: true,
      items: [
        { text: 'Introduction', link: '/fr/labs/introduction' }
      ]
    },
    { text: 'IA de reconnaissance d\'écriture manuscrite',
      collapsed: true,
      items: [
        { text: 'Introduction', link: '/fr/labs/introduction' }
      ]
    },
    { text: 'Détecteur de Spam',
      collapsed: true,
      items: [
        { text: 'Introduction', link: '/fr/labs/introduction' }
      ]
    },
    { text: 'Reconnaissance Faciale',
      collapsed: true,
      items: [
        { text: 'Introduction', link: '/fr/labs/introduction' }
      ]
    }
  ]
}