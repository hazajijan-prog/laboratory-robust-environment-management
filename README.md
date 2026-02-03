# Laboratory – Robust Environment Management

Detta repository är en laboration i kursen **MLOps** som fokuserar på att skapa en  
**robust och reproducerbar Python-miljö** för maskininlärningsprojekt.

Målet är att använda moderna verktyg (som `uv` och `pyproject.toml`) för att hantera beroenden på ett stabilt sätt.

---

## Projektinnehåll

Repo:t innehåller:

- `pyproject.toml` – projektets beroenden och miljödefinition  
- `uv.lock` – låst versionsfil för reproducerbara installationer  
- `check_env.py` – script som verifierar att miljön fungerar korrekt  
- `README.md` – instruktioner och reflektion kring uppgiften  


## Kör verifieringen

För att verifiera att miljön fungerar korrekt kör:

``bash
uv run check_env.py

---

Reflektion: Problem och lösningar under miljöuppsättningen
Under arbetet upptäckte jag snabbt att maskininlärningsmiljöer kan vara känsliga för versionskonflikter mellan bibliotek.

Detta projekt handlade därför inte bara om att installera paket, utan om att förstå varför vissa versioner och val behövdes för att få en stabil miljö.

Problem jag stötte på:
Problem 1: PyTorch kunde inte installeras

PyTorch kunde inte installeras med vissa versioner:

torch==2.10.0 can't be installed
because it doesn't have a wheel for the current platform


Orsak: Versionen saknade stöd för Intel macOS.

Lösning:
torch==2.2.2


Reflektion:
Stora ML-bibliotek som PyTorch kräver att rätt binära version (“wheel”) finns tillgänglig för operativsystemet.

Problem 2: NumPy 2.x skapade inkompatibilitet med Torch

Efter installation uppstod varningen:
A module compiled using NumPy 1.x cannot be run in NumPy 2.x

Lösning:
numpy<2.0


Reflektion:
När stora bibliotek gör en major-versionändring tar det tid innan hela ekosystemet blir kompatibelt.

Problem 3: Pandas-versioner krävde NumPy ≥2.x

Dependency-konflikt:

pandas>=3.0 depends on numpy>=2.3.3
but project requires numpy<2.0

Lösning:
pandas<3.0

Reflektion:
Dependency conflicts är vanliga i ML-miljöer och visar varför versionskontroll är viktig.

Problem 4: PyTorch behövde ett separat installationsindex

För korrekt CPU-version behövdes PyTorchs officiella index:

[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cpu"
explicit = true


Reflektion:
PyTorch distribueras ibland via egna index för att rätt CPU/GPU-version ska installeras.

Problem 5: VS Code hittade inte paketen trots att miljön fungerade

VS Code visade:
Import "torch" could not be resolved (Pylance)

Lösning:
Jag valde rätt interpreter manuellt:

.venv/bin/python


Reflektion:
Reproducerbarhet handlar inte bara om installation utan även om att utvecklingsmiljön är korrekt kopplad till rätt venv.


Script för miljöverifiering
check_env.py kontrollerar:
- Python-version
- Versioner för pandas, scikit-learn och torch
- GPU-stöd (CUDA/MPS/CPU)
- En enkel tensorberäkning