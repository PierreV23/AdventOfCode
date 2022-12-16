from __future__ import annotations
from dataclasses import dataclass, is_dataclass
from pprint import pprint
from typing import Literal, TypedDict
from dacite.core import from_dict
import json

###
with open('data.json') as file:
    data = json.load(file)

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
### zorgt voor een wat mooier bestand


UserId = int

@dataclass
class Leaderboard:
    event: str
    owner_id: UserId
    members: dict[str, User]

@dataclass
class User:
    global_score: int
    name: str | None
    stars: int
    last_star_ts: int
    local_score: int
    id: UserId
    completion_day_level: dict[str, dict[str, Star]]
    
    def get_all_stars(self) -> list[Star]:
        return [
            star
            for day in self.completion_day_level.values()
            for star in day.values()
        ]

@dataclass
class Star:
    get_star_ts: int
    star_index: int


# exon = Leaderboard(**data)
exon = from_dict(data_class=Leaderboard, data=data)
pierre = next(
    filter(
        lambda user: user.id == 1058074,
        exon.members.values()
        )
    )

marc = next(
    filter(
        lambda user: user.id == 1030283,
        exon.members.values()
        )
    )


# pierre_stars = pierre.get_all_stars()
# local_score = pierre.local_score
# marc_stars = marc.get_all_stars()

# pierre_stars = sorted([s.get_star_ts - 1669870800 for s in pierre_stars])
# marc_stars = sorted([s.get_star_ts - 1669870800 for s in marc_stars])

# UserPoints = TypedDict('UserPoints', user = UserId, points = int)

def get_ts(member: User, day: int, star: Literal[1, 2]) -> None | int:
    a = member.completion_day_level
    if str(day) in a:
        a = member.completion_day_level[str(day)]
        if str(star) in a:
            return a[str(star)].get_star_ts

def get_finishing_order_for_star(leaderboard: Leaderboard, day: int, star: int) -> list[User]:
    return [*sorted([*
            filter(
                lambda member: isinstance(get_ts(member, day, star), int),
                leaderboard.members.values()
            )],
            key = lambda member: get_ts(member, day, star)
        )
    ]

class TimestampedLeaderboard:
    ts: int
    # leaderboard: list[UserPoints]
    leaderboard: dict[UserId, int]

    def __init__(self, ts: int, leaderboard: Leaderboard):
        self.ts = ts
        days = (ts - 1669870800) // (24 * 60 * 60)
        user_points = {int(k):0 for k in leaderboard.members}
        for day in range(1, days+1):

            
            first_star = get_finishing_order_for_star(leaderboard, day, 1)
            second_star = get_finishing_order_for_star(leaderboard, day, 2)

            for star_pos, user in enumerate(first_star):
                points = len(leaderboard.members) - star_pos
                user_points[user.id] += points
            
            for star_pos, user in enumerate(second_star):
                points = len(leaderboard.members) - star_pos
                user_points[user.id] += points
        self.leaderboard = dict(sorted(user_points.items(), key=lambda k_v: k_v[1]))
        # pprint(self.leaderboard, sort_dicts=False)
    
from datetime import datetime, timezone
UTC = timezone.utc
START_TS = 1669870800
DAY = 24*60*60
# ts_lead = TimestampedLeaderboard(int(datetime.now(tz=UTC).timestamp() + DAY), exon)


import matplotlib.pyplot as plt
def compare_points(p1, p1_name, p2, p2_name, x, lead):
    if lead == 'p1':
        leader = p1
        follower = p2
        leader_name = p1_name
        follower_name = p2_name
    elif lead == 'p2':
        leader = p2
        follower = p1
        leader_name = p2_name
        follower_name = p1_name
    else:
        raise Exception()

    delta = [m - p for m, p in zip(p1, p2)]

    fig, ax1 = plt.subplots()

    ax1.set_xlim(xmin=1, xmax=len(days)-1)
    ax1.set_xticks(x)

    # ax1.set_facecolor("#000000")

    ax2 = ax1.twinx()
    ax1.plot(x, p1, marker='o', color='g', label = p1_name)
    ax1.plot(x, p2, marker='o', color='b', label = p2_name)

    ax2.set_ylim(ymin=0, ymax=max(delta))
    ax2.plot(x, delta, marker='o', color='red', label = 'delta')

    ax1.set_xlabel('Day')
    ax1.set_ylabel('Points')
    ax2.set_ylabel(f'{p1_name} lead on {p2_name}')
    ax1.legend()
    ax2.legend()
    plt.show()

def compare_pos(p1_1, p1_2, p1_name, p2_1, p2_2, p2_name, x):
    fig, ax1 = plt.subplots()
    ax1.set_xlim(xmin=1, xmax=len(x))
    ax1.set_ylim(ymin=1, ymax=max(map(max, (p1_1, p1_2, p2_1, p2_2))))
    ax1.set_xticks(x)
    ax1.set_xlabel('Day')
    ax1.set_ylabel('Finishing Position')
    ax1.plot(x, p1_1, marker='o', color='g', label = p1_name + ' star 1')
    ax1.plot(x, p2_1, marker='o', color='b', label = p2_name + ' star 1')
    ax1.plot(x, p1_2, marker='o', color='r', label = p1_name + ' star 2')
    ax1.plot(x, p2_2, marker='o', color='orange', label = p2_name + ' star 2')
    ax1.legend()
    # ax2.legend()
    plt.show()

def compare_average_pos(p1_1, p1_2, p1_name, p2_1, p2_2, p2_name, x):
    p1 = [(a+b)/2 for a,b in zip(p1_1, p1_2)]
    p2 = [(a+b)/2 for a,b in zip(p2_1, p2_2)]
    fig, ax1 = plt.subplots()
    ax1.set_xlim(xmin=1, xmax=len(x))
    ax1.set_ylim(ymin=1, ymax=max(map(max, (p1, p2))))
    ax1.set_xticks(x)
    ax1.set_xlabel('Day')
    ax1.set_ylabel('Finishing Position')
    ax1.plot(x, p1, marker='o', color='g', label = p1_name)
    ax1.plot(x, p2, marker='o', color='b', label = p2_name)
    ax1.legend()
    # ax2.legend()
    plt.show()

DAYS = 11 + 1
days = {k:{'Marc': 0, 'Pierre': 0} for k in range(1, DAYS)}
for day in days:
    ts_lead = TimestampedLeaderboard(int(START_TS + day*DAY), exon)
    marc = ts_lead.leaderboard[1030283]
    pierre = ts_lead.leaderboard[1058074]
    days[day]['Marc'] = marc
    days[day]['Pierre'] = pierre

marc = [d['Marc'] for d in days.values()]
pierre = [d['Pierre'] for d in days.values()]

print(marc)
print(pierre)
x = [*days.keys()]

compare_points(marc, 'Marc', pierre, 'Pierre', x, 'p1')


marc_1 = []
marc_2 = []
pierre_1 = []
pierre_2 = []
for day in range(1, DAYS):
    first_star = get_finishing_order_for_star(exon, day, 1)
    second_star = get_finishing_order_for_star(exon, day, 2)
    marc_1.append(first_star.index(next(filter(lambda member: member.id == 1030283, first_star))) + 1)
    marc_2.append(second_star.index(next(filter(lambda member: member.id == 1030283, second_star))) + 1)
    pierre_1.append(first_star.index(next(filter(lambda member: member.id == 1058074, first_star))) + 1)
    pierre_2.append(second_star.index(next(filter(lambda member: member.id == 1058074, second_star))) + 1)

compare_pos(marc_1, marc_2, 'Marc', pierre_1, pierre_2, 'Pierre', x)
compare_average_pos(marc_1, marc_2, 'Marc', pierre_1, pierre_2, 'Pierre', x)

m = [(a+b)/2 for a,b in zip(marc_1, marc_2)]
p = [(a+b)/2 for a,b in zip(pierre_1, pierre_2)]

print('Marc', sum(m)/len(m))
print('Pierre', sum(p)/len(p))