import sublime
from typing import Dict, NamedTuple, Optional
import os.path

class WindowDetail:

  def __init__(self, window: sublime.Window) -> None:
    self.window = window
    self.folder = self.get_folder()
    self.long_name : str= self.get_long_name()
    self.short_name: str = self.get_short_name()
    self.active_view: str = self.get_active_view()
    self.view_count: int = len(window.views())

  def get_folder(self) -> Optional[str]:
    return self.get_folder_variable(self.window.extract_variables())

  def get_long_name(self) -> str:
    if self.folder and self.folder.lstrip().rstrip():
      return self.folder
    else:
      return "(no folder)"

  def get_short_name(self) -> str:
    long_name = self.get_long_name()
    if long_name != "(no folder)":
      return os.path.basename(long_name)
    else:
      return "<unknown>" #markup is only allowed in the trigger of QuickPanelItem

  def get_folder_variable(self, variables: Dict[str, str]) -> Optional[str]:
    return variables.get("folder")

  def get_active_view(self) -> str:
    view: Optional[sublime.View] = self.window.active_view()
    if view:
      if (file_name := view.file_name()) is not None:
        return file_name
      elif view.name() and view.name().lstrip().rstrip():
        return view.name()
      else:
        return "(no named views)"
    else:
      return "(no active view)"


