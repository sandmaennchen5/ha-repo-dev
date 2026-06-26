# Fehlerbehandlung & Troubleshooting

## ⚠️ Workflow Errors

### Invalid workflow file

**Problem:** GitHub zeigt "Invalid workflow file" Error

**Lösungen:**
1. YAML-Syntax prüfen (keine Tabs, richtige Einrückung)
   ```bash
   python -m py_compile .github/workflows/translate.yml
   ```

2. Sonderzeichen in Variablen vermeiden
   - `TARGET_LANGUAGES: "en,fr,es"` ✅
   - `TARGET_LANGUAGES: en, fr, es` ❌ (mit Leerzeichen)

3. Quotes richtig setzen
   ```yaml
   run: gh variable set KEY -b "value"  # Richtig
   run: gh variable set KEY --body value # Falsch
   ```

### Permission denied

**Problem:** Workflow kann nicht pushen oder PRs erstellen

**Lösungen:**
1. Check Workflow Permissions:
   ```bash
   gh repo view --json repositoryTopics
   ```

2. Token Scopes prüfen:
   - `contents: write` ✅ (für Commits/Pushes)
   - `pull-requests: write` ✅ (für PRs)

3. Branch Protection Rules prüfen:
   - Erlaubt `github-actions[bot]` Commits?
   - Erlaubt Direct Pushes (kein Review)?

---

## 📊 Variable/Secret Errors

### Variable not found

**Problem:** `TARGET_LANGUAGES` wird nicht gefunden

**Quick Fix:**
```bash
# Variable manuell setzen
gh variable set TARGET_LANGUAGES -b "en,fr,es"

# Oder mit GitHub UI:
# Settings → Secrets and variables → Variables → New variable
```

### DEEPL_API_KEY nicht vorhanden

**Problem:** Workflow gibt Fehler, obwohl KEY gesetzt

**Lösung:** MyMemory Fallback ist aktiviert!
- Workflow funktioniert auch ohne DeepL
- Qualität ist gut (80-90% korrekt)
- Mit DeepL Key bessere Qualität (95%+)

```bash
# Key nachträglich hinzufügen
gh secret set DEEPL_API_KEY -b "sk-..."

# Oder leer lassen, Fallback wird genutzt
```

---

## 🔄 Workflow Issues

### Workflow läuft nicht

**Ursachen:**
1. Push auf falschen Branch (muss `main` sein)
2. Keine deutschen Dateien geändert
3. Workflow deaktiviert

**Check:**
```bash
# Workflow Status
gh workflow list -w translate.yml

# Manuell starten
gh workflow run translate.yml -r main

# Logs prüfen
gh run list -w translate.yml --limit 1 | head -1
```

### Nur manche Dateien übersetzt

**Problem:** README.md wird übersetzt, DOCS.md nicht

**Ursachen:**
- Falsche Dateistruktur
- Datei nicht im richtigen Pfad
- Dateiname exakt korrekt?

**Unterstützte Pfade:**
```
✅ README.md          (Root)
✅ DOCS.md            (Root)
✅ apps/foo/README.md
✅ apps/foo/DOCS.md
✅ apps/foo/translations/de.yaml
✅ apps/foo/translations/de.yml
✅ apps/foo/translations/de.json

❌ readme.md          (Kleinbuchstaben)
❌ App/README.md      (Großbuchstaben im Pfad)
❌ docs/de.yaml       (Wrong location)
```

---

## 🐛 Translation Issues

### Schlechte Übersetzungen

**Mit MyMemory:**
- Einfache Texte: Gut
- Technische Texte: Schwächer
- Lange Sätze: Fehler möglich

**Lösungen:**
1. DeepL Key hinzufügen (beste Qualität)
   ```bash
   gh secret set DEEPL_API_KEY -b "your-key"
   ```

2. Deutschen Text verbessern:
   - Klare, kurze Sätze
   - Keine Slang/Jargon
   - Markdown richtig formatieren

3. Cache leeren (neuer Versuch):
   ```bash
   git checkout i18n-update
   rm -rf .i18n_cache/
   git add .i18n_cache/
   git commit -m "clear cache"
   git push origin i18n-update
   ```

### Text wird nicht übersetzt

**Problem:** Original-Deutsch bleibt in Übersetzung

**Ursachen:**
1. API-Fehler (Rate Limit?)
2. Leerer/ungültiger Text
3. Network-Fehler

**Debug:**
```bash
# PR aufrufen und neue Übersetzung forcen
git checkout i18n-update
rm .i18n_cache/translation_cache.json
git add .i18n_cache/
git commit -m "force retranslation"
git push origin i18n-update
```

---

## 🔗 PR Issues

### PR wird nicht erstellt

**Problem:** Keine PR sichtbar, obwohl Workflow erfolgreich

**Ursachen:**
1. Keine Änderungen (Cache-Hit)
2. PR existiert bereits
3. GitHub Permissions fehlen

**Check:**
```bash
# Existierende PRs
gh pr list --head i18n-update

# Alle Commits in Branch
git log origin/i18n-update --oneline -n 5

# Erzwinge PR-Erstellung
gh pr create \
  --base main \
  --head i18n-update \
  --title "chore(i18n): translations" \
  --body "Updated translations"
```

### PR wird nicht aktualisiert

**Problem:** Neue Übersetzungen werden nicht in offene PR committed

**Ursationen:**
1. Branch-Versatz (rebase nötig)
2. Workflow läuft parallel
3. Commit-Fehler

**Manuell beheben:**
```bash
# i18n-update lokal aktualisieren
git checkout i18n-update
git pull origin i18n-update
git rebase origin/main

# Lokale Änderungen machen
# ...

git add .
git commit -m "chore(i18n): update"
git push origin i18n-update
```

---

## 🔧 Debug-Tipps

### Workflow-Logs anschauen

```bash
# Letzte Ausführung
gh run list -w translate.yml --limit 1

# Logs downloaden
gh run view <RUN_ID> --log > workflow.log

# Live folgen
gh workflow run translate.yml -r main
gh run list -w translate.yml --limit 1
while true; do
  gh run view $(gh run list -w translate.yml --limit 1 --json databaseId --jq '.[0].databaseId') --log
  sleep 5
done
```

### Git History prüfen

```bash
# Commits in i18n-update
git log origin/i18n-update --oneline -n 10

# Was ist anders zu main?
git diff main...origin/i18n-update --stat

# Welche Dateien wurden verändert?
git diff --name-only main...origin/i18n-update
```

### Cache prüfen

```bash
# Cache Datei ansehen
git show origin/i18n-update:.i18n_cache/translation_cache.json | jq .

# Cache Größe
git show origin/i18n-update:.i18n_cache/translation_cache.json | wc -c
```

---

## 💡 Best Practices

### Regelmäßige Maintenance

```bash
# Wöchentlich: Cache leeren (für Qualität)
git checkout i18n-update
rm -rf .i18n_cache/
git add .i18n_cache/
git commit -m "chore: reset translation cache"
git push origin i18n-update
```

### Übersetzungen reviewen

```bash
# PR Diff anschauen
gh pr view <NUMBER> --web

# Oder lokal
git checkout i18n-update
git diff main... -- '*.en.md'
```

### Performance optimieren

```bash
# Cache nicht synchronisieren (wenn klein)
# → .gitignore hinzufügen (optional):
echo ".i18n_cache/translation_cache.json" >> .gitignore

# Oder als Artefakt speichern (GitHub Actions)
```

---

## 📞 Mehr Hilfe

Fehler-Logs sammeln:
```bash
gh workflow run translate.yml -r main
gh run list -w translate.yml --limit 1 | head -1
gh run view <RUN_ID> --log | tail -50
```

Dann issue erstellen:
```bash
gh issue create -t "Translation workflow error" \
  -b "$(gh run view <RUN_ID> --log | tail -100)"
```

---

**Letztes Update:** $(date)
