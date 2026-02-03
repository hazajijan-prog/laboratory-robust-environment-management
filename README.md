# Laboratory – Robust Environment Management

Detta repository är en laboration i kursen MLOps som fokuserar på att skapa en **robust och reproducerbar Python-miljö** för maskininlärningsprojekt.

Målet är att använda moderna verktyg (som `uv` och `pyproject.toml`) för att hantera beroenden på ett stabilt.
---

## Projektinnehåll

Repo:t innehåller:

- `pyproject.toml` – projektets beroenden och miljödefinition  
- `uv.lock` – låst versionsfil för reproducerbara installationer  
- `check_env.py` – script som verifierar att miljön fungerar korrekt  
- `README.md` – instruktioner och reflektion kring uppgiften  

## Kör verifieringen

För att verifiera att miljön fungerar korrekt kör: 
bash 
uv run check_env.py

---

## Reflektion: Problem och lösningar under miljöuppsättningen
Under arbetet upptäckte jag snabbt att maskininlärningsmiljöer kan vara känsliga för versionskonflikter mellan bibliotek.

Detta projekt handlade därför inte bara om att installera paket, utan om att förstå varför vissa versioner och val behövdes för att få en stabil miljö.

## Problem jag stötte på

Ett av de första problemen var att PyTorch inte kunde installeras med vissa versioner:
torch==2.10.0 can't be installed
because it doesn't have a wheel for the current platform

Detta betyder att versionen saknade stöd för min plattform (Intel macOS). 
Lösningen blev att använda en version som fungerade korrekt:
Jag pinade den version som fungerade korrekt:
torch==2.2.2

## Reflektion
Stora ML-bibliotek som PyTorch är beroende av att rätt binära version (“wheel”) finns tillgänglig för operativsystemet.

## Lösning
Jag pinade den version som fungerade korrekt:
torch==2.2.2


## Problem 2: NumPy 2.x skapade inkompatibilitet med Torch

Efter installation uppstod varningen:
A module compiled using NumPy 1.x cannot be run in NumPy 2.x

### Vad betyder felet?
Torch var kompilerat mot NumPy 1.x, och NumPy 2.x kan orsaka krascher.

### Reflektion
När stora bibliotek gör en major-versionändring tar det tid innan hela ekosystemet blir kompatibelt.

### Lösning
Jag begränsade NumPy-versionen:
numpy<2.0


## Problem 3: Pandas-versioner krävde NumPy ≥2.x

### Vid dependency resolution uppstod konflikter:

pandas>=3.0 depends on numpy>=2.3.3
but project requires numpy<2.0

### Vad betyder felet?
Pandas 3.x kräver NumPy 2.x, vilket krockade med Torch.

### Reflektion
Dependency conflicts är vanliga i ML-miljöer och visar varför versionskontroll är viktig.

### Lösning
Jag begränsade Pandas till en kompatibel version:

pandas<3.0

## Problem 4: PyTorch behövde ett separat installationsindex
För att få korrekt CPU-version av PyTorch behövde jag använda PyTorchs officiella index:

[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cpu"
explicit = true

### Reflektion
PyTorch distribueras ibland via egna index för att rätt CPU/GPU-version ska installeras.

-- 

## Problem 5: VS Code hittade inte paketen trots att miljön fungerade
Trots att uv run check_env.py fungerade visade VS Code:
Import "torch" could not be resolved (Pylance)

### Vad betyder felet?
Paketen var installerade i .venv, men VS Code använde en annan interpreter globalt.

### Lösning
Jag valde rätt interpreter manuellt:

.venv/bin/python

### Reflektion
Det visar att reproducerbarhet inte bara handlar om installation utan även om att utvecklingsmiljön är korrekt kopplad till rätt venv.


## Script för miljöverifiering
### check_env.py kontrollerar:
- Python-version
- Versioner för pandas, scikit-learn och torch
- GPU-stöd (CUDA/MPS/CPU)
- En enkel tensorberäkning