#!/usr/bin/env python3
"""Affiche la transcription d'une vidéo YouTube sur la sortie standard."""
import argparse
import re
import sys

from youtube_transcript_api import YouTubeTranscriptApi

ID_PATTERN = re.compile(r"(?:v=|youtu\.be/|shorts/|embed/|live/)([A-Za-z0-9_-]{11})")


def video_id(value):
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", value):
        return value
    match = ID_PATTERN.search(value)
    if not match:
        sys.exit(f"Impossible de trouver l'ID de la vidéo dans : {value}")
    return match.group(1)


def timestamp(seconds):
    minutes, secs = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours}:{minutes:02d}:{secs:02d}" if hours else f"{minutes:02d}:{secs:02d}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", help="URL YouTube ou ID de la vidéo")
    parser.add_argument("--lang", nargs="+", default=["fr", "en"],
                        help="langues par ordre de préférence (défaut : fr en)")
    parser.add_argument("--timestamps", action="store_true",
                        help="préfixer chaque ligne par son horodatage")
    parser.add_argument("--list", action="store_true",
                        help="lister les langues de sous-titres disponibles")
    args = parser.parse_args()

    api = YouTubeTranscriptApi()
    vid = video_id(args.video)

    if args.list:
        for t in api.list(vid):
            kind = "auto" if t.is_generated else "manuel"
            print(f"{t.language_code}\t{t.language}\t({kind})")
        return

    transcript = api.fetch(vid, languages=args.lang)
    print(f"# Vidéo {vid} — langue : {transcript.language_code}"
          f"{' (générée automatiquement)' if transcript.is_generated else ''}")
    for snippet in transcript:
        text = snippet.text.replace("\n", " ").strip()
        if not text:
            continue
        print(f"[{timestamp(snippet.start)}] {text}" if args.timestamps else text)


if __name__ == "__main__":
    main()
