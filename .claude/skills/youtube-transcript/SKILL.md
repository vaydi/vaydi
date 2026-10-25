---
name: youtube-transcript
description: Récupère la transcription (sous-titres) d'une vidéo YouTube puis la résume, en extrait les étapes ou répond à des questions sur son contenu. À utiliser dès que l'utilisateur colle un lien YouTube (youtube.com, youtu.be, shorts) ou demande de « lire », « résumer » ou « tirer un tuto » d'une vidéo.
---

# YouTube → Claude : lire une vidéo via sa transcription

Claude ne regarde pas les vidéos : il lit leur **transcription**. Ce skill la récupère
avec `scripts/get_transcript.py`, puis travaille sur le texte.

## Étapes

1. **Installer la dépendance** (une seule fois) :
   ```bash
   pip install youtube-transcript-api
   ```
2. **Récupérer la transcription** (URL complète ou ID de 11 caractères) :
   ```bash
   python3 .claude/skills/youtube-transcript/scripts/get_transcript.py "<URL>" --lang fr en
   ```
   - `--lang` : langues par ordre de préférence (défaut : `fr en`).
   - `--timestamps` : préfixe chaque ligne par `[mm:ss]`, utile pour citer un passage.
   - `--list` : affiche les langues de sous-titres disponibles.
3. **Traiter le texte** selon la demande :
   - *Résumé* : idée principale, puis 3 à 7 points clés.
   - *Tutoriel* : liste numérotée d'étapes concrètes (commandes, fichiers, réglages),
     avec l'horodatage de chaque étape si `--timestamps` a été utilisé.
   - *Question* : répondre en citant le passage et son horodatage.
4. Indiquer clairement si la transcription est générée automatiquement : les noms
   propres et termes techniques peuvent y être mal orthographiés.

## Si ça échoue

- `TranscriptsDisabled` / `NoTranscriptFound` : la vidéo n'a pas de sous-titres dans
  ces langues. Relancer avec `--list`, puis choisir une langue disponible.
- Erreur réseau ou 403 : l'environnement bloque `youtube.com`. Le dire à l'utilisateur
  et lui demander de coller la transcription (YouTube → « … » → *Afficher la transcription*).
- Ne jamais inventer le contenu d'une vidéo qu'on n'a pas pu lire.

Les liens Facebook, Instagram ou TikTok ne sont pas pris en charge : demander à
l'utilisateur de coller la légende ou la transcription.
