import sublime
from typing import NamedTuple, Optional
import os.path

class WindowDetail:

  def __init__(self, window: sublime.Window, folder: str) -> None:
    self.window = window
    self.folder = folder
    self.short_name = os.path.basename(self.folder)
    self.active_view = self.get_active_view()
    self.view_count = len(window.views())

  def get_active_view(self) -> str:
    view: Optional[sublime.View] = self.window.active_view()
    if view:
      if (file_name := view.file_name()) is not None:
        return file_name
      elif view.name():
        return view.name()
      else:
        return "-"
    else:
      return "<no active view>"


