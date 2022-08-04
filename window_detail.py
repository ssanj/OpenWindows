import sublime
from typing import NamedTuple

class WindowDetail(NamedTuple):
  window: sublime.Window
  folder: str
