"""sizing.py (Claude, 11-21-2026): how long would each era's fastest known computer take to train a modern AI model? Pure arithmetic on cited speeds.

Workloads (floating-point operations to train):
  small video model  1e21  ESTIMATE, deliberately small; ModelScope's real figure is not published
  GPT-4 class        2e25  Epoch AI's estimate (https://epoch.ai/data-insights/models-over-1e25-flop)
Speeds are each machine's measured or peak rate (TOP500 Linpack where it exists), cited in docs/02_sizing.md. "Secret lead" multiplies a machine by
50 or 200, the range the NSA itself measured for its Harvest codebreaker over the best commercial machine in 1962. Run: python sizing.py"""

YEAR = 3.15576e7  # seconds in a year
SMALL, GPT4 = 1e21, 2e25
MACHINES = [("Cray-1, 1976 (peak)", 1.6e8), ("Cray-2, 1985", 1.9e9), ("CM-5, 1993", 5.97e10), ("ASCI White, 2000", 4.938e12),
            ("Earth Simulator, 2002", 3.586e13), ("Roadrunner, 2008", 1.026e15), ("Jaguar, 2009", 1.75e15)]


def span(seconds):
    y = seconds / YEAR
    return f"{y:,.1f} years" if y >= 1 else f"{y * 365.25:,.1f} days"


print(f"{'machine':24s} {'FLOP/s':>9s}  {'small model':>16s}  {'GPT-4 class':>18s}  {'small, lead x50':>16s}  {'small, lead x200':>16s}")
for name, rate in MACHINES:
    print(f"{name:24s} {rate:9.3g}  {span(SMALL / rate):>16s}  {span(GPT4 / rate):>18s}  {span(SMALL / rate / 50):>16s}  {span(SMALL / rate / 200):>16s}")
need = SMALL / YEAR
print(f"\nto train the small model in one year needs {need:.3g} FLOP/s: {need / 1.9e9:,.0f} times the Cray-2 of 1985")
