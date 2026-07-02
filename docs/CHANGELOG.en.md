# Changelog – Badge Framework

This changelog documents changes to the badge framework and repository infrastructure (not individual apps).

## [1.0.0] – 2026-06-26

### New
- Complete repository structure for Home Assistant add-ons and HACS
- Central configuration file `.github/config.yaml` (badge + dashboard in one file)
- **Transform pipeline ** for badges: `replace`, `join`, `split`, `lower`, `upper`, `title`, `trim`, `url_encode`, `regex_replace`, `prefix`, `suffix`, `defa