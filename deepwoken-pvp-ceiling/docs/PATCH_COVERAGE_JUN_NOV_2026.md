# Patch coverage audit: June–November 2026 (Deepwoken PvP mantras)

**Audited 2026-11-14**. Source-coverage correction to the previous May-only patch audit. **NOT a complete official changelog**: the official Discord patch channel and in-game patch-note viewer contain releases not readable through public web search. Never infer full patch contents from Roblox publication timestamps.

## Access points

- [Official Deepwoken Discord](https://discord.com/servers/920707638034067486) — **best primary location for per-week patch notes**, messages require Discord access; the public landing page does not reveal message text.
- [In-game patch-note viewer](https://deepwoken.fandom.com/wiki/Version_History/2026) — apparently added during game-health updates; check game main menu for up-to-date releases.
- [Fandom Version History 2026](https://deepwoken.fandom.com/wiki/Version_History/2026) — public accessible text **stops at May 31** (not the last release).
- [Deepwoken Builder patch-notes page](https://deepwoken.co/patch-notes) — says **Coming soon**; cannot be treated as an archive.
- [Deepwoken.co Builder](https://deepwoken.co/) — current mantra stat data, not a date-by-date patch archive; useful for verifying current base damage.
- [Bloxstatus updates](https://bloxstatus.com/games/deepwoken/updates/) — Nov 2, 6, 9 Roblox published timestamps (NOT notes); some page text is stale, even showing "yesterday" for Nov 9.
- [SpawnRadar game update history](https://www.spawnradar.com/games/1359573625/deepwoken/history) — its 500 changes appear hourly, suspect polling artefacts, not evidence of 500 genuine gameplay patches.
- [Unofficial deepwokengame.wiki hub](https://deepwokengame.wiki/updates/) — gives November seasonal summaries and some October patch labels, but not original official transcript or reliable numeric balance diff.
- [Sept 2026 comparative report](https://earnaldo.com/blog/deepwoken-vs-arcane-odyssey) — details of August 13 and 22; secondary source, not official.
- [Reddit r/deepwoken](https://www.reddit.com/r/deepwoken/) — dated player observations and balance reports, not proof of exact patch entry.

## Month-by-month coverage

| Month | Source coverage | Verified dated sightings and PvP implications | Confidence |
|---|---|---|---|
| June 2026 | **Gap**: no full official changelog retrieved | Game continued to receive changes, but this investigation has **no itemized primary June list** | NO PATCH TRANSCRIPT |
| July 2026 | **Partial** community reporting | Aug 1 player says previous patch nerfed Gale Trap, Hailbreaker, Captain's Call, SH Periapt, Gale Pale, dagger swing, and backstab tech; this identifies **late-July leads**, not numbers or exact shipping dates | COMMUNITY REPORT |
| August 2026 | **Partial** secondary report + dated Reddit | Aug 13: Steelscale Dusters, new FTD and CHA/INT talents, Battle Royale map and Chaos matchmaking score reported. Aug 22 `pv_AUG_22_17:49a`: Palace Tachi, Guard Turrets, Sightless Beam duration **3s→2s**, max damage reportedly **-1/3**, cooldown **16→24s**, optional Blindseer blindfold | DATED SECONDARY |
| September 2026 | **Gap** primary notes; community evidence of patch cadence | Sept 5 players discuss omitted hotfixes/bugs; do **not** invent numerical balance modifications | COMMUNITY / INCOMPLETE |
| October 2026 | **Partial** unofficial season/guide | Oct 19 `pv_OCT_20_01:11a` merge Mastery+Conceit into Shrine of Ego (unofficial guide). Oct 31 Hallowtide / Sanguine Blaze / Alloyblood report. Exact official release text unverified | SECONDARY |
| November 2026 (to 14th) | **Partial** community + platform timestamps | Roblox publish stamps Nov 2, 6, 9 (contents unknown); Nov 5 players describe new Flame+Blood mantras as high-pressure and difficult to react to, with counterarguments (windup/endlag). Nov 11 players still discuss Shadow/Gale/Thunder PvP vs Fire+Blood ranged pressure | PLATFORM / COMMUNITY |

**No month June–November can yet be marked fully audited.** The statement “all latest patches analyzed” is not defensible; archive is incomplete.

## Links grounding specific month claims

- [Aug 1: player lists nerfs to several PvP staples](https://www.reddit.com/r/deepwoken/comments/1vca1cb/deep_is_getting_kinda_dry/).
- [Aug 13 / Aug 22 details including Sightless Beam nerf](https://earnaldo.com/blog/deepwoken-vs-arcane-odyssey).
- [Sept 5 players discuss gaps in hotfix cadence](https://www.reddit.com/r/deepwoken/comments/1w7xmga/genuinely_why_dont_they_put_out_hotfixes/).
- [Oct 19 Shrine of Ego patch account, secondary](https://deepwokengame.wiki/guides/deep-shrines/).
- [Oct 31 seasonal changes, secondary](https://deepwokengame.wiki/updates/hallowtide-2026/).
- [Nov 5 Flame+Blood PvP reactions: conflicting opinions](https://www.reddit.com/r/deepwoken/comments/1xov0lx/anyone_else_feel_like_those_new_flame_blood/).
- [Nov 11 practical attunement commentary](https://www.reddit.com/r/deepwoken/comments/1xtcxrq/types_of_magic/).
- [Nov 2/6/9 Roblox publish timestamps, not notes](https://bloxstatus.com/games/deepwoken/updates/).
- [Official Discord entry point](https://discord.com/servers/920707638034067486).
- [Builder Patch Notes page has no patch content](https://deepwoken.co/patch-notes).

## Impact on our mathematical ceiling model

1. **Sightless Beam** — previous 3s channel, if used, is invalid after the Aug 22 reported 2s/max-damage nerf. The exact tick count after nerf requires a fresh Lv5 test. Do NOT apply -1/3 universally to every level without confirming the patch numbers.
2. **Gale Trap, Hailbreaker, Captain's Call and Gale Pale** — July community reports indicate changes, so a pre-August Gale proc/stun combo may be inapplicable. Confirm with official July logs.
3. **Bloodrend + Flamecharm / Bloodrend + Ironsing** — plausible November contender meta due to detonation/pressure and new hybrid mechanics; exact per-target hits, damage and post-release hotfixes unknown, so do not label S-tier proven.
4. **Ceaseless / Tornado** — cross-version base data remain inconsistent; old wiki vs current builder source conflict still not resolved.
5. **Other** — verify defensive movement, resistances, penalties, Oath/armor changes per patch. Single-cast raw damage does not directly predict competitive win rate.

## Required verification for a complete archive

Download/copy **the actual official patch posts** from June 1 through Nov 14 2026, including midweek hotfixes and their timestamps. For every note, record:
`published_at | original_url_or_message_id | patch_version | affected_object | effect_type | prior | new | source_confidence`.

Then diff against the builder files and rerun damage tests. Specifically check channel `#updates`, `#patch-notes` or equivalent in the **official** server — exact channel name unconfirmed because the public landing page hides the messages. Do not invent the channel URL.

Until then, keep overall status as **PARTIAL** and remove any impression that the late-2026 meta is fully known.

## August 13–14: further patch-specific numeric leads (secondary source)

A dated [Aug 16 weapon audit](https://earnaldo.com/blog/deepwoken-tier-list-2026) explicitly attributes its entries to **Aug 13 `pv_AUG_13_04:19a`** and **Aug 14 hotpatch `3.2.18a`**:
- **Alloyed Falchion buff** (magnitude omitted).
- **Bloodedge** posture scaling cut by half; base posture 7→6 and **+0.1s endlag**.
- **Bloodfouler** running crit made **jumpable** (weaker in PvP, not a mantra hit-count nerf).
- **Ghost** from Aug 13 blocks enemy lock-on during its invisibility window, which affects projectile/mantra hit probability; not a raw damage multiplier.
- **Steelscale Dusters** listed 14 base / Light scaling 10 at 55 Light, swing 1.12x (secondary stat table, not directly a mantra ceiling).

These statements are **not from an official patch transcript**. Treat as dated verification leads, not patch-certified truth.
