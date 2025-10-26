# IPKO TV Scraper

Kjo skriptë përdor gjuhën programuese **Python** për të nxjerrë të dhëna mbi programet televizive nga [IPKO TV](https://ipko.tv) dhe për të gjeneruar JSON files për cdo ditë të caktuara, për analizë dhe përdorim të mëtejshëm.

---

## Karakteristikat kryesore
- Merr të dhënat për të gjitha kanalet televizive IPKO.
- Lejon zgjedhjen e diapazonit të datave (ditët e kaluara dhe të ardhshme).
- Gjeneron automatikisht:
  - Oraret e fillimit dhe të përfundimit.
  - Preferencat e shikuesëve.
  - Blloqet e përparësisë bazuar në dendësinë e kanalit.
  - Listat e kanaleve dhe programeve me zhanre dhe rezultate.
- Nxjerr një JSON file gati për përdorim për secilën datë (p.sh. `2ipko_schedule_2025-10-26.json`). 

---

## Si të përdoret

Duhet të keni të instaluar **Python 3.8+** dhe libraritë e mëposhtme:

```bash
pip install requests
```

---

## 2. Ekzekutoni skriptën

   ```bash
   python ipko.py
   ```

4. Plotësoni të dhënat e kërkuara:
   - Sa ditë **para sot** dëshironi të merrni të dhëna.
   - Sa ditë **pas sot** dëshironi të merrni të dhëna.

   Shembull:
   ```
   Sa ditë më parë nga sot dëshironi të merrni të dhëna? 1
   Sa ditë nga sot dëshironi të merrni të dhëna? 2
   ```

   Kjo do të marrë të dhëna nga **dje deri pasnesër**.

---

## Skripta gjeneron JSON për çdo ditë

```
2ipko_schedule_2025-10-26.json
```

Struktura e JSON-it:
```json
{
  "opening_time": 480,
  "closing_time": 1380,
  "channels": [
    {
      "channel_id": 0,
      "channel_name": "rtk-1",
      "programs": [
        {
          "program_id": "rtk-1_1",
          "start": 540,
          "end": 600,
          "genre": "news",
          "score": 75
        }
      ]
    }
  ]
}
```

---
