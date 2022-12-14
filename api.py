import json
import os
from datetime import datetime
import sys
import requests
from dotenv import load_dotenv


def get_leaderboard(session_key, leaderboard_id):
    leaderboard = None
    try:
        with open("cached_leaderboard.json") as f:
            cached_leaderboard = json.load(f)
            updated_at_datetime = datetime.fromisoformat(
                cached_leaderboard["updated_at"]
            )
            if abs((datetime.now() - updated_at_datetime).seconds) < 15 * 60:
                leaderboard = cached_leaderboard["leaderboard"]

    except FileNotFoundError:
        pass

    if leaderboard is None:
        r = requests.get(
            f"https://adventofcode.com/2022/leaderboard/private/view/{leaderboard_id}.json",
            cookies={"session": session_key},
        )
        leaderboard = r.json()
        with open("cached_leaderboard.json", "w") as f:
            f.write(
                json.dumps(
                    {
                        "updated_at": datetime.now().replace(microsecond=0).isoformat(),
                        "leaderboard": leaderboard,
                    }
                )
            )
    return leaderboard


if __name__ == "__main__":
    load_dotenv()

    leaderboard = get_leaderboard(os.getenv("SESSION"), os.getenv("LEADERBOARD_ID"))
    members: dict = leaderboard["members"]

    day = None
    if len(sys.argv) > 1:
        day = sys.argv[1]
    else:
        day = str(datetime.now().day)

    for (id, member_data) in members.items():
        name = member_data["name"]
        if name is None:
            name = f"Anonymous user #{id}"

        day_star_data = member_data["completion_day_level"].get(day)
        if day_star_data is None:
            continue
        first_star_timestamp = day_star_data.get("1", {}).get("get_star_ts", None)
        second_star_timestamp = day_star_data.get("2", {}).get("get_star_ts", None)
        print(name)
        print(datetime.fromtimestamp(first_star_timestamp))
        if second_star_timestamp is None:
            print("Did not get second star")
        else:
            print(datetime.fromtimestamp(second_star_timestamp))
        print()