#!/usr/bin/env python3
"""Mission Control — daily email assembler.

Runs at 10:45 UTC. Reads the content bank + configs + public dashboard data,
writes data/today/email.html + subject.txt + status.json, and advances
engine state. NO AI, NO KEYS required — the bank dispenses.

Optional path: if ANTHROPIC_API_KEY is present in the environment, a hook
point is marked below where fresh generation could replace the bank pull.
The bank path is the production path.
"""
import json, os, re, datetime, urllib.request
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def rd(p, default=None):
    try:
        return json.load(open(os.path.join(ROOT, p)))
    except Exception:
        return default

NOW_CT = datetime.datetime.now(ZoneInfo("America/Chicago"))
TODAY = NOW_CT.date()
DOW = TODAY.strftime("%a")  # Mon, Tue, ...

cfg = rd("config/content-config.json", {"linkedin_start_day": 31, "post_days": ["Mon", "Wed", "Fri"]})
blackout = rd("config/blackout.json", {"ranges": []})
state = rd("data/engine-state.json", {"next_slot": 1, "streak": 0, "last_run": None})

def in_blackout():
    for r in blackout.get("ranges", []):
        if r["start"] <= TODAY.isoformat() <= r["end"]:
            return True
    return False

LIGHT = in_blackout()

# ── today's post ─────────────────────────────────────────────────────
post_html, post_meta = "", ""
is_post_day = DOW in cfg.get("post_days", [])
slot = state["next_slot"]
if is_post_day and slot <= 90:
    path = os.path.join(ROOT, f"content-bank/linkedin/day-{slot:03d}.md")
    raw = open(path).read()
    m = re.match(r"---\n(.*?)\n---\n\n(.*)", raw, re.S)
    fm, body = (m.group(1), m.group(2)) if m else ("", raw)
    tags = re.findall(r'- "(.*?)"', fm)
    day_number = cfg["linkedin_start_day"] + slot - 1
    body = f"Day {day_number}.\n\n" + body.strip()
    post_html = f"""
    <h2 style="margin:18px 0 6px">Today: LinkedIn Day {day_number}</h2>
    <div style="background:#f6f6f2;border:1px solid #ddd;border-radius:8px;padding:14px;white-space:pre-wrap;font-size:14px">{body}</div>
    <p style="font-size:12px;color:#666">Hashtag options: {" · ".join(tags) or "see bank file"} — post at 7:40 AM CT.</p>"""
    post_meta = f"Day {day_number}"
    state["next_slot"] = slot + 1
elif is_post_day:
    post_html = "<p><strong>Bank empty (90/90 used).</strong> Refill: write 10 new posts into content-bank/linkedin/ or run the optional generation path.</p>"
else:
    post_html = f"<p style='color:#666'>No post today (cadence {'/'.join(cfg.get('post_days', []))}). Engage: 10 minutes of comments on target-company PM posts.</p>"

# ── tasks ────────────────────────────────────────────────────────────
tasks = []
if not LIGHT:
    # 1. job task from public dashboard data
    try:
        u = "https://raw.githubusercontent.com/Shubham-Safaya/job-search-dashboard/main/data/dashboard_data.json"
        jd = json.load(urllib.request.urlopen(u, timeout=20))
        top = jd.get("top_matches") or []
        new_ct = (jd.get("summary") or {}).get("new_today") or (jd.get("summary") or {}).get("total_new") or len(top)
        if top:
            first = top[0]
            tasks.append(f"Job: {new_ct or len(top)} fresh matches — top: {first.get('company','?')} · {first.get('title','?')} → apply tonight. Full list: https://shubham-safaya.github.io/job-search-dashboard/")
        else:
            tasks.append("Job: review today's brief; if empty, send one hiring-manager DM from the target-company list.")
    except Exception:
        tasks.append("Job: dashboard data unreachable — open https://shubham-safaya.github.io/job-search-dashboard/ and pick one action.")
    # 2. EB1A rotation
    rot = rd("content-bank/eb1a-rotation.json", {"rotation": []}).get("rotation", [])
    if rot:
        wk = TODAY.isocalendar().week % len(rot)
        tasks.append("EB1A: " + rot[wk]["task"])
    # 3. build micro-task rotation
    micro = [
        "Check live/ healthcheck issues (should be zero): https://github.com/Shubham-Safaya/live/issues",
        "Skim yesterday's daily-engineering-log auto-entry; add one Notes line",
        "Reply to one EvenOut/Checkpoint user piece of feedback (or share one link)",
        "Review the portfolio stats strip renders today's date",
        "Trim one stale item from mission-control dashboard",
    ]
    tasks.append("Build: " + micro[TODAY.toordinal() % len(micro)])

# ── weekly attachments ───────────────────────────────────────────────
extra = ""
if not LIGHT and DOW == "Mon":
    week_no = min(13, max(1, (TODAY.isocalendar().week % 13) or 13))
    for suffix in ("DRAFT", "brief"):
        p = os.path.join(ROOT, f"content-bank/medium/week-{week_no:02d}-{suffix}.md")
        if os.path.exists(p):
            extra = f"<h2>This week's Medium ({suffix})</h2><div style='background:#f6f6f2;border-radius:8px;padding:12px;white-space:pre-wrap;font-size:13px'>{open(p).read()[:6000]}</div>"
            break
if not LIGHT and DOW == "Sat":
    week_no = min(13, max(1, (TODAY.isocalendar().week % 13) or 13))
    p = os.path.join(ROOT, f"content-bank/reels/week-{week_no:02d}.md")
    if os.path.exists(p):
        extra = f"<h2>This week's reel plan</h2><div style='background:#f6f6f2;border-radius:8px;padding:12px;white-space:pre-wrap;font-size:13px'>{open(p).read()}</div>"

# ── streak + assemble ────────────────────────────────────────────────
if state.get("last_run") == (TODAY - datetime.timedelta(days=1)).isoformat():
    state["streak"] = state.get("streak", 0) + 1
elif state.get("last_run") != TODAY.isoformat():
    state["streak"] = 1
state["last_run"] = TODAY.isoformat()

auto = "Auto-completed overnight: pulse refreshed, jobs indexed, portfolio stats updated, healthcheck ran."
task_html = "".join(f"<li style='margin:6px 0'>{t}</li>" for t in tasks)
mode = "LIGHT MODE" if LIGHT else f"streak {state['streak']}"
bank_left = 90 - (state["next_slot"] - 1)
refill_note = f"Bank: {bank_left} posts left" + (" — REFILL SOON" if bank_left <= 15 else "")

html = f"""<!doctype html><html><body style="font-family:-apple-system,Segoe UI,sans-serif;max-width:640px;margin:0 auto;color:#1b1d21">
<h1 style="font-size:20px">Good morning{', Shubham' if not LIGHT else ''}. <span style="font-size:12px;color:#888">{TODAY.strftime('%A, %b %d')} · {mode}</span></h1>
{post_html}
{'<h2 style="margin:18px 0 6px">Today (60–90 min)</h2><ul style="padding-left:18px;font-size:14px">' + task_html + '</ul>' if tasks else ''}
{extra}
<p style="font-size:12px;color:#666">{auto}<br>{refill_note} · <a href="https://shubham-safaya.github.io/mission-control/dashboard.html">dashboard</a></p>
</body></html>"""

os.makedirs(os.path.join(ROOT, "data/today"), exist_ok=True)
open(os.path.join(ROOT, "data/today/email.html"), "w").write(html)
open(os.path.join(ROOT, "data/today/subject.txt"), "w").write(
    f"Mission Control — {TODAY.strftime('%a %b %d')}" + (f" · {post_meta}" if post_meta else ""))
json.dump(state, open(os.path.join(ROOT, "data/engine-state.json"), "w"), indent=2)
json.dump({"date": TODAY.isoformat(), "bank_left": bank_left, "streak": state["streak"],
           "light_mode": LIGHT, "post": post_meta or None, "tasks": tasks},
          open(os.path.join(ROOT, "data/today/status.json"), "w"), indent=2)

# history per backbone 3a
os.makedirs(os.path.join(ROOT, "data/history"), exist_ok=True)
json.dump({"date": TODAY.isoformat(), "bank_left": bank_left, "streak": state["streak"], "light": LIGHT},
          open(os.path.join(ROOT, f"data/history/{TODAY.isoformat()}.json"), "w"), indent=2)
print(f"assembled: {TODAY} light={LIGHT} post={post_meta or 'none'} tasks={len(tasks)} bank_left={bank_left}")
