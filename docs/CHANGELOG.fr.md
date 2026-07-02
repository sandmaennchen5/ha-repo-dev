# Changelog – Badge Framework

Ce changelog documente les modifications apportées au cadre du badge et à l'infrastructure du référentiel (pas aux applications individuelles).

## [1.0.0] – 2026-06-26

### Nouveau
- Structure de référentiel complète pour les add-ons Home Assistant et HACS
- Fichier de configuration central `.github/config.yaml` (badge + tableau de bord dans un fichier)
- **pipeline de transformation ** pour les badges : `replace`, `join`, `split`, `lower`, `upper`, `title`, `trim`, `url_encode`, `regex_replace`, `prefix`, `suffix`, `defa