#!/usr/bin/env python3
"""
TOEFL-style training example generator v3.
Stochastic sampling: each call draws randomly from subject × scenario × error type,
so repeated runs produce distinct output without full cartesian expansion.

Usage:
  python3 gen_toefl_v3.py [--target 10000] [--seed SEED] [--out path.jsonl] [--existing superset.jsonl]
"""

import json, random, argparse, os, hashlib, sys
from pathlib import Path

# ─── CLI ──────────────────────────────────────────────────────────────────────
p = argparse.ArgumentParser()
p.add_argument("--target", type=int, default=10000)
p.add_argument("--seed", type=int, default=None)
p.add_argument("--out", default=None)
p.add_argument("--existing", nargs="*", default=[])
args = p.parse_args()

rng = random.Random(args.seed)  # seeded only if --seed provided; else random each run

# ─── Load existing to avoid duplicates ───────────────────────────────────────
existing_hashes = set()
for path in args.existing:
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line: continue
                try:
                    obj = json.loads(line)
                    h = hashlib.md5(obj["messages"][0]["content"].lower().strip().encode()).hexdigest()
                    existing_hashes.add(h)
                except: pass
        print(f"Loaded {len(existing_hashes)} existing hashes from {path}", flush=True)

# ─── Subjects ─────────────────────────────────────────────────────────────────
SUBJ3SG = [
    "My friend", "My sister", "My brother", "My cousin", "My neighbor",
    "My colleague", "My classmate", "My roommate", "My manager", "My professor",
    "My doctor", "My coworker", "My advisor", "My tutor", "My partner",
    "My girlfriend", "My boyfriend", "My wife", "My husband", "My mother",
    "My father", "My aunt", "My uncle", "My daughter", "My son",
    "Her friend", "His friend", "Her sister", "His brother", "Her teacher",
    "His doctor", "Her professor", "His colleague", "Her classmate", "His roommate",
    "The teacher", "The student", "The professor", "The doctor", "The engineer",
    "The manager", "The scientist", "The journalist", "The chef", "The driver",
    "The nurse", "The lawyer", "The accountant", "The artist", "The coach",
    "She", "He",
]
SUBJ1ST = [
    "I", "We", "My friend and I", "My sister and I", "My colleague and I",
    "My partner and I", "My roommate and I", "My classmate and I",
    "My brother and I", "My mother and I",
]
SUBJ3PL = [
    "They", "My friends", "My colleagues", "The students", "The workers",
    "My brothers", "My neighbors", "The children", "My coworkers", "The researchers",
    "My parents", "My cousins", "The customers", "The guests", "My classmates",
]

# ─── Everyday social scenarios ────────────────────────────────────────────────
# Each scenario: (description, activities, times, follow_ups)

SCENARIOS = {

    "grocery_shopping": {
        "activities": [
            "buy milk and bread", "forget her shopping list", "pick up vegetables",
            "spend too much at the supermarket", "find everything on sale",
            "try a new recipe ingredient", "check the expiration dates",
            "argue about which brand to buy", "forget to bring the reusable bags",
            "get in the wrong checkout line", "use a coupon wrong",
            "run into an old friend", "grab snacks for the weekend",
            "look for a specific spice", "buy too many impulse items",
        ],
        "times": [
            "yesterday", "last Saturday", "this morning", "last weekend",
            "every week", "on Sunday", "earlier today", "last night",
        ],
        "follow": [
            "Did she find everything?", "Was the store busy?", "How long did it take?",
            "Did she stick to her budget?", "What was she making?",
            "Is she a regular there?", "Did she go alone?",
        ],
    },

    "public_transport": {
        "activities": [
            "miss the bus", "take the wrong train", "forget her metro card",
            "stand for the entire ride", "fall asleep and miss her stop",
            "get on the subway in the wrong direction", "wait for ages at the platform",
            "run to catch the last train", "give up her seat to an elderly person",
            "get stuck in a delay", "argue with the ticket machine",
            "travel without a valid ticket", "get lost at the station",
            "ask someone for directions", "sprint through the turnstile",
        ],
        "times": [
            "this morning", "yesterday", "last Monday", "on the way home",
            "last Tuesday", "during rush hour", "on her way to work",
        ],
        "follow": [
            "Was she late?", "Does that happen often?", "How far is the commute?",
            "Did she get there in time?", "Is the service reliable?",
            "How long did she wait?", "Does she drive instead now?",
        ],
    },

    "dating_relationships": {
        "activities": [
            "go on a first date", "text her ex by mistake", "cancel a date last minute",
            "forget their anniversary", "plan a surprise dinner",
            "meet someone at a party", "argue about something small",
            "make up after a fight", "introduce her partner to her parents",
            "break up with someone", "get back together", "feel nervous before a date",
            "spend the whole night talking", "go to the cinema together",
            "cook dinner for the first time", "send a message to the wrong person",
        ],
        "times": [
            "last Friday", "last weekend", "yesterday", "on Valentine's Day",
            "last Saturday night", "a few weeks ago", "recently", "last month",
        ],
        "follow": [
            "How did it go?", "Was she nervous?", "Are they still together?",
            "What happened next?", "Did he find out?", "Is she happy?",
            "Did they make up?", "Was it awkward?",
        ],
    },

    "family_gatherings": {
        "activities": [
            "visit her parents for the weekend", "help cook the holiday meal",
            "argue with her relatives about politics", "take too many photos",
            "eat too much and regret it", "play board games with the kids",
            "fall asleep on the sofa after lunch", "catch up with cousins she hadn't seen",
            "help her grandmother with the dishes", "have an awkward conversation",
            "leave earlier than expected", "forget to bring a gift",
            "arrive late to the family dinner", "get emotional seeing old photos",
            "stay up too late talking",
        ],
        "times": [
            "last Christmas", "last Thanksgiving", "last weekend", "during the holidays",
            "at the last family reunion", "last summer", "this past Sunday",
        ],
        "follow": [
            "Was it enjoyable?", "How many people were there?", "Did anything funny happen?",
            "How long did they stay?", "Is her family close?", "Does she visit often?",
            "Was there any drama?",
        ],
    },

    "sports_fitness": {
        "activities": [
            "join a gym", "go for a run in the park", "try yoga for the first time",
            "injure her knee during training", "sign up for a marathon",
            "skip the gym for a whole week", "beat her personal record",
            "play football with friends", "take a swimming class",
            "forget her gym bag at home", "train for a triathlon",
            "start cycling to work", "try a new fitness class", "overdo it and feel sore",
            "finally do a pull-up", "go hiking in the mountains",
        ],
        "times": [
            "this morning", "last weekend", "every day", "twice a week",
            "last month", "recently", "since January", "for three months",
        ],
        "follow": [
            "How is it going?", "Is she enjoying it?", "Did she stick with it?",
            "What's her goal?", "Is she training alone?", "How did it feel?",
            "Has she seen improvement?",
        ],
    },

    "social_media_tech": {
        "activities": [
            "post the wrong photo by accident", "get too many notifications",
            "spend hours scrolling before bed", "accidentally go live on Instagram",
            "forget her password again", "delete the wrong message",
            "share something she regretted", "get a lot of likes on a post",
            "start a new account", "unfollow someone after an argument",
            "post a story meant for close friends to everyone",
            "reply to the wrong thread", "lose her phone at the worst time",
            "try to fix her wifi for an hour", "update her profile photo",
        ],
        "times": [
            "last night", "yesterday", "this morning", "last week",
            "over the weekend", "a few days ago", "earlier today",
        ],
        "follow": [
            "Was it embarrassing?", "Did anyone notice?", "Did she fix it?",
            "How did people react?", "Has she done that before?",
            "What was she trying to do?", "Did she delete it in time?",
        ],
    },

    "eating_out": {
        "activities": [
            "try a new restaurant", "wait an hour for a table",
            "order the wrong dish by mistake", "forget her wallet",
            "split the bill awkwardly", "leave a bad review online",
            "get food poisoning", "eat somewhere way too expensive",
            "find a new favorite café", "go to a food festival",
            "try food from a country she'd never tasted before",
            "complain about slow service", "order too much food",
            "take too many photos of the food", "go out for brunch",
        ],
        "times": [
            "last weekend", "yesterday", "last Friday night", "on her birthday",
            "last month", "recently", "a few days ago",
        ],
        "follow": [
            "Was it good?", "Would she go back?", "How was the food?",
            "Who did she go with?", "Was it expensive?", "Did she enjoy it?",
            "What did she order?",
        ],
    },

    "work_casual": {
        "activities": [
            "arrive late because of traffic", "forget a meeting completely",
            "send an email to the wrong person", "spill coffee on her keyboard",
            "fall asleep in a long meeting", "get stuck on a call for two hours",
            "miss a deadline by five minutes", "mess up a presentation",
            "accidentally unmute herself during a video call",
            "lose an important file", "work through lunch again",
            "make a mistake in a spreadsheet", "say something awkward to her boss",
            "forget her password on her first day back", "borrow a charger and forget to return it",
        ],
        "times": [
            "this morning", "yesterday", "last week", "on Monday",
            "earlier today", "last Tuesday", "a few days ago",
        ],
        "follow": [
            "Was it a big deal?", "Did anyone notice?", "How did her boss react?",
            "Did she sort it out?", "Does that happen often?",
            "Is she usually organized?", "What happened next?",
        ],
    },

    "home_life": {
        "activities": [
            "burn dinner", "lock herself out of the apartment",
            "lose her keys for an hour", "forget to pay rent on time",
            "try to fix a leak and make it worse", "spend all day cleaning",
            "finally organize her wardrobe", "buy furniture and not be able to assemble it",
            "forget to take out the trash", "get a package delivered to the wrong address",
            "stay up all night decorating", "accidentally set off the smoke alarm",
            "water her plants and realize they were fake", "bake something that came out wrong",
            "sleep through her alarm by three hours",
        ],
        "times": [
            "last night", "yesterday", "this morning", "last weekend",
            "over the weekend", "a few days ago", "earlier today",
        ],
        "follow": [
            "How did she handle it?", "Was anyone else home?", "Is everything okay?",
            "Did she call anyone for help?", "Has that happened before?",
            "What did she do next?", "Was it a big mess?",
        ],
    },

    "travel_leisure": {
        "activities": [
            "miss her flight", "lose her passport at the airport",
            "book the wrong hotel", "arrive in the wrong city",
            "get stuck at customs for ages", "forget to buy travel insurance",
            "pack way too much luggage", "run out of local currency",
            "take the scenic route and get completely lost",
            "meet interesting people on the train",
            "try to speak the local language and fail spectacularly",
            "leave her phone on the plane", "find an amazing hidden restaurant",
            "get a terrible sunburn on day one",
            "stay out all night and miss the morning tour",
        ],
        "times": [
            "last summer", "during her vacation", "last month", "recently",
            "when she traveled to {country}", "last spring", "on her trip",
        ],
        "follow": [
            "Did she make it in time?", "How did she sort it out?", "Was she stressed?",
            "What happened next?", "Where was she going?", "Did she manage?",
            "Was it a good trip overall?",
        ],
    },

    "studying": {
        "activities": [
            "pull an all-nighter before the exam", "forget everything she studied",
            "study the wrong chapter entirely", "lose her notes the day before the test",
            "fall asleep at the library", "procrastinate for a whole week",
            "finally understand a concept she'd struggled with",
            "submit the assignment five minutes late", "get a better grade than expected",
            "ask a classmate to explain something", "redo her notes from scratch",
            "turn up to the wrong exam room", "start studying two days before the deadline",
            "join a study group that turned into a chat session",
            "read the textbook on public transport",
        ],
        "times": [
            "last semester", "before the exam", "this week", "last night",
            "during finals", "recently", "at the weekend",
        ],
        "follow": [
            "How did it go?", "Did she pass?", "Was she prepared?",
            "What subject was it?", "Is she still stressed?",
            "How did she feel after?", "Would she do anything differently?",
        ],
    },

    "health_medical": {
        "activities": [
            "cancel a doctor's appointment last minute", "forget to take her medication",
            "try to self-diagnose on the internet", "wait too long to see a doctor",
            "get the flu right before an important event",
            "sprain her ankle at the worst time", "finally get a check-up",
            "follow a new diet for exactly three days", "stay up late despite being ill",
            "ask a friend for medical advice instead of a doctor",
            "lose her health insurance card", "wait two hours in the waiting room",
            "take the wrong dose of medicine", "recover faster than expected",
            "google her symptoms and assume the worst",
        ],
        "times": [
            "last week", "recently", "last month", "a few days ago",
            "over the weekend", "earlier this week", "last winter",
        ],
        "follow": [
            "Is she feeling better?", "Did she eventually go?", "How is she now?",
            "Did it affect her plans?", "Was it serious?",
            "Has she sorted it out?", "Is she taking better care of herself?",
        ],
    },

    "friends_socializing": {
        "activities": [
            "host a party that got out of hand", "forget a friend's birthday",
            "cancel plans at the last minute", "reconnect with an old friend",
            "have a falling out over something small", "laugh so hard at the pub",
            "stay out much later than planned", "organize a surprise party",
            "show up to the wrong address", "give terrible advice",
            "accidentally start a group chat argument", "catch up over coffee",
            "help a friend move to a new flat", "karaoke until 2am",
            "become friends with someone she thought she'd never like",
        ],
        "times": [
            "last Saturday", "recently", "last weekend", "over the holidays",
            "last week", "a while ago", "a few months ago",
        ],
        "follow": [
            "How did that go?", "Are they still friends?", "Was it a good time?",
            "Did she apologize?", "How did everyone react?",
            "Would she do it again?", "Who else was there?",
        ],
    },

    "weather_seasons": {
        "activities": [
            "get caught in the rain without an umbrella",
            "slip on ice on the way to work", "go to the beach on a cloudy day",
            "miss a barbecue because of bad weather",
            "wear the wrong outfit for the temperature",
            "get sunburned in October somehow",
            "complain about the heat for the hundredth time",
            "get her car stuck in the snow",
            "refuse to wear a coat and regret it",
            "cancel outdoor plans because of the forecast",
            "enjoy the first sunny day of the year",
            "misjudge how cold it would be at night",
            "get her umbrella turned inside out by the wind",
        ],
        "times": [
            "yesterday", "last week", "this morning", "last winter",
            "during the summer", "recently", "last Tuesday",
        ],
        "follow": [
            "Was she prepared?", "Did she manage?", "Was it bad?",
            "What did she do?", "Has she learned her lesson?",
            "Does that happen often?", "Is she okay?",
        ],
    },

    "money_finances": {
        "activities": [
            "forget to check her bank balance before spending",
            "buy something she immediately regretted",
            "lend money to a friend and regret it",
            "find a great deal and buy too many",
            "forget about a subscription she was paying for",
            "try to budget for the first time", "overdraft her account",
            "get a surprise refund", "discover she was charged twice",
            "splurge on something unnecessary", "sell something online",
            "negotiate a better deal", "panic about an unexpected bill",
            "save up for something for months", "treat herself after a tough week",
        ],
        "times": [
            "last week", "this month", "recently", "yesterday",
            "last payday", "a few days ago", "last year",
        ],
        "follow": [
            "Was it worth it?", "Did she sort it out?", "How much did she spend?",
            "Is she more careful now?", "Did she get a refund?",
            "How did she feel about it?", "Has she fixed it?",
        ],
    },
}

COUNTRIES = [
    "Japan", "France", "Germany", "Spain", "Italy", "Brazil", "Australia",
    "Canada", "Mexico", "South Korea", "India", "Portugal", "Argentina",
    "the Netherlands", "Sweden", "Norway", "Thailand", "Vietnam", "Egypt",
]

# ─── Error patterns ───────────────────────────────────────────────────────────
# Each returns a function (subj, activity, time, follow) -> (sentence, reply) | None

def subj3sg_form(subj):
    """Conjugate verb for 3rd singular subject."""
    return subj not in SUBJ1ST and subj not in SUBJ3PL

def err_missing_past_ed(subj, activity, time, follow):
    """She finish the report yesterday. (base form, no -ed)"""
    # activity is already a phrase; treat first word as verb
    words = activity.split()
    verbs_to_keep_bare = {"go","come","run","get","make","take","buy","find","give",
                           "know","see","say","tell","leave","bring","write","read","win",
                           "lose","meet","send","spend","build","feel","break","eat","sleep"}
    if not words: return None
    v = words[0]
    if v in verbs_to_keep_bare: return None  # these need irregular forms — skip
    sentence = f"{subj} {activity} {time}."
    return (sentence, rng.choice(follow))

def err_have_wrong_past(subj, activity, time, follow):
    """She have finished. / I have went."""
    wrong_forms = {
        "go": "went", "come": "came", "take": "took", "see": "saw",
        "eat": "ate", "run": "ran", "buy": "buyed", "make": "maked",
        "find": "finded", "get": "getted", "give": "gived",
    }
    words = activity.split()
    v = words[0]
    wrong = wrong_forms.get(v)
    if not wrong: return None
    rest = " ".join(words[1:])
    if subj3sg_form(subj):
        sentence = f"{subj} have {wrong} {rest} {time}.".strip()
    else:
        sentence = f"{subj} has {wrong} {rest} {time}.".strip()
    return (sentence, rng.choice(follow))

def err_sv_3sg(subj, activity, time, follow):
    """My friend go to the gym every day. (3sg missing -s)"""
    if subj not in SUBJ3SG: return None
    words = activity.split()
    v = words[0]
    # Only works if first word is a base form verb
    if v not in {"go","live","work","study","play","run","travel","eat","drink","read",
                  "watch","cook","use","take","make","give","tell","ask","learn",
                  "help","show","feel","seem","keep","move","like","want","need","love"}:
        return None
    sentence = f"{subj} {activity} {time}."
    return (sentence, rng.choice(follow))

def err_wrong_preposition(subj, activity, time, follow):
    """She arrived in the airport. She is good in programming."""
    # Use fixed preposition-error phrases rather than string replacement (too unpredictable)
    prep_errors = [
        "arrived in the airport", "is good in organizing things",
        "is interested on the topic", "is different of her colleague",
        "depends of others for support", "complained of the situation",
        "talked to about the problem", "is satisfied of the result",
        "is married with a colleague", "is responsible of the whole project",
        "graduated of the program", "specializes on that subject",
        "applied of the scholarship", "listened of the advice",
        "agreed to the new terms",
    ]
    phrase = rng.choice(prep_errors)
    sentence = f"{subj} {phrase} {time}."
    return (sentence, rng.choice(follow))

def err_missing_article(subj, activity, time, follow):
    """She got promotion yesterday. She lost wallet."""
    article_nouns = ["a job", "a promotion", "an appointment", "a table",
                     "a ticket", "a refund", "a bill", "a receipt", "the keys",
                     "the wallet", "the phone", "the bag", "an umbrella"]
    for phrase in article_nouns:
        if phrase in activity:
            bare = phrase.split(" ", 1)[1]  # strip article
            sentence = f"{subj} {activity.replace(phrase, bare)} {time}."
            return (sentence, rng.choice(follow))
    return None

def err_adj_as_adv(subj, activity, time, follow):
    """She explained things very clear. He responded very quick."""
    adv_subs = [
        (" clearly", " clear"), (" quickly", " quick"), (" slowly", " slow"),
        (" carefully", " careful"), (" perfectly", " perfect"), (" easily", " easy"),
        (" loudly", " loud"), (" quietly", " quiet"), (" patiently", " patient"),
        (" fluently", " fluent"),
    ]
    sent = f"{subj} {activity} {time}."
    for correct_adv, wrong_adj in adv_subs:
        if correct_adv in sent:
            return (sent.replace(correct_adv, wrong_adj), rng.choice(follow))
    return None

def err_double_negative(subj, activity, time, follow):
    """I don't know nothing about it."""
    short_objects = [
        "it", "the situation", "the problem", "the issue", "what happened",
        "the delay", "the decision", "the mistake", "the result", "the plan",
    ]
    obj = rng.choice(short_objects)
    templates = [
        f"{subj} didn't do nothing about {obj} {time}.",
        f"{subj} doesn't have no problem with {obj}.",
        f"I haven't told nobody about {obj}.",
        f"{subj} barely never asks about {obj}.",
        f"{subj} can't do nothing about {obj} {time}.",
        f"{subj} doesn't know nothing about {obj}.",
        f"I didn't say nothing about {obj} {time}.",
    ]
    return (rng.choice(templates), rng.choice(follow))

def err_pronoun_case(subj, activity, time, follow):
    """Me and her went. She told he to wait."""
    templates = [
        f"Me and my friend tried to {activity} {time}.",
        f"Her and I both {activity} {time}.",
        f"Him and his sister {activity} {time}.",
        f"They asked my friend and I to {activity}.",
        f"She invited my colleague and I to {activity} {time}.",
    ]
    return (rng.choice(templates), rng.choice(follow))

def err_was_were(subj, activity, time, follow):
    """They was there. My friends was excited."""
    if subj in SUBJ3PL or subj in ["They", "My friends", "My colleagues", "The students"]:
        sentence = f"{subj} was {activity} {time}."
        return (sentence, rng.choice(follow))
    if subj in SUBJ3SG:
        sentence = f"{subj} were {activity} {time}."
        return (sentence, rng.choice(follow))
    return None

def err_make_do(subj, activity, time, follow):
    """She did a mistake. He made his homework."""
    wrong_phrases = [
        "did a mistake", "made her homework", "did a decision",
        "made a research on the topic", "made exercise",
        "did a complaint about the service", "made a favor for her colleague",
        "did an effort to improve",
        "made business with the company", "did a great progress",
        "made a question during the meeting", "did an attempt to explain",
        "made a sport every morning", "did a party for her team",
    ]
    wrong = rng.choice(wrong_phrases)
    sentence = f"{subj} {wrong} {time}."
    return (sentence, rng.choice(follow))

def err_conditional_will_in_if(subj, activity, time, follow):
    """If she will finish, we can start."""
    # Use short fixed-phrase conditionals to avoid malformed combinations
    short_acts = [
        "finish in time", "arrive early", "agree to the plan", "come to the meeting",
        "respond to the email", "be ready", "fix the problem", "pass the exam",
        "accept the offer", "show up on time",
    ]
    act = rng.choice(short_acts)
    templates = [
        f"If {subj.lower()} will {act}, everything will be fine.",
        f"If {subj.lower()} will {act}, we can proceed.",
        f"If {subj.lower()} will {act}, we can celebrate.",
        f"If {subj.lower()} will {act}, the team will be happy.",
    ]
    return (rng.choice(templates), rng.choice(follow))

def err_gerund_infinitive(subj, activity, time, follow):
    """She enjoys to cook. He avoids to speak in public."""
    gerund_verbs = ["enjoy", "avoid", "consider", "keep", "finish", "suggest",
                    "mind", "practice", "miss", "recommend"]
    intransitive_acts = [
        "cook at home", "run in the morning", "read before bed", "study on weekends",
        "exercise every day", "travel alone", "work from home", "walk to work",
        "sing in public", "speak in front of others", "write in a journal",
        "meditate every morning", "swim in the evenings", "cycle to the office",
        "bake on Sundays",
    ]
    v = rng.choice(gerund_verbs)
    act = rng.choice(intransitive_acts)
    sentence = f"{subj} {v} to {act} {time}."
    return (sentence, rng.choice(follow))

def err_modal_to(subj, activity, time, follow):
    """She must to go. He can to do it."""
    modals = ["must to", "can to", "should to", "will to", "would to", "may to"]
    m = rng.choice(modals)
    sentence = f"{subj} {m} {activity} {time}."
    return (sentence, rng.choice(follow))

def err_present_continuous_for_perfect(subj, activity, time, follow):
    """I am living here since three years."""
    dur_times = ["since three years", "since two months", "since a long time",
                 "since she arrived", "since a while", "since 2022", "since last year"]
    dur = rng.choice(dur_times)
    # Use a fixed set of clean -ing forms rather than naive string append
    ing_map = {
        "try": "trying", "go": "going", "run": "running", "work": "working",
        "live": "living", "study": "studying", "play": "playing", "make": "making",
        "take": "taking", "help": "helping", "join": "joining", "use": "using",
        "move": "moving", "learn": "learning", "train": "training", "cook": "cooking",
        "visit": "visiting", "meet": "meeting", "sign": "signing", "build": "building",
        "plan": "planning", "spend": "spending", "stay": "staying", "travel": "traveling",
        "organize": "organizing", "prepare": "preparing", "look": "looking",
        "wait": "waiting", "start": "starting", "finish": "finishing",
        "attend": "attending", "apply": "applying", "sell": "selling", "buy": "buying",
        "host": "hosting", "save": "saving", "manage": "managing",
    }
    v = activity.split()[0]
    v_ing = ing_map.get(v)
    if not v_ing:
        return None
    rest = activity.split(" ", 1)[1] if " " in activity else ""
    sentence = f"{subj} is {v_ing} {rest} {dur}.".strip()
    return (sentence, rng.choice(follow))

def err_mass_noun_pluralized(subj, activity, time, follow):
    """She gave me some informations. He needs more advices."""
    wrong_plurals = [
        ("informations", "about the situation"),
        ("advices", "from her colleague"),
        ("researches", "on the topic"),
        ("furnitures", "for the new place"),
        ("equipments", "for the job"),
        ("knowledges", "in this field"),
        ("homeworks", "before the deadline"),
        ("staffs", "at the company"),
        ("traffics", "on the way home"),
        ("weathers", "for the weekend"),
    ]
    wrong, context = rng.choice(wrong_plurals)
    verbs = ["needed", "shared", "got", "received", "provided", "gave her", "collected",
             "asked for", "found a lot of", "gathered useful"]
    v = rng.choice(verbs)
    sentence = f"{subj} {v} {wrong} {context} {time}."
    return (sentence, rng.choice(follow))

ERROR_GENERATORS = [
    err_missing_past_ed,
    err_have_wrong_past,
    err_sv_3sg,
    err_wrong_preposition,
    err_missing_article,
    err_adj_as_adv,
    err_double_negative,
    err_pronoun_case,
    err_was_were,
    err_make_do,
    err_conditional_will_in_if,
    err_gerund_infinitive,
    err_modal_to,
    err_present_continuous_for_perfect,
    err_mass_noun_pluralized,
]

# ─── Corpus of correct examples (10% of output) ──────────────────────────────
CORRECT_REPLIES = [
    "That sounds like quite an experience! How did it all turn out?",
    "Really? How did you feel afterward?",
    "That's interesting. What happened next?",
    "I can imagine! Did everything work out in the end?",
    "Oh wow. How do you feel about it now?",
    "That must have been tough. Is everything sorted?",
    "Nice! Would you do it again?",
]

def make_correct(subj, activity, time, follow):
    sentence = f"{subj} {activity} {time}."
    return (sentence, rng.choice(CORRECT_REPLIES))

# ─── Generation loop ─────────────────────────────────────────────────────────
scenario_names = list(SCENARIOS.keys())
all_subjects = SUBJ3SG + SUBJ1ST + SUBJ3PL

results = []
seen_hashes = set(existing_hashes)
max_attempts = args.target * 30
attempts = 0

while len(results) < args.target and attempts < max_attempts:
    attempts += 1

    # Sample a scenario
    sc_name = rng.choice(scenario_names)
    sc = SCENARIOS[sc_name]
    activity = rng.choice(sc["activities"])
    time_expr = rng.choice(sc["times"])
    follow = sc["follow"]

    # Substitute {country} if present
    country = rng.choice(COUNTRIES)
    time_expr = time_expr.replace("{country}", country)

    # Sample a subject
    subj = rng.choice(all_subjects)

    # Sample an error generator (90%) or correct form (10%)
    if rng.random() < 0.10:
        result = make_correct(subj, activity, time_expr, follow)
    else:
        gen = rng.choice(ERROR_GENERATORS)
        result = gen(subj, activity, time_expr, follow)

    if result is None:
        continue

    sentence, reply = result
    sentence = sentence.strip()
    if not sentence:
        continue

    h = hashlib.md5(sentence.lower().strip().encode()).hexdigest()
    if h in seen_hashes:
        continue

    seen_hashes.add(h)
    results.append({"messages": [
        {"role": "user", "content": sentence},
        {"role": "assistant", "content": reply},
    ]})

    if len(results) % 1000 == 0:
        print(f"  {len(results)} / {args.target}  (attempts: {attempts})", flush=True)

print(f"\nGenerated {len(results)} examples in {attempts} attempts", flush=True)
if len(results) < args.target:
    print(f"WARNING: hit attempt ceiling. {len(results)}/{args.target} produced.", flush=True)

# ─── Write ────────────────────────────────────────────────────────────────────
from datetime import datetime
date_str = datetime.now().strftime("%Y%m%d")
out_path = args.out or f"/home/milwrite/Quimbot/fine-tuning/data/toefl_batch_{date_str}_v3gen.jsonl"

rng.shuffle(results)
with open(out_path, "w") as f:
    for obj in results:
        f.write(json.dumps(obj) + "\n")

print(f"Wrote {len(results)} lines → {out_path}", flush=True)
