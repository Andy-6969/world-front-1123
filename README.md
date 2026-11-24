# world-front-1123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Andy-6969/world-front-1123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Andy-6969/world-front-1123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Monday 23 November 2026 on one page, made for the [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
bounty "Sum up 23 November's world news in one image".

![Monday 23 November 2026](entry.png)

Three drawn leads: Ukraine says its sea drones sank the Russian corvette Merkury in Benghazi, Libya; India pledges
$1.62bn to help Nepal rebuild as PM Balendra Shah visits New Delhi; and a national strike grounds every flight in
Belgium. Eight drawn cards follow, each with its key number in large type, then a short list of the day's other
stories, a UTC timeline, region counts and a date check that names what was left out because it happened on
another day.

Each story carries a tag: CONFIRMED (two or more outlets), OFFICIAL (on the record), REPORTED (one outlet) or
CLAIM (one side's word). [docs/sources.md](docs/sources.md) lists the outlets behind every line.

## Build and run

- `tools/stories.py` holds every story; `tools/pictures.py` draws each picture as SVG; `tools/build.py` writes
  the page as HTML (set `NE_DIR` to a folder holding Natural Earth's public-domain `ne_110m_land.geojson`, not
  committed, for the optional map).
- `tools/render.ps1` screenshots the page with headless Chrome at 2x and `tools/shrink.py` scales it to the
  1024 x 1024 `entry.png` (under 1 MiB).
- `main.ts` (Node 22, no dependencies, no network) checks `entry.png` and copies it to `/output/entry.png`:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

No image model was used: text, pictures, timeline and layout are all drawn in code.

## License

MIT — see [LICENSE](LICENSE).
