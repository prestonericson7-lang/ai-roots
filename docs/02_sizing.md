# Sizing it: could each era's hardware have made AI video?

Preston's claim to test: AI could make convincing video in the 1980s, and early-2000s AI video is everywhere. This chapter sizes the hardware side.
Everything here is my arithmetic on cited speeds (**MEASURED** as arithmetic); the workloads are **ESTIMATES**. Reproduce it with
[`tools/sizing.py`](../tools/sizing.py).

## The workloads

- **A small modern video model: 1e21 floating-point operations to train** (ESTIMATE, deliberately small; ModelScope's real figure, the model behind
  the 2023 spaghetti clip, isn't published).
- **A GPT-4-class model: about 2e25** ([Epoch AI](https://epoch.ai/data-insights/models-over-1e25-flop)).

## The machines, and how long they would take running flat out

| Machine | Speed | Small video model | GPT-4 class | Small model, secret lead x50 | x200 |
|---|---|---|---|---|---|
| Cray-1, 1976 (peak) | 160 megaflops | 198,050 years | about 4 billion years | 3,961 years | 990 years |
| Cray-2, 1985 | 1.9 gigaflops | 16,678 years | about 334 million years | 334 years | 83 years |
| CM-5, 1993 | 59.7 gigaflops (UNVERIFIED figure) | 531 years | about 10.6 million years | 10.6 years | 2.7 years |
| ASCI White, 2000 | 4.9 teraflops | 6.4 years | 128,344 years | 47 days | 12 days |
| Earth Simulator, 2002 | 35.9 teraflops | 323 days | 17,673 years | 6.5 days | 1.6 days |
| Roadrunner, 2008 | 1.03 petaflops | 11.3 days | 618 years | under a day | under a day |
| Jaguar, 2009 (paid for by the NSA) | 1.75 petaflops | 6.6 days | 362 years | under a day | under a day |

**Why a "secret lead" column.** The NSA's own evaluation found its 1962 Harvest codebreaker 50 to 200 times more powerful than the best commercial
machine ([IEEE Spectrum](https://spectrum.ieee.org/cold-war-codebreaker-nsa-ibm)). That is the one measured size of a secret compute lead I found,
so the table applies it.

Sources for the speeds: [Cray-1](https://en.wikipedia.org/wiki/Cray-1), [TOP500 November 2000](https://top500.org/lists/top500/list/2000/11),
[TOP500 June 2002](https://top500.org/lists/top500/list/2002/06), [TOP500 June 2008](https://top500.org/lists/top500/2008/06/),
[HPCwire on Jaguar](https://www.hpcwire.com/2012/03/19/nsa_employs_cutting-edge_supercomputing_for_domestic_surveillance/); the Cray-2's 1.9
gigaflops is from histories of supercomputing; the CM-5's figure is from my memory of the June 1993 TOP500 list and needs checking.

## Storage

50 TB of training video (ESTIMATE) cost about $1.74 billion in disk at 1985's price (about $34,750 per GB) and about $500 thousand at 2000's
(about $10 per GB). Sources: [storage cost history](https://boingboing.net/2011/03/08/tracking-the-astound.html),
[stellarinfo table](https://stellarinfo.co.in/kb/history-evolution-of-hard-disk-drive.php).

## What it means (ESTIMATE)

- **Before about 1993, no.** Even with a Harvest-sized secret lead, the 1985 run takes 83 to 334 years. The 1980s could fake a person by makeup and
  compositing, not by a learning machine.
- **The hardware door opens in the 1990s for a secret program.** With a secret lead, 1993 takes 2.7 to 10.6 years (a dedicated decade), and 2000
  takes 12 to 47 days. In the open, the door opens about 2002 to 2009.
- **What stays shut is the methods.** The open world's generative methods arrive in 2014 (GANs), 2015 to 2020 (diffusion) and 2017 (the transformer).
  A secret program would have needed them years earlier; nothing found shows that, and the CIA's 2003 fake used actors. This is where
  [shot 1](06_shots_in_the_dark.md) lives.
- **GPT-4-class models were out of reach for any known machine before the 2020s** (hundreds of years even on 2009 hardware).
