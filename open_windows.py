import sublime
import sublime_plugin
from typing import List
import os
import json
import subprocess
from OpenWindows.window_detail import WindowDetail

class OpenWindowsCommand(sublime_plugin.WindowCommand):

  def run(self):
    window = self.window
    if window:

        open_windows: List[sublime.Window] = sublime.windows()

        window_details: List[WindowDetail] = [WindowDetail(w, w.extract_variables()['folder']) for w in open_windows if 'folder' in w.extract_variables()]
        quick_panel_items: List[sublime.QuickPanelItem] = list(map(lambda wd: self.to_quick_panel_items(wd), window_details))
        window.show_quick_panel(
          items = quick_panel_items,
          placeholder = "Open Windows:",
          on_select = lambda index: self.on_select(window_details, index),
        )
    else:
      sublime.message_dialog("No active window found")

  def to_quick_panel_items(self, window_detail: WindowDetail) -> sublime.QuickPanelItem:
    return sublime.QuickPanelItem(window_detail.folder, "", "", sublime.KIND_AMBIGUOUS)

  def on_select(self, open_windows: List[WindowDetail] ,index: int) -> None:
    if index >= 0 and len(open_windows) > index:
      open_windows[index].window.bring_to_front()
