#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SHADOW TRACER – Cyberpunk Intelligence Suite
Author: SYLHETYHACKVENGER (THE-ERROR808)
SYLHETY Edition – “Every packet tells a story.”
"""

import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import sys
from colorama import Fore, Back, Style, init
from concurrent.futures import ThreadPoolExecutor, as_completed

init(autoreset=True)

# =========================
# 🔹 GLOBAL CONFIG
# =========================
VERSION = "2.0"
AUTHOR = "SYLHETYHACKVENGER (THE-ERROR808)"
TAGLINE = "“Break the matrix, one trace at a time.”"

# =========================
# 🔹 CLEAR SCREEN
# =========================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# =========================
# 🔹 LOADING ANIMATION
# =========================
def loading_animation(text, duration=1.0):
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{Fore.CYAN}[{frames[i % len(frames)]}] {text}{Fore.RESET}   ")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write("\r" + " " * (len(text) + 10) + "\r")

# =========================
# 🔹 BANNER
# =========================
def banner():
    clear()
    art = f"""
{Fore.CYAN}{Style.BRIGHT}
 _____ _   _   ___ ______ _____  _    _
/  ___| | | | / _ \|  _  \  _  || |  | |
\ `--.| |_| |/ /_\ \ | | | | | || |  | |
 `--. \  _  ||  _  | | | | | | || |/\| |
/\__/ / | | || | | | |/ /\ \_/ /\  /\  /
\____/\_| |_/\_| |_/___/  \___/  \/  \/


 ___________  ___  _____  _____
|_   _| ___ \/ _ \/  __ \|  ___|
  | | | |_/ / /_\ \ /  \/| |__
  | | |    /|  _  | |    |  __|
  | | | |\ \| | | | \__/\| |___
  \_/ \_| \_\_| |_/\____/\____/
{Fore.RESET}
"""
    print(art)
    print(Fore.MAGENTA + Style.BRIGHT + "╔══════════════════════════════════════════════════════════════════╗")
    print(Fore.MAGENTA + "║" + Fore.CYAN + "   SHADOW TRACE v2.0" + VERSION + " – Neural Reconnaissance Engine       " + Fore.MAGENTA + "║")
    print(Fore.MAGENTA + "║" + Fore.YELLOW + f"   Author: {AUTHOR:<44}" + Fore.MAGENTA + "║")
    print(Fore.MAGENTA + "║" + Fore.GREEN + f"   {TAGLINE:<50}" + Fore.MAGENTA + "║")
    print(Fore.MAGENTA + "╚══════════════════════════════════════════════════════════════════╝" + Fore.RESET)
    print()

# =========================
# 🔹 DECORATOR FOR BANNER
# =========================
def with_banner(func):
    def wrapper(*args, **kwargs):
        banner()
        func(*args, **kwargs)
    return wrapper

# =========================
# 🔹 UTILITY: PRINT BOXED INFO
# =========================
def print_boxed_info(title, data_pairs):
    """Print a neat box with title and key-value pairs."""
    print(Fore.CYAN + "┌" + "─" * 48 + "┐")
    print(Fore.CYAN + "│" + Fore.YELLOW + Style.BRIGHT + f" {title:<46}" + Fore.CYAN + "│")
    print(Fore.CYAN + "├" + "─" * 48 + "┤")
    for key, value in data_pairs:
        val_str = str(value)
        if len(val_str) > 30:
            val_str = val_str[:27] + "..."
        print(Fore.CYAN + "│ " + Fore.WHITE + f"{key:<20}" + Fore.GREEN + f": {val_str:<24}" + Fore.CYAN + "│")
    print(Fore.CYAN + "└" + "─" * 48 + "┘")

# =========================
# 🔹 IP TRACKER
# =========================
@with_banner
def IP_Track():
    ip = input(f"{Fore.WHITE}\n Enter target IP address : {Fore.GREEN}")
    print()
    loading_animation("Querying IPwho.is database", 1.2)
    try:
        req_api = requests.get(f"http://ipwho.is/{ip}", timeout=10)
        ip_data = json.loads(req_api.text)
    except Exception as e:
        print(Fore.RED + f"[!] API error: {e}")
        input(f"\n{Fore.CYAN}[+] Press Enter to continue...")
        return

    data = [
        ("IP Address", ip),
        ("Type", ip_data.get("type", "N/A")),
        ("Country", ip_data.get("country", "N/A")),
        ("Country Code", ip_data.get("country_code", "N/A")),
        ("City", ip_data.get("city", "N/A")),
        ("Continent", ip_data.get("continent", "N/A")),
        ("Region", ip_data.get("region", "N/A")),
        ("Latitude", ip_data.get("latitude", "N/A")),
        ("Longitude", ip_data.get("longitude", "N/A")),
        ("Postal", ip_data.get("postal", "N/A")),
        ("Calling Code", ip_data.get("calling_code", "N/A")),
        ("Capital", ip_data.get("capital", "N/A")),
        ("Borders", ip_data.get("borders", "N/A")),
        ("Flag", ip_data.get("flag", {}).get("emoji", "N/A")),
        ("ASN", ip_data.get("connection", {}).get("asn", "N/A")),
        ("Organization", ip_data.get("connection", {}).get("org", "N/A")),
        ("ISP", ip_data.get("connection", {}).get("isp", "N/A")),
        ("Domain", ip_data.get("connection", {}).get("domain", "N/A")),
        ("Timezone ID", ip_data.get("timezone", {}).get("id", "N/A")),
        ("UTC Offset", ip_data.get("timezone", {}).get("utc", "N/A")),
        ("Current Time", ip_data.get("timezone", {}).get("current_time", "N/A")),
    ]
    lat = ip_data.get("latitude")
    lon = ip_data.get("longitude")
    if lat and lon:
        map_link = f"https://www.google.com/maps/@{lat},{lon},8z"
        data.append(("Maps Link", map_link))

    print_boxed_info("🔍 IP INTELLIGENCE", data)
    input(f"\n{Fore.CYAN}[+] Press Enter to continue...")

# =========================
# 🔹 SHOW MY IP
# =========================
@with_banner
def showIP():
    loading_animation("Fetching your public IP", 0.8)
    try:
        response = requests.get('https://api.ipify.org/', timeout=5)
        my_ip = response.text
    except:
        my_ip = "Unable to retrieve"
    data = [("Your Public IP", my_ip)]
    print_boxed_info("🛸 SELF IP DISCLOSURE", data)
    input(f"\n{Fore.CYAN}[+] Press Enter to continue...")

# =========================
# 🔹 PHONE NUMBER TRACKER
# =========================
@with_banner
def phoneGW():
    phone_input = input(f"\n{Fore.WHITE} Enter phone number (e.g. +6281xxxxxxxxx) : {Fore.GREEN}")
    default_region = "ID"
    try:
        parsed_number = phonenumbers.parse(phone_input, default_region)
    except:
        print(Fore.RED + "[!] Invalid phone number format.")
        input(f"\n{Fore.CYAN}[+] Press Enter to continue...")
        return

    region_code = phonenumbers.region_code_for_number(parsed_number)
    provider = carrier.name_for_number(parsed_number, "en") or "Unknown"
    location = geocoder.description_for_number(parsed_number, "id") or "Unknown"
    is_valid = phonenumbers.is_valid_number(parsed_number)
    is_possible = phonenumbers.is_possible_number(parsed_number)
    intl_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    mobile_format = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region, with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    tz_list = timezone.time_zones_for_number(parsed_number)
    timezone_str = ', '.join(tz_list) if tz_list else "Unknown"

    type_desc = {
        phonenumbers.PhoneNumberType.MOBILE: "Mobile",
        phonenumbers.PhoneNumberType.FIXED_LINE: "Fixed Line",
        phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed/Mobile",
        phonenumbers.PhoneNumberType.TOLL_FREE: "Toll Free",
        phonenumbers.PhoneNumberType.PREMIUM_RATE: "Premium Rate",
        phonenumbers.PhoneNumberType.SHARED_COST: "Shared Cost",
        phonenumbers.PhoneNumberType.VOIP: "VoIP",
        phonenumbers.PhoneNumberType.PERSONAL_NUMBER: "Personal",
        phonenumbers.PhoneNumberType.PAGER: "Pager",
        phonenumbers.PhoneNumberType.UAN: "UAN",
        phonenumbers.PhoneNumberType.VOICEMAIL: "Voicemail",
        phonenumbers.PhoneNumberType.UNKNOWN: "Unknown"
    }.get(number_type, "Unknown")

    data = [
        ("Location", location),
        ("Region Code", region_code),
        ("Timezone", timezone_str),
        ("Operator", provider),
        ("Valid Number", str(is_valid)),
        ("Possible Number", str(is_possible)),
        ("International Format", intl_format),
        ("Mobile Format", mobile_format),
        ("E.164 Format", phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)),
        ("Country Code", str(parsed_number.country_code)),
        ("National Number", str(parsed_number.national_number)),
        ("Type", type_desc)
    ]
    print_boxed_info("📱 PHONE NUMBER DECRYPT", data)
    input(f"\n{Fore.CYAN}[+] Press Enter to continue...")

# =========================
# 🔹 ENHANCED USERNAME TRACKER (Multi-threaded, curated list)
# =========================
@with_banner
def TrackLu():
    username = input(f"\n{Fore.WHITE} Enter target username : {Fore.GREEN}").strip()
    if not username:
        print(Fore.RED + "[!] Username cannot be empty.")
        input(f"\n{Fore.CYAN}[+] Press Enter to continue...")
        return

    # --- Curated platform list ---
    sites = [
        # ---- SOCIAL MEDIA (30+) ----
        {"url": "https://www.facebook.com/{}", "name": "Facebook"},
        {"url": "https://www.instagram.com/{}", "name": "Instagram"},
        {"url": "https://www.twitter.com/{}", "name": "Twitter/X"},
        {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
        {"url": "https://github.com/{}", "name": "GitHub"},
        {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
        {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
        {"url": "https://www.youtube.com/@{}", "name": "YouTube"},
        {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
        {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
        {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
        {"url": "https://www.behance.net/{}", "name": "Behance"},
        {"url": "https://medium.com/@{}", "name": "Medium"},
        {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
        {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
        {"url": "https://www.reddit.com/user/{}", "name": "Reddit"},
        {"url": "https://vimeo.com/{}", "name": "Vimeo"},
        {"url": "https://www.deviantart.com/{}", "name": "DeviantArt"},
        {"url": "https://www.patreon.com/{}", "name": "Patreon"},
        {"url": "https://steamcommunity.com/id/{}", "name": "Steam"},
        {"url": "https://www.roblox.com/users/{}", "name": "Roblox"},
        {"url": "https://news.ycombinator.com/user?id={}", "name": "Hacker News"},
        {"url": "https://www.goodreads.com/{}", "name": "Goodreads"},
        {"url": "https://letterboxd.com/{}", "name": "Letterboxd"},
        {"url": "https://myanimelist.net/profile/{}", "name": "MyAnimeList"},
        {"url": "https://www.last.fm/user/{}", "name": "Last.fm"},
        {"url": "https://www.mixcloud.com/{}", "name": "Mixcloud"},
        {"url": "https://www.discogs.com/user/{}", "name": "Discogs"},
        {"url": "https://www.ello.co/{}", "name": "Ello"},
        {"url": "https://www.weheartit.com/{}", "name": "We Heart It"},
        {"url": "https://www.threads.net/@{}", "name": "Threads"},

        # ---- TRADING / FINANCE (30+) ----
        {"url": "https://www.tradingview.com/u/{}", "name": "TradingView"},
        {"url": "https://www.etoro.com/people/{}", "name": "eToro"},
        {"url": "https://www.zulutrade.com/trader/{}", "name": "ZuluTrade"},
        {"url": "https://www.myfxbook.com/members/{}", "name": "Myfxbook"},
        {"url": "https://www.forexfactory.com/{}", "name": "ForexFactory"},
        {"url": "https://www.robinhood.com/people/{}", "name": "Robinhood (if enabled)"},
        {"url": "https://www.webull.com/profile/{}", "name": "Webull"},
        {"url": "https://www.fiverr.com/{}", "name": "Fiverr (freelance)"},
        {"url": "https://www.upwork.com/freelancers/~{}", "name": "Upwork"},
        {"url": "https://www.freelancer.com/u/{}", "name": "Freelancer"},
        {"url": "https://www.guru.com/freelancers/{}", "name": "Guru"},
        {"url": "https://www.peopleperhour.com/freelancer/{}", "name": "PeoplePerHour"},
        {"url": "https://www.99designs.com/profiles/{}", "name": "99designs"},
        {"url": "https://www.designcrowd.com/designer/{}", "name": "DesignCrowd"},
        {"url": "https://www.toptal.com/resume/{}", "name": "Toptal"},
        {"url": "https://contently.com/{}", "name": "Contently"},
        {"url": "https://workingnotworking.com/{}", "name": "Working Not Working"},
        {"url": "https://www.servicescape.com/freelancers/{}", "name": "ServiceScape"},
        {"url": "https://www.bark.com/en/us/profile/{}", "name": "Bark"},
        {"url": "https://www.thumbtack.com/{}", "name": "Thumbtack"},
        {"url": "https://hubstafftalent.com/freelancer/{}", "name": "Hubstaff Talent"},
        {"url": "https://www.skyword.com/author/{}", "name": "Skyword"},
        {"url": "https://www.authenticjobs.com/{}", "name": "Authentic Jobs"},

        # ---- LANGUAGE LEARNING (20+) ----
        {"url": "https://www.duolingo.com/profile/{}", "name": "Duolingo"},
        {"url": "https://www.memrise.com/user/{}", "name": "Memrise"},
        {"url": "https://www.busuu.com/{}", "name": "Busuu"},
        {"url": "https://www.italki.com/user/{}", "name": "italki"},
        {"url": "https://www.tandem.net/profile/{}", "name": "Tandem"},
        {"url": "https://www.hellotalk.com/profile/{}", "name": "HelloTalk"},
        {"url": "https://www.lingq.com/profile/{}", "name": "LingQ"},
        {"url": "https://www.clozemaster.com/users/{}", "name": "Clozemaster"},
        {"url": "https://preply.com/en/tutor/{}", "name": "Preply"},
        {"url": "https://www.verbling.com/teachers/{}", "name": "Verbling"},
        {"url": "https://www.wyzant.com/tutors/{}", "name": "Wyzant"},
        {"url": "https://www.superprof.com/{}", "name": "Superprof"},
        {"url": "https://takelessons.com/profile/{}", "name": "TakeLessons"},
        {"url": "https://lingbe.com/profile/{}", "name": "Lingbe"},
        {"url": "https://speaky.com/profile/{}", "name": "Speaky"},
        {"url": "https://polyglotclub.com/member/{}", "name": "Polyglot Club"},
        {"url": "https://lang-8.com/{}", "name": "Lang-8"},
        {"url": "https://hinative.com/en-US/users/{}", "name": "HiNative"},
        {"url": "https://www.lingodeer.com/user/{}", "name": "Lingodeer"},
        {"url": "https://www.mangolanguages.com/profile/{}", "name": "Mango Languages"},

        # ---- CYBERSECURITY / HACKING PLATFORMS ----
        {"url": "https://www.hackerrank.com/{}", "name": "HackerRank"},
        {"url": "https://leetcode.com/{}", "name": "LeetCode"},
        {"url": "https://www.codewars.com/users/{}", "name": "CodeWars"},
        {"url": "https://tryhackme.com/p/{}", "name": "TryHackMe"},
        {"url": "https://app.hackthebox.com/profile/{}", "name": "HackTheBox"},
        {"url": "https://hackerone.com/{}", "name": "HackerOne"},
        {"url": "https://bugcrowd.com/{}", "name": "Bugcrowd"},
        {"url": "https://intigriti.com/profiles/{}", "name": "Intigriti"},
        {"url": "https://0x00sec.org/u/{}", "name": "0x00sec"},
        {"url": "https://ctftime.org/user/{}", "name": "CTFtime"},
        {"url": "https://www.openbugbounty.org/researchers/{}", "name": "Open Bug Bounty"},
        {"url": "https://yeswehack.com/hunter/{}", "name": "YesWeHack"},
        {"url": "https://cyberdefenders.org/profile/{}", "name": "CyberDefenders"},
    ]

    # Also add some blogging / news platforms (journals)
    blog_sites = [
        {"url": "https://{}.blogspot.com", "name": "Blogger"},
        {"url": "https://{}.wordpress.com", "name": "WordPress"},
        {"url": "https://substack.com/@{}", "name": "Substack"},
        {"url": "https://medium.com/@{}", "name": "Medium (already)"},  # already included
        {"url": "https://hashnode.com/@{}", "name": "Hashnode"},
        {"url": "https://dev.to/{}", "name": "DEV Community"},
    ]
    sites.extend(blog_sites)

    # Remove duplicates (if any)
    seen = set()
    unique_sites = []
    for site in sites:
        key = site['url']
        if key not in seen:
            seen.add(key)
            unique_sites.append(site)
    sites = unique_sites

    total = len(sites)
    print(Fore.CYAN + f"\n[>] Scanning {total} platforms... (this may take a moment)\n")

    results = {}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    def check_site(site):
        name = site['name']
        url = site['url'].format(username)
        try:
            resp = requests.get(url, timeout=5, headers=headers, allow_redirects=False)
            status = resp.status_code
            if status in (404, 410):
                return (name, f"{Fore.RED}NOT FOUND{Fore.RESET}")
            elif status in (301, 302, 303, 307, 308):
                # Redirect often means profile exists
                return (name, f"{Fore.GREEN}FOUND{Fore.RESET} – {url}")
            elif status == 200:
                # Check for "not found" keywords in body
                text = resp.text.lower()
                not_found_phrases = [
                    "not found", "page not found", "doesn't exist",
                    "sorry, we couldn't find", "profile not found",
                    "no such user", "user not found", "couldn't find"
                ]
                found = any(phrase in text for phrase in not_found_phrases)
                if found:
                    return (name, f"{Fore.RED}NOT FOUND{Fore.RESET}")
                else:
                    return (name, f"{Fore.GREEN}FOUND{Fore.RESET} – {url}")
            else:
                return (name, f"{Fore.YELLOW}UNKNOWN ({status}){Fore.RESET}")
        except requests.exceptions.Timeout:
            return (name, f"{Fore.YELLOW}TIMEOUT{Fore.RESET}")
        except Exception:
            return (name, f"{Fore.RED}ERROR{Fore.RESET}")

    # Multi-threaded scanning
    completed = 0
    with ThreadPoolExecutor(max_workers=20) as executor:
        future_to_site = {executor.submit(check_site, site): site for site in sites}
        for future in as_completed(future_to_site):
            name, status = future.result()
            results[name] = status
            completed += 1
            # Live progress update
            sys.stdout.write(f"\r{Fore.CYAN}[>] Scanned {completed}/{total} platforms...{Fore.RESET}")
            sys.stdout.flush()
    print()  # newline after progress

    # --- Output results in a box ---
    print(Fore.CYAN + "┌" + "─" * 58 + "┐")
    print(Fore.CYAN + "│" + Fore.YELLOW + Style.BRIGHT + f" USERNAME RECON – @{username:<42}" + Fore.CYAN + "│")
    print(Fore.CYAN + "├" + "─" * 58 + "┤")
    for site, status in results.items():
        # Truncate site name if too long
        site_display = site[:18] if len(site) <= 18 else site[:15] + "..."
        print(Fore.CYAN + "│ " + Fore.WHITE + f"{site_display:<18}" + Fore.RESET + f": {status:<35}" + Fore.CYAN + "│")
    print(Fore.CYAN + "└" + "─" * 58 + "┘")
    input(f"\n{Fore.CYAN}[+] Press Enter to continue...")

# =========================
# 🔹 MENU OPTIONS
# =========================
options = [
    {'num': 1, 'text': 'IP TARGET RECON', 'func': IP_Track},
    {'num': 2, 'text': 'SELF IP DISCLOSURE', 'func': showIP},
    {'num': 3, 'text': 'PHONE NUMBER INFO DECRYPT', 'func': phoneGW},
    {'num': 4, 'text': 'USERNAME SHADOW TRACE', 'func': TrackLu},
    {'num': 0, 'text': 'TERMINATE SESSION', 'func': exit}
]

def option_text():
    text = ""
    for opt in options:
        text += f"{Fore.CYAN}[ {Fore.GREEN}{opt['num']}{Fore.CYAN} ] {Fore.WHITE}{opt['text']}\n"
    return text

# =========================
# 🔹 MAIN LOOP
# =========================
def main():
    while True:
        banner()
        print(option_text())
        try:
            choice = int(input(f"{Fore.CYAN}\n SELECT OPTION > {Fore.GREEN}"))
            if choice == 0:
                print(Fore.RED + Style.BRIGHT + "\n[>] SYSTEM SHUTDOWN – STAY IN THE SHADOWS.\n")
                sys.exit(0)
            for opt in options:
                if opt['num'] == choice:
                    opt['func']()
                    break
            else:
                print(Fore.RED + "[!] INVALID OPTION")
                time.sleep(1)
        except ValueError:
            print(Fore.RED + "[!] ENTER A NUMBER")
            time.sleep(1)
        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] INTERRUPT RECEIVED – EXITING")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] EXIT")
        sys.exit(0)
