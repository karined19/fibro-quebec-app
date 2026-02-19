from __future__ import annotations

from pathlib import Path
import streamlit as st

from utils.repository import JSONResourceRepository

[
  {
    "id": "sqf",
    "name": "Société québécoise de la fibromyalgie (SQF)",
    "category": "fibromyalgie",
    "description": "Regroupe et représente des associations régionales qui soutiennent les personnes vivant avec la fibromyalgie et leurs proches. Offre de l'information, des ressources et des liens vers des organismes membres partout au Québec.",
    "website_url": "https://www.sqf.quebec/",
    "region_covered": "Province entière",
    "tags": ["fibromyalgie", "associations", "ressources", "Québec"],
    "services": ["bottin", "information", "orientation", "soutien"]
  },
  {
    "id": "fibromyalgie-montreal",
    "name": "Fibromyalgie Montréal",
    "category": "fibromyalgie",
    "description": "Organisme communautaire qui informe et soutient les personnes vivant avec la fibromyalgie dans la région de Montréal. Propose des activités, du soutien et de la documentation pour mieux s'orienter.",
    "website_url": "https://www.fibromyalgiemontreal.ca/",
    "region_covered": "Montréal",
    "tags": ["Montréal", "groupes", "information", "activités"],
    "services": ["soutien", "information", "accompagnement"]
  },
  {
    "id": "aqdc",
    "name": "Association québécoise de la douleur chronique (AQDC)",
    "category": "douleur_chronique",
    "description": "Soutient les personnes vivant avec une douleur chronique et contribue à réduire l'isolement. Offre des ressources, conférences et services d'entraide selon les régions.",
    "website_url": "https://douleurquebec.ca/",
    "region_covered": "Province entière",
    "tags": ["douleur chronique", "entraide", "conférences", "ressources"],
    "services": ["soutien", "information", "accompagnement"]
  },
  {
    "id": "fibromyalgie-monteregie",
    "name": "Fibromyalgie Montérégie (AFRM)",
    "category": "fibromyalgie",
    "description": "Aide et soutient les personnes atteintes de fibromyalgie en Montérégie. Met à disposition de l'information, des références et des outils d'auto-prise en charge.",
    "website_url": "https://www.fibromyalgiemonteregie.ca/",
    "region_covered": "Montérégie",
    "tags": ["Montérégie", "fibromyalgie", "soutien", "documentation"],
    "services": ["soutien", "information", "accompagnement", "bottin"]
  },
  {
    "id": "fibro-124",
    "name": "FIBRO-124 (bottin de ressources)",
    "category": "navigation",
    "description": "Bottin de ressources relayé par des organismes de fibromyalgie pour faciliter l'orientation vers des services et associations. Utile pour trouver des pistes de soutien, d'information et d'accompagnement.",
    "website_url": "https://www.fibromyalgiemonteregie.ca/fibro-124",
    "region_covered": "Province entière",
    "tags": ["bottin", "orientation", "ressources", "fibromyalgie"],
    "services": ["bottin", "navigation", "orientation"]
  },
  {
    "id": "fibro-canada",
    "name": "Fibro Canada (Fibromyalgia Association Canada)",
    "category": "fibromyalgie",
    "description": "Organisation nationale visant à améliorer la qualité de vie des personnes vivant avec la fibromyalgie au Canada. Offre information, sensibilisation et liens utiles.",
    "website_url": "https://fibrocanada.ca/fr",
    "region_covered": "Canada",
    "tags": ["Canada", "sensibilisation", "information", "fibromyalgie"],
    "services": ["information", "orientation"]
  },
  {
    "id": "proche-aidance-quebec",
    "name": "Proche aidance Québec",
    "category": "proches_aidants",
    "description": "Regroupe des organismes communautaires qui soutiennent les personnes proches aidantes à travers le Québec. Permet d'identifier des ressources et de mieux s'orienter vers du soutien.",
    "website_url": "https://procheaidance.quebec/",
    "region_covered": "Province entière",
    "tags": ["proches aidants", "organismes", "soutien", "Québec"],
    "services": ["bottin", "orientation", "information", "soutien"]
  },
  {
    "id": "lappui",
    "name": "L’Appui pour les proches aidants",
    "category": "proches_aidants",
    "description": "Service d'écoute, information et références pour personnes proches aidantes (dont Info-aidant) et répertoire de ressources par code postal. Soutient aussi des organismes via des projets et du financement.",
    "website_url": "https://www.lappui.org/fr/",
    "region_covered": "Province entière",
    "tags": ["Info-aidant", "répertoire", "répit", "écoute"],
    "services": ["soutien", "répit", "bottin", "accompagnement", "navigation"]
  },
  {
    "id": "juridiqc-credits",
    "name": "JuridiQC (aides financières et crédits)",
    "category": "aide_financiere",
    "description": "Portail juridique gouvernemental vulgarisé. Propose des pages pratiques et outils (ex: crédits d'impôt liés à la proche aidance) pour mieux comprendre ses options.",
    "website_url": "https://juridiqc.gouv.qc.ca/",
    "region_covered": "Québec",
    "tags": ["crédits d'impôt", "aide financière", "proche aidance", "juridique"],
    "services": ["information", "navigation", "aides financières", "orientation"]
  },
  {
    "id": "dfac",
    "name": "DFAC (Disability Financial Assistance Corporation)",
    "category": "aide_financiere",
    "description": "Organisation offrant de l'accompagnement pour accéder à certains programmes et bénéfices liés au handicap. Sert de point d'orientation pour démêler des démarches administratives complexes.",
    "website_url": "https://dfac.ca/",
    "region_covered": "Canada",
    "tags": ["handicap", "bénéfices", "formulaires", "accompagnement"],
    "services": ["accompagnement", "navigation", "aides financières"]
  },
  {
    "id": "aqeips",
    "name": "AQEIPS (équité et inclusion au postsecondaire)",
    "category": "navigation",
    "description": "Organisme 'par et pour' les personnes étudiantes en situation de handicap au postsecondaire. Offre information, défense de droits et un programme de bourses.",
    "website_url": "https://aqeips.org/",
    "region_covered": "Québec",
    "tags": ["études", "handicap", "bourses", "droits"],
    "services": ["information", "aides financières", "accompagnement", "navigation"]
  },
  {
    "id": "ophq",
    "name": "Office des personnes handicapées du Québec (OPHQ)",
    "category": "navigation",
    "description": "Organisme gouvernemental visant à accroître la participation sociale des personnes handicapées. Propose information, ressources et contenus sur l'accessibilité et les droits.",
    "website_url": "https://www.ophq.gouv.qc.ca/",
    "region_covered": "Québec",
    "tags": ["gouvernement", "handicap", "droits", "accessibilité"],
    "services": ["information", "navigation", "orientation"]
  },
  {
    "id": "plan-institute",
    "name": "Plan Institute",
    "category": "navigation",
    "description": "Organisation canadienne offrant des ressources éducatives et du soutien sur la planification liée au handicap. Partage aussi de l'information sur des prestations nationales.",
    "website_url": "https://planinstitute.ca/",
    "region_covered": "Canada",
    "tags": ["planification", "prestations", "handicap", "information"],
    "services": ["information", "navigation", "orientation"]
  },
  {
    "id": "disability-benefits-compass",
    "name": "Disability Benefits Compass",
    "category": "aide_financiere",
    "description": "Outil d'orientation pour comprendre les principaux bénéfices liés au handicap et savoir par où commencer. Conçu pour les personnes, proches et intervenants qui veulent une vue claire des options.",
    "website_url": "https://disability.benefitswayfinder.org/",
    "region_covered": "Canada",
    "tags": ["bénéfices", "handicap", "orientation", "prestations"],
    "services": ["navigation", "information", "aides financières"]
  },
  {
    "id": "4korners",
    "name": "4Korners (Laurentides)",
    "category": "navigation",
    "description": "Organisme communautaire caritatif qui connecte la communauté anglophone des Laurentides à des programmes et services. Offre aussi des pages ressources (incluant handicaps et troubles).",
    "website_url": "https://4korners.org/",
    "region_covered": "Laurentides",
    "tags": ["Laurentides", "anglais", "communautaire", "ressources"],
    "services": ["information", "navigation", "orientation", "accompagnement"]
  }
]
