import requests
import json
import random
from datetime import datetime, timedelta, timezone

url = "https://stargate.ipko.tv/api/titan.tv.WebEpg/GetWebEpgData"

headers = {
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json",
    "origin": "https://ipko.tv",
    "referer": "https://ipko.tv/",
    "user-agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/141.0.0.0 Safari/537.36"
    ),
    "x-applayout": "1",
    "x-language": "sq"
}

urls = [
    "https://ipko.tv/tv-guide/ipko-promo",
    "https://ipko.tv/tv-guide/rtk-1",
    "https://ipko.tv/tv-guide/rtk-2",
    "https://ipko.tv/tv-guide/klan-kosova",
    "https://ipko.tv/tv-guide/rtv-21",
    "https://ipko.tv/tv-guide/ktv",
    "https://ipko.tv/tv-guide/t7",
    "https://ipko.tv/tv-guide/atv",
    "https://ipko.tv/tv-guide/tv-dukagjini",
    "https://ipko.tv/tv-guide/kanal-10",
    "https://ipko.tv/tv-guide/teve-1",
    "https://ipko.tv/tv-guide/pro1",
    "https://ipko.tv/tv-guide/vizion-+-hd",
    "https://ipko.tv/tv-guide/top-channel",
    "https://ipko.tv/tv-guide/dtv",
    "https://ipko.tv/tv-guide/alsat-m",
    "https://ipko.tv/tv-guide/klan",
    "https://ipko.tv/tv-guide/rtsh-1",
    "https://ipko.tv/tv-guide/rtsh-plus",
    "https://ipko.tv/tv-guide/rtsh-24",
    "https://ipko.tv/tv-guide/rtsh-shqip",
    "https://ipko.tv/tv-guide/rtsh-3",
    "https://ipko.tv/tv-guide/tring-tring",
    "https://ipko.tv/tv-guide/tring-kids",
    "https://ipko.tv/tv-guide/bubble",
    "https://ipko.tv/tv-guide/21-junior",
    "https://ipko.tv/tv-guide/sofia",
    "https://ipko.tv/tv-guide/prince-kids",
    "https://ipko.tv/tv-guide/tao-tao",
    "https://ipko.tv/tv-guide/kids",
    "https://ipko.tv/tv-guide/trt-cocuk",
    "https://ipko.tv/tv-guide/bang-bang",
    "https://ipko.tv/tv-guide/cufo",
    "https://ipko.tv/tv-guide/junior-tv",
    "https://ipko.tv/tv-guide/tring-family",
    "https://ipko.tv/tv-guide/smile",
    "https://ipko.tv/tv-guide/tring-shqip",
    "https://ipko.tv/tv-guide/tring-super-hd",
    "https://ipko.tv/tv-guide/tring-action-hd",
    "https://ipko.tv/tv-guide/tring-life",
    "https://ipko.tv/tv-guide/tring-comedy",
    "https://ipko.tv/tv-guide/tring-fantasy",
    "https://ipko.tv/tv-guide/tring-collection",
    "https://ipko.tv/tv-guide/tring-classics",
    "https://ipko.tv/tv-guide/gold-hd",
    "https://ipko.tv/tv-guide/max-hd",
    "https://ipko.tv/tv-guide/family-hd",
    "https://ipko.tv/tv-guide/eurofilm",
    "https://ipko.tv/tv-guide/film-autor",
    "https://ipko.tv/tv-guide/film-hits-hd",
    "https://ipko.tv/tv-guide/film-thriller",
    "https://ipko.tv/tv-guide/film-drame",
    "https://ipko.tv/tv-guide/film-aksion",
    "https://ipko.tv/tv-guide/film-komedi",
    "https://ipko.tv/tv-guide/star-movies",
    "https://ipko.tv/tv-guide/star",
    "https://ipko.tv/tv-guide/star-life",
    "https://ipko.tv/tv-guide/kino-1",
    "https://ipko.tv/tv-guide/kino-2",
    "https://ipko.tv/tv-guide/kino-3",
    "https://ipko.tv/tv-guide/premiere-1",
    "https://ipko.tv/tv-guide/premiere-2",
    "https://ipko.tv/tv-guide/premiere-3",
    "https://ipko.tv/tv-guide/premiere-4",
    "https://ipko.tv/tv-guide/tring-series",
    "https://ipko.tv/tv-guide/3-plus",
    "https://ipko.tv/tv-guide/turkish-stories",
    "https://ipko.tv/tv-guide/kanald-drama",
    "https://ipko.tv/tv-guide/novelas",
    "https://ipko.tv/tv-guide/stinet",
    "https://ipko.tv/tv-guide/t-hd",
    "https://ipko.tv/tv-guide/prime-tv",
    "https://ipko.tv/tv-guide/episode",
    "https://ipko.tv/tv-guide/doku-1",
    "https://ipko.tv/tv-guide/doku-2",
    "https://ipko.tv/tv-guide/tring-history",
    "https://ipko.tv/tv-guide/tring-planet",
    "https://ipko.tv/tv-guide/tring-world",
    "https://ipko.tv/tv-guide/living-hd",
    "https://ipko.tv/tv-guide/muse",
    "https://ipko.tv/tv-guide/gurmania",
    "https://ipko.tv/tv-guide/premium-channel",
    "https://ipko.tv/tv-guide/life-hd",
    "https://ipko.tv/tv-guide/terra-hd",
    "https://ipko.tv/tv-guide/exp-shkence",
    "https://ipko.tv/tv-guide/exp-histori",
    "https://ipko.tv/tv-guide/euro-d",
    "https://ipko.tv/tv-guide/euro-star",
    "https://ipko.tv/tv-guide/show-turk",
    "https://ipko.tv/tv-guide/show-maxx",
    "https://ipko.tv/tv-guide/tgrt-eu",
    "https://ipko.tv/tv-guide/a2",
    "https://ipko.tv/tv-guide/sky-360",
    "https://ipko.tv/tv-guide/tv8-int",
    "https://ipko.tv/tv-guide/kanal-7",
    "https://ipko.tv/tv-guide/dream-turk",
    "https://ipko.tv/tv-guide/power-turk",
    "https://ipko.tv/tv-guide/trt-muzik",
    "https://ipko.tv/tv-guide/tgrt-belgesel",
    "https://ipko.tv/tv-guide/trt-belgesel",
    "https://ipko.tv/tv-guide/trt-turk",
    "https://ipko.tv/tv-guide/trt-1",
    "https://ipko.tv/tv-guide/trt-world",
    "https://ipko.tv/tv-guide/tv-4",
    "https://ipko.tv/tv-guide/24-tv",
    "https://ipko.tv/tv-guide/a-haber",
    "https://ipko.tv/tv-guide/a-para",
    "https://ipko.tv/tv-guide/haber-turk",
    "https://ipko.tv/tv-guide/trt-haber",
    "https://ipko.tv/tv-guide/tgrt-haber",
    "https://ipko.tv/tv-guide/halk-tv",
    "https://ipko.tv/tv-guide/ulke-tv",
    "https://ipko.tv/tv-guide/beat-tv",
    "https://ipko.tv/tv-guide/rtsh-muzike",
    "https://ipko.tv/tv-guide/21-plus",
    "https://ipko.tv/tv-guide/21-popullore",
    "https://ipko.tv/tv-guide/zico-tv",
    "https://ipko.tv/tv-guide/ntv",
    "https://ipko.tv/tv-guide/club-tv",
    "https://ipko.tv/tv-guide/elrodi",
    "https://ipko.tv/tv-guide/folk-+",
    "https://ipko.tv/tv-guide/click-tv",
    "https://ipko.tv/tv-guide/bbf",
    "https://ipko.tv/tv-guide/positive-gold",
    "https://ipko.tv/tv-guide/suite",
    "https://ipko.tv/tv-guide/travelingo",
    "https://ipko.tv/tv-guide/my-music",
    "https://ipko.tv/tv-guide/klan-music",
    "https://ipko.tv/tv-guide/rtk-3",
    "https://ipko.tv/tv-guide/rtk-4",
    "https://ipko.tv/tv-guide/first-channel",
    "https://ipko.tv/tv-guide/e--tv",
    "https://ipko.tv/tv-guide/tv-llapi",
    "https://ipko.tv/tv-guide/alb-uk-tv",
    "https://ipko.tv/tv-guide/atd-tv",
    "https://ipko.tv/tv-guide/tv-arta",
    "https://ipko.tv/tv-guide/a-news",
    "https://ipko.tv/tv-guide/kanali-7",
    "https://ipko.tv/tv-guide/fax-news",
    "https://ipko.tv/tv-guide/tring-originals",
    "https://ipko.tv/tv-guide/syri-tv",
    "https://ipko.tv/tv-guide/top-news",
    "https://ipko.tv/tv-guide/klan-news",
    "https://ipko.tv/tv-guide/klan-plus",
    "https://ipko.tv/tv-guide/a2-cnn",
    "https://ipko.tv/tv-guide/euronews-albania",
    "https://ipko.tv/tv-guide/tv-syri-vision",
    "https://ipko.tv/tv-guide/tv-mitrovica",
    "https://ipko.tv/tv-guide/tv-festina",
    "https://ipko.tv/tv-guide/tv-puls",
    "https://ipko.tv/tv-guide/star-plus-tv",
    "https://ipko.tv/tv-guide/peace-tv",
    "https://ipko.tv/tv-guide/sport-1",
    "https://ipko.tv/tv-guide/sport-2",
    "https://ipko.tv/tv-guide/sport-3",
    "https://ipko.tv/tv-guide/sport-4",
    "https://ipko.tv/tv-guide/sport-5",
    "https://ipko.tv/tv-guide/sport-6",
    "https://ipko.tv/tv-guide/k-sport-1",
    "https://ipko.tv/tv-guide/k-sport-2",
    "https://ipko.tv/tv-guide/k-sport-3",
    "https://ipko.tv/tv-guide/k-sport-4",
    "https://ipko.tv/tv-guide/kb-peja",
    "https://ipko.tv/tv-guide/trt-spor",
    "https://ipko.tv/tv-guide/a-spor",
    "https://ipko.tv/tv-guide/supersport-1",
    "https://ipko.tv/tv-guide/supersport-2",
    "https://ipko.tv/tv-guide/supersport-3",
    "https://ipko.tv/tv-guide/supersport-4",
    "https://ipko.tv/tv-guide/supersport-5",
    "https://ipko.tv/tv-guide/supersport-6",
    "https://ipko.tv/tv-guide/supersport-7",
    # "https://ipko.tv/tv-guide/france-24",
]

channels = [url.split("/")[-1] for url in urls]

def day_range(offset_days=0):
    day = datetime.now() + timedelta(days=offset_days)
    start = datetime(day.year, day.month, day.day, 0, 0, 0)
    end = start + timedelta(days=1) - timedelta(seconds=1)
    return int(start.timestamp()), int(end.timestamp())

def unix_to_minutes(ts):
    dt = datetime.fromtimestamp(ts, tz=timezone.utc)
    return dt.hour * 60 + dt.minute

def generate_time_preferences(epg_data, max_preferences=20, block_size=60):
    """Generate time preferences from genres and time blocks."""
    from collections import defaultdict
    time_genre_map = defaultdict(int)

    for channel, ch_data in epg_data.items():
        for show in ch_data.get("shows", []):
            genres = show.get("genres") or []
            genre = (genres[0].lower().strip() if genres and genres[0] else "other")
            start_min = unix_to_minutes(show.get("show_start"))
            block_start = (start_min // block_size) * block_size
            time_genre_map[(block_start, genre)] += 1


    prefs = []
    for (block_start, genre), count in sorted(time_genre_map.items()):
        prefs.append({
            "start": block_start,
            "end": block_start + block_size,
            "preferred_genre": genre,
            "bonus": min(100, 20 + count * 10 + random.randint(0, 10))
        })


    prefs = sorted(prefs, key=lambda x: x["bonus"], reverse=True)[:max_preferences]
    prefs.sort(key=lambda x: x["start"])
    return prefs
def generate_priority_blocks(epg_data, block_size=60, top_n=3):

    from collections import defaultdict
    
    block_channel_map = defaultdict(list)
    
    for i, (channel, ch_data) in enumerate(epg_data.items()):
        for show in ch_data.get("shows", []):
            start_min = unix_to_minutes(show["show_start"])
            block_start = (start_min // block_size) * block_size
            block_channel_map[block_start].append(i)
    
    blocks = [(start, start + block_size, channels) for start, channels in block_channel_map.items()]
    
    blocks.sort(key=lambda x: len(x[2]), reverse=True)
    
    priority_blocks = []
    for start, end, channels in blocks[:top_n]:
        priority_blocks.append({
            "start": start,
            "end": end,
            "allowed_channels": channels
        })
    
    return priority_blocks


def epg_to_smart_json(epg_data):
    all_starts, all_ends = [], []
    used_ids = set()  

 
    for ch_data in epg_data.values():
        for show in ch_data.get("shows", []):
            start_time = show.get("show_start")
            end_time = show.get("show_end")

            if start_time and end_time:
                start_min = unix_to_minutes(start_time)
                end_min = unix_to_minutes(end_time)


                if end_min < start_min:
                    end_min += 1440  

                all_starts.append(start_min)
                all_ends.append(end_min)

    
    opening_time = min(all_starts) if all_starts else 480
    closing_time = max(all_ends) if all_ends else 1380  


    smart_json = {
        "opening_time": opening_time,
        "closing_time": closing_time,
        "min_duration": 30,
        "max_consecutive_genre": 2,
        "channels_count": len(epg_data),
        "switch_penalty": 5,
        "termination_penalty": 10,
        "time_preferences": generate_time_preferences(epg_data),
        "priority_blocks": generate_priority_blocks(epg_data),
        "channels": []
    }


    for i, (channel, ch_data) in enumerate(epg_data.items()):
        programs = []
        for pid, show in enumerate(ch_data.get("shows", []), start=1):
            start_time = unix_to_minutes(show["show_start"])
            end_time = unix_to_minutes(show["show_end"])

            
            if end_time < start_time:
                end_time += 1440  

            genres = show.get("genres") or []
            genre = (genres[0].lower().strip() if genres and genres[0] else "other")

            program_name = show.get("show_name") or show.get("title") or "Unknown Program"
            
          
            program_id = program_name
            if program_id in used_ids:
                program_id = f"{program_name}_{pid}"  
            used_ids.add(program_id) 

            programs.append({
                "program_id": program_id,  
                "start": start_time,
                "end": end_time,
                "genre": genre,  
                "score": random.randint(50, 90)
            })

        smart_json["channels"].append({
            "channel_id": i,
            "programs": programs
        })

    return smart_json

    all_starts, all_ends = [], []

    for ch_data in epg_data.values():
        for show in ch_data.get("shows", []):
            
            start_time = show.get("show_start")
            end_time = show.get("show_end")

            
            if start_time and end_time:
                start_min = unix_to_minutes(start_time)
                end_min = unix_to_minutes(end_time)

               
                if end_min < start_min:
                    end_min += 1440  

                
                all_starts.append(start_min)
                all_ends.append(end_min)

    
    opening_time = min(all_starts) if all_starts else 480  
    closing_time = max(all_ends) if all_ends else 1380    

    
    smart_json = {
        "opening_time": opening_time,
        "closing_time": closing_time,
        "min_duration": 30,
        "max_consecutive_genre": 2,
        "channels_count": len(epg_data),
        "switch_penalty": 5,
        "termination_penalty": 10,
        "time_preferences": generate_time_preferences(epg_data),
        "priority_blocks": generate_priority_blocks(epg_data),
        "channels": []
    }

    
    for i, (channel, ch_data) in enumerate(epg_data.items()):
        programs = []
        for pid, show in enumerate(ch_data.get("shows", []), start=1):
            start_time = unix_to_minutes(show["show_start"])
            end_time = unix_to_minutes(show["show_end"])

            
            if end_time < start_time:
                end_time += 1440  

            genres = show.get("genres") or []
            genre = (genres[0].lower().strip() if genres and genres[0] else "other")

            
            program_name = show.get("show_name") or show.get("title") or "Unknown Program"

            programs.append({
                "program_id": f"{channel}_{pid}",
                "start": start_time,
                "end": end_time,
                "genre": genre,  
                "score": random.randint(50, 90)
            })

        smart_json["channels"].append({
            "channel_id": i,
            "programs": programs
        })

    return smart_json

    all_starts, all_ends = [], []

    for ch_data in epg_data.values():
        for show in ch_data.get("shows", []):
            
            start_time = show.get("show_start")
            end_time = show.get("show_end")

            
            if start_time and end_time:
                start_min = unix_to_minutes(start_time)
                end_min = unix_to_minutes(end_time)

                
                if end_min < start_min:
                    end_min += 1440  

                
                all_starts.append(start_min)
                all_ends.append(end_min)

   
    opening_time = min(all_starts) if all_starts else 480 
    closing_time = max(all_ends) if all_ends else 1380    

    
    smart_json = {
        "opening_time": opening_time,
        "closing_time": closing_time,
        "min_duration": 30,
        "max_consecutive_genre": 2,
        "channels_count": len(epg_data),
        "switch_penalty": 5,
        "termination_penalty": 10,
        "time_preferences": generate_time_preferences(epg_data),
        "priority_blocks": generate_priority_blocks(epg_data),
        "channels": []
    }

    
    for i, (channel, ch_data) in enumerate(epg_data.items()):
        programs = []
        for pid, show in enumerate(ch_data.get("shows", []), start=1):
            start_time = unix_to_minutes(show["show_start"])
            end_time = unix_to_minutes(show["show_end"])

           
            if end_time < start_time:
                end_time += 1440  

            genres = show.get("genres") or []
            genre = (genres[0].lower().strip() if genres and genres[0] else "other")
            programs.append({
                "program_id": f"{channel}_{pid}",
                "start": start_time,
                "end": end_time,
                "genre": genre,
                "score": random.randint(50, 90)
            })

        smart_json["channels"].append({
            "channel_id": i,
            "programs": programs
        })

    return smart_json

    all_starts, all_ends = [], []

    for ch_data in epg_data.values():
        for show in ch_data.get("shows", []):
            
            start_time = show.get("show_start")
            end_time = show.get("show_end")

            
            if start_time and end_time and start_time < end_time:
                start_min = unix_to_minutes(start_time)
                end_min = unix_to_minutes(end_time)

                all_starts.append(start_min)
                all_ends.append(end_min)

    
    opening_time = min(all_starts) if all_starts else 480  
    closing_time = max(all_ends) if all_ends else 1380    

    
    smart_json = {
        "opening_time": opening_time,
        "closing_time": closing_time,
        "min_duration": 30,
        "max_consecutive_genre": 2,
        "channels_count": len(epg_data),
        "switch_penalty": 5,
        "termination_penalty": 10,
        "time_preferences": generate_time_preferences(epg_data),
        "priority_blocks": generate_priority_blocks(epg_data),
        "channels": []
    }

    
    for i, (channel, ch_data) in enumerate(epg_data.items()):
        programs = []
        for pid, show in enumerate(ch_data.get("shows", []), start=1):
            start_time = unix_to_minutes(show["show_start"])
            end_time = unix_to_minutes(show["show_end"])
            genres = show.get("genres") or []
            genre = (genres[0].lower().strip() if genres and genres[0] else "other")
            programs.append({
                "program_id": f"{channel}_{pid}",
                "start": start_time,
                "end": end_time,
                "genre": genre,
                "score": random.randint(50, 90)
            })

        smart_json["channels"].append({
            "channel_id": i,
            "programs": programs
        })

    return smart_json

    all_starts, all_ends = [], []
    for ch_data in epg_data.values():
        for show in ch_data.get("shows", []):
            s = unix_to_minutes(show["show_start"])
            e = unix_to_minutes(show["show_end"])
            all_starts.append(s)
            all_ends.append(e)

    opening_time = min(all_starts) if all_starts else 480
    closing_time = max(all_ends) if all_ends else 1380

    smart_json = {
        "opening_time": opening_time,
        "closing_time": closing_time,
        "min_duration": 30,
        "max_consecutive_genre": 2,
        "channels_count": len(epg_data),
        "switch_penalty": 5,
        "termination_penalty": 10,
        "time_preferences": generate_time_preferences(epg_data),
        "priority_blocks": generate_priority_blocks(epg_data),  

        "channels": []
    }

    for i, (channel, ch_data) in enumerate(epg_data.items()):
        programs = []
        for pid, show in enumerate(ch_data.get("shows", []), start=1):
            start = unix_to_minutes(show["show_start"])
            end = unix_to_minutes(show["show_end"])
            genres = show.get("genres") or []
            genre = (genres[0].lower().strip() if genres and genres[0] else "other")
            programs.append({
                "program_id": f"{channel}_{pid}",
                "start": start,
                "end": end,
                "genre": genre,
                "score": random.randint(50, 90)
            })

        smart_json["channels"].append({
            "channel_id": i,
            "programs": programs
        })

    return smart_json

choiceFrom = int(input("\nSa ditë më parë nga sot dëshironi të merrni të dhëna? "))
choiceTo = int(input("\nSa ditë nga sot dëshironi të merrni të dhëna? "))

for day_offset in range(-choiceFrom, choiceTo):  
    from_ts, to_ts = day_range(day_offset)
    date_str = (datetime.now() + timedelta(days=day_offset)).strftime("%Y-%m-%d")
    print(f"\n Fetching schedule for {date_str} ({from_ts} → {to_ts})")
    
    day_data = {}

    for ch_id in channels:
        payload = {
            "ch_ext_id": ch_id,
            "from": from_ts,
            "to": to_ts
        }

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            response.raise_for_status()
            day_data[ch_id] = response.json()
            print(f"{ch_id} fetched")
        except requests.HTTPError as e:
            print(f" HTTP error for {ch_id}: {e}")
        except Exception as e:
            print(f"Error fetching {ch_id}: {e}")

  
        epg_data = day_data
        smart_json = epg_to_smart_json(epg_data)

    output_file = f"ipko_schedule_{date_str}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(smart_json, f, indent=2, ensure_ascii=False)


