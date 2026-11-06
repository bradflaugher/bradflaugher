I build small models that run on the machine in front of you, and software for machines that don't have much machine.

[bradflaugher.com](https://bradflaugher.com)

## Models

The inference stays on the device.

**[divid3](https://github.com/bradflaugher/divid3)** routes a search query without a server. A 22 MB `all-MiniLM-L6-v2` embeds it in WASM and picks a destination from a JSON file you edit. Bangs such as !yt beat the model. A bare domain goes straight through. A phone that cannot hold the weights uses a keyword router. [divid3.com](https://divid3.com)

**[genaro-poker](https://github.com/bradflaugher/genaro-poker)** is a poker model meant to live on a phone. Two Qwen3 fine-tunes, [0.6B](https://huggingface.co/predbrad/Genaro-poker) (Q4_K_M, 397 MB) and [1.7B](https://huggingface.co/predbrad/Genaro-poker-1.7B) (Q4_K_M, 1.1 GB), trained on PokerSI's prompts. 96 tokens: a legal action inside a GBNF grammar, and one short line that does not name its cards. v3 is distilled from a search solver running on PokerSI's own engine.

**[PokerSI](https://github.com/bradflaugher/PokerSI)** is that runtime. Android poker, every opponent played by llama.cpp on the phone. Six games, a tour, personas who bet and talk. No network unless a model is downloading. [Google Play](https://play.google.com/store/apps/details?id=com.bradflaugher.pokersi)

<p align="center">
  <img src="https://raw.githubusercontent.com/bradflaugher/PokerSI/main/docs/screenshots/table-holdem.png" width="260" alt="Texas Hold'em against three on-device models. One of them is talking.">
</p>

**[post-training](https://github.com/bradflaugher/post-training)** is a 4×4 word-connection game run by `albert-base-v2`, 11.8M parameters, in the browser. Group four tokens and the group opens onto the sentence probe, the probability, and the logit. The lab takes any sentence, or four of yours, and builds a board from the model's own rankings. [post-training.win](https://post-training.win)

**[LMPlayground](https://github.com/bradflaugher/LMPlayground)** is a fork of [andriydruk/LMPlayground](https://github.com/andriydruk/LMPlayground).

## Game Boy

Four cartridges. C, a Makefile, original art and sound.

**[open-world](https://github.com/bradflaugher/open-world)** is a wordless walk in a world 65,536 cells on a side, generated from a 16-bit seed, wrapping at the edges. Light three beacons. A fourth light appears. Sit there and the world ends. The cairns you left are ruins in the next one. No combat. Almost no text.

**[infinite-best](https://github.com/bradflaugher/infinite-best)** is a sliding puzzle. You move until something stops you. A solver on the cartridge computes par while the next sector loads. Match it and the grade is BEST. Rewind is free and the move counter is not. A generated sector is kept only when taking the new rule out makes the solution longer, or impossible.

**[alignment](https://github.com/bradflaugher/alignment)** is a mech on a station that lost its gravity. Up+A turns the floor into the ceiling. Eight hand-built sectors, a boss in each, then an endless station from a seed.

**[speedy-purple-peter](https://github.com/bradflaugher/speedy-purple-peter)** is a platform level with no flagpole. The run, the skid, and the three jump heights use the 1985 subpixel constants. The art does not. Pick a seed on the title screen and the run is the same run every time.

<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://raw.githubusercontent.com/bradflaugher/open-world/main/docs/screens/gameplay.gif" width="100%" alt="A figure walking a generated coast on a Game Boy."><br>
      <sub><a href="https://github.com/bradflaugher/open-world">open-world</a></sub>
    </td>
    <td align="center" width="50%">
      <img src="https://raw.githubusercontent.com/bradflaugher/infinite-best/main/docs/screens/gameplay.gif" width="100%" alt="Sliding through a sector. The cartridge grades the solution against par."><br>
      <sub><a href="https://github.com/bradflaugher/infinite-best">infinite-best</a></sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <img src="https://raw.githubusercontent.com/bradflaugher/alignment/main/docs/screens/gameplay.gif" width="100%" alt="A mech fighting through a hangar, gravity ready to flip."><br>
      <sub><a href="https://github.com/bradflaugher/alignment">alignment</a></sub>
    </td>
    <td align="center" width="50%">
      <img src="https://raw.githubusercontent.com/bradflaugher/speedy-purple-peter/main/docs/screens/gameplay.gif" width="100%" alt="Peter running an endless seeded platform level."><br>
      <sub><a href="https://github.com/bradflaugher/speedy-purple-peter">speedy-purple-peter</a></sub>
    </td>
  </tr>
</table>

## Android

Clients on Google Play. No ads. PokerSI is listed under Models.

**[bf-12c](https://github.com/bradflaugher/bf-12c)** is an HP-12C. Landscape is the 4×10 keyboard, gold f legends and blue g legends, four phosphors, RPN, and the financial keys on the top row. [Google Play](https://play.google.com/store/apps/details?id=com.bradflaugher.bf12c)

<img src="https://raw.githubusercontent.com/bradflaugher/bf-12c/main/docs/screenshots/landscape.png" width="800" alt="bf-12c in landscape. Green phosphor, the full 12C keyboard.">

**[CozyGrams](https://github.com/bradflaugher/CozyGrams)** is nonograms for a television. Two controllers, Rose and Sky, one picture. A phone plays the same puzzles with a fill-or-cross pen. [Google Play](https://play.google.com/store/apps/details?id=com.cozygrams.tv)

**['Bout That Action](https://github.com/bradflaugher/bout-that-action)** drops you on a roof and only goes down: tower, crust, magma, Hell, void. Floors, music, and sound effects are generated. No asset files. No network. [Google Play](https://play.google.com/store/apps/details?id=com.bradflaugher.aboutthataction)

**[Blauncher](https://github.com/bradflaugher/Blauncher)** is a home screen with the date, a search bar, and one shortcut. Forked from [Olauncher](https://github.com/tanujnotes/Olauncher). The app has no internet permission. [Google Play](https://play.google.com/store/apps/details?id=com.bradflaugher.blauncher)

<table>
  <tr>
    <td align="center" width="62%">
      <img src="https://raw.githubusercontent.com/bradflaugher/CozyGrams/main/docs/screenshots/gameplay.webp" width="100%" alt="Rose and Sky solving one nonogram on a television."><br>
      <sub><a href="https://github.com/bradflaugher/CozyGrams">CozyGrams</a></sub>
    </td>
    <td align="center" width="38%">
      <img src="https://raw.githubusercontent.com/bradflaugher/bout-that-action/main/docs/screenshots/rooftop.png" width="180" alt="A helicopter drop onto a neon roof. The game only goes down from here."><br>
      <sub><a href="https://github.com/bradflaugher/bout-that-action">'Bout That Action</a></sub>
    </td>
  </tr>
</table>

## Desk

**[b.indicators](https://github.com/bradflaugher/b.indicators)** is my Omarchy hover row: screenshot, a warning while passwordless sudo is on, night light, do not disturb, stay awake. The toggles shell out to the public `omarchy-toggle-*` commands, because a third-party bar widget is not handed the first-party service objects.

**[bradflaugher.com](https://github.com/bradflaugher/bradflaugher.com)** is the site. One HTML file, no build step, Cloudflare Pages. [bradflaugher.com](https://bradflaugher.com)

## Book

**[AI Harmony](https://github.com/bradflaugher/AI-Harmony-Book)** is the LaTeX source of the book. The Fable Edition PDF, the epub, and the first-edition audiobook are in the [releases](https://github.com/bradflaugher/AI-Harmony-Book/releases). [aiharmony.info](https://aiharmony.info)

<img src="https://raw.githubusercontent.com/bradflaugher/AI-Harmony-Book/main/preview.png" width="640" alt="A typeset spread from AI Harmony.">
