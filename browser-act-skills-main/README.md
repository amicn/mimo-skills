# BrowserAct Skills for Eburon AI

Browser automation CLI skills purpose-built for AI agents — navigation, interaction, data extraction, screenshots, form automation, multi-browser parallel operation, proxy support, and human-agent collaboration.

Powered by [BrowserAct](https://www.browseract.com) — a browser CLI built for LLM reasoning, not human scripts.

## Why BrowserAct

**A browser for agents must get four things right:**

1. **Break through blocks** — stealth fingerprint spoofing, TLS rotation, proxy switching, captcha solving, human handoff
2. **Three browser modes** — `chrome` (local login state), `stealth` privacy (fresh fingerprint), `stealth` fixed (stable identity)
3. **Zero-interference concurrency** — independent cookies, fingerprints, proxies per session; tasks don't cross-contaminate
4. **Designed for agent reasoning** — compact text output (token-efficient), indexed interaction (click/type by index), semantic memory (browser desc matching)

## Entry Skills

| Skill | Description |
|-------|-------------|
| [browser-act](./browser-act) | Core browser automation CLI — navigation, interaction, extraction, screenshots |
| [browser-act-skill-forge](./browser-act-skill-forge) | Forge reusable Skill packages from website exploration |
| [flutter-dev](./flutter-dev) | Full-stack Flutter development — MVVM + Repository architecture, go_router, responsive layout, JSON serialization, i18n, widget/integration testing |

## Solutions Catalog

### Frontend & PWA Design

| Skill | Description |
|-------|-------------|
| [mobile-pwa-design](./solutions/mobile-pwa-design) | Design modern PWA frontends — mobile-first HTML/CSS, app-shell, offline, Touch-optimized UI. Reference: 400+ ThemeForest mobile templates |

### Search & Research

| Skill | Description |
|-------|-------------|
| [google-search-serp](./solutions/search-research/google-search-serp) | Extract Google SERP data: organic, ads, PAA, AI Overview |
| [web-page-marker](./solutions/search-research/web-page-marker) | Convert any webpage to clean Markdown |

### Video Platforms

| Skill | Description |
|-------|-------------|
| [youtube-search](./solutions/video-platforms/youtube-search) | Extract YouTube search results with metadata |
| [youtube-transcript](./solutions/video-platforms/youtube-transcript) | Extract YouTube video transcripts with timestamps |

### AI Video Generation & Production

| Skill | Description |
|-------|-------------|
| [ai-video-generation](./ai-video-generation) | Core AI video generation — 100+ t2v/i2v/lipsync models (Kling, Sora, Veo, Wan, Seedance, Hailuo, Runway) via Muapi API, 5-part cinematic prompt formula, scene planning workflow, lip-sync talking heads |
| [ai-video-production](./ai-video-production) | Full production pipeline — ElevenLabs/Qwen3-TTS voiceovers, ACE-Step music generation with scene presets, Remotion compositing, timing sync, cloud GPU (Modal/RunPod), SadTalker talking heads, watermark removal, upscaling, brand management |
| [ai-video-cinema](./ai-video-cinema) | Cinematic AI video with Google Veo 3.1 — 5-part formula for cinema-quality prompts, ingredients-to-video with multi-reference images, first→last frame transitions, FFmpeg overlay/concat/GIF/audio-sync tooling |
| [tiktok-contents](./tiktok-contents) | TikTok content creation with Symphony Creative Studio — Dreamina Seedance 2.0 cinematic video, avatar narrators, translate & dubbing, AI video remixing, Recommended Creatives, Symphony Automation/API, trend-driven TikTok ad production |

## Quick Start

```bash
# Install browser-act
uv tool install browser-act-cli --python 3.12

# Extract protected page content (zero config)
browser-act stealth-extract https://example.com

# Full browser automation
browser-act --session my-task browser open <id> https://example.com
browser-act --session my-task state          # See clickable elements
browser-act --session my-task click 3        # Click by index
browser-act --session my-task input 2 "hi"   # Type into a field
```

## Install a Skill

Tell your AI agent:

> Install browser-act from https://github.com/eburon-ai/browser-act-skills/tree/main/browser-act

Or for a solution skill:

> Install google-search-serp from https://github.com/eburon-ai/browser-act-skills/tree/main/solutions/search-research/google-search-serp

## Architecture

```
Entry Skill (SKILL.md) ── teaches agent "browser-act exists"
    │
    └── Runtime: `browser-act get-skills core` ── environment state + commands + directives
```

Two-layer design: the entry skill is lightweight and stable. The actual instructions come from `get-skills core` at runtime, which is always version-matched to the CLI.

---

Built with ❤️ by Eburon AI — founded by Joe Lernout
