from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# ASCII art kepala Foxy (dirancang agar pas untuk terminal)
fox_ascii_head = r"""
        .-"      "-.
       /            \
      |              |
      |,  .-.  .-.  ,|
      | )(_o/  \o_)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`
"""

def get_fox_panel(message: str) -> Panel:
    """Menggabungkan ASCII art Foxy dengan pesan untuk ditampilkan sebagai panel dinamis."""
    text = Text(fox_ascii_head + "\n\n" + message, style="bold")
    return Panel(text, title="Fox 🦊", border_style="red")

def show_intro():
    """Menampilkan intro sekali (tidak dinamis/live)."""
    panel = get_fox_panel("🦊 Hi, I'm Fox. Ready to assist you!")
    console.print(panel)
