import os
import re

from .base import Base
from denite.util import error, expand, Nvim


class Source(Base):
    """Denite source for autojump directories."""

    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)

        self.name = "autojump"
        self.kind = "directory"
        self.default_action = "autojump"
        self.vars["data_file"] = vim.vars.get(
            "autojump_database", ""
        )

    def on_init(self, context):
        context["data_file"] = expand(self.vars["data_file"])

    def gather_candidates(self, context):
        """Gather candidates from `autojump.txt`."""
        candidates = []

        try:
            f = open(context["data_file"], "r")
        except OSError:
            err_string = "Coult not open " + context["data_file"]
            error(self.vim, err_string)
            f = []

        content = f.readlines()
        path_list = self.sorted_num(content)
        for path in path_list[::-1]:
            stripped = re.sub(r"^\d+?\.\d+?\s", "", path.rstrip())
            short_rel = self.vim.call('fnamemodify', stripped, ":~:.")
            candidates.append({
                "word": short_rel,
                "action__path": stripped,
                "abbr": short_rel + os.sep
                })

        return candidates

    def sorted_num(self, l):
        """Natural sort list of alpha-numberic strings."""
        convert = lambda text: int(text) if text.isdigit() else text
        alphanum_key = lambda key: [convert(c) for c in re.split("([0-9]+)", key)]
        return sorted(l, key=alphanum_key)
