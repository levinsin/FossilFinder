# FossilFinder

Ein interaktives Wortratespiel, bei dem du Dinosauriernamen erraten musst!

[![Tests](https://img.shields.io/badge/tests-34%2F34%20%E2%9C%93-brightgreen)](./test/)
[![Coverage](https://img.shields.io/badge/coverage-98%25-brightgreen)](./documentation/documentation.md#42-coverage)
[![MyPy](https://img.shields.io/badge/mypy-passing-brightgreen)](./documentation/documentation.md#43-mypy)
[![Pylint](https://img.shields.io/badge/pylint-10.0%2F10.0-brightgreen)](./documentation/documentation.md#44-pylint)
[![Python](https://img.shields.io/badge/python-3.12%2B-blue)](./documentation/documentation.md#5-versionsangaben)

---

## Überblick

**FossilFinder** ist ein Hangman-ähnliches Spiel, bei dem der Spieler versucht, den Namen eines Dinosauriers zu erraten. Du hast **6 Fehlversuche** pro Runde und kannst entweder einzelne Buchstaben oder das gesamte Wort erraten.

### Spielmechanik

- **Einzelne Buchstaben raten**: Für jeden falschen Buchstaben verlierst du einen Lebenspunkt
- **Ganze Wörter raten**: Wenn du falsch liegst, kostet dich das auch einen Lebenspunkt
- **6 Lebenspunkte**: Bei 6 Fehlversuchen ist die Runde verloren
- **Bis zu 10 Spielrunden** pro Spielsession
- **Spielverlauf-Anzeige**: Am Ende wird dein Score angezeigt

---

## Installation & Start

### Anforderungen

- Python **3.12+**
- (Optional) `coverage`, `mypy`, `pylint` für Code-Analyse

### Projekt starten

```bash
cd FossilFinder
python -m source.game
```

---

## Tests & Code-Qualität

### Tests ausführen

Um die Tests ausführen zu lassen, sollten die folgenden drei Tools installiert werden:
- coverage 7.13.5
- mypy 1.19.1
- pylint 4.0.5


```bash
python3.14 -m unittest discover test/ -v

python3.14 -m coverage run -m unittest discover test/
python3.14 -m coverage report
```

### Code-Analyse

```bash
mypy source/

pylint source/

coverage report --show-missing
```

### Metriken

| Tool | Status | Details |
|------|--------|---------|
| **Tests** | 43/43 bestanden | Vollständige Test-Abdeckung |
| **Coverage** | 99% | Nur minimale Ausnahmen |
| **MyPy** | keine Beanstandungen | Strikte Type-Checking |
| **Pylint** | 10.0/10.0 | Hohe Code-Qualität |

---

## Projektstruktur

```
FossilFinder/
├── source/                      # Spiellogik
│   ├── game.py                 # Spielschleife
│   ├── engine.py               # GameEngine
│   ├── ui_creator.py           # UI & Terminal-Ausgabe
│   ├── word_provider.py        # Wort-Management
│   └── wordrepo.txt            # Dinosaurier-Namen
├── test/                        # Unit Tests
│   ├── test_game.py
│   ├── test_engine.py
│   ├── test_ui_creator.py
│   └── test_word_provider.py
├── documentation/               # Umfangreiche Dokumentation
│   ├── documentation.md         # Vollständige Doku
│   └── img/                     # Screenshots & Diagramme
├── mypy.ini                     # MyPy Konfiguration
├── .pylintrc                    # Pylint Konfiguration
├── requirements.txt             # Abhängigkeiten
└── README.md                    # Dieses File
```

---

## Abbruchszenarios

Das Spiel endet automatisch, wenn:

1. **Spieler gewinnt**: Ganzes Wort erraten
2. **Spieler verliert**: 6 Fehlversuche erreicht
3. **Max. Rundenzahl**: 10 Spiele gespielt
4. **Spieler beendet**: Nach jeder vollständigen Runde möglich (Input: "n")

---

## Weitere Dokumentation

Für detaillierte Informationen siehe:
- [`documentation/documentation.md`](./documentation/documentation.md) — Vollständige Architektur & Implementation
- [`test/`](./test/) — 43 Unit Tests mit hoher Abdeckung

---

## Technische Details

- **Sprache**: Python 3.12
- **Testing**: `unittest` + `coverage`
- **Type Checking**: MyPy (strict mode)
- **Linting**: Pylint (Rating: 10.0/10.0)
- **Architektur**: Objekt-orientiert, modulare Struktur

---

## Lizenz

[Siehe LICENSE](./LICENSE)

---

**Viel Spaß beim Spielen!**