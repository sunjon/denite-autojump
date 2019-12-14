# Denite-autojump

[![](http://img.shields.io/github/issues/sunjon/denite-autojump.svg)](https://github.com/sunjon/denite-autojump/issues)
[![](http://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![](https://img.shields.io/badge/doc-%3Ah%20denite--autojump.txt-red.svg)](doc/denite-autojump.txt)

A [Denite](https://github.com/Shougo/denite.nvim) source for [autojump](https://github.com/wting/autojump).

## Install

For [vim-plug](https://github.com/junegunn/vim-plug) for, add:

    Plug 'Shougo/denite.nvim'
    Plug 'sunjon/denite-autojump'

To your `.vimrc` and run `PlugInstall` and `UpdateRemotePlugins` after
a restart.

**Note:** [denite.nvim](https://github.com/Shougo/denite.nvim) requires python3+
Make sure `has('python3')` returns true, and run:

    pip3 install neovim

before you install any neovim remote plugin.

Run `:CheckHealth` if you get any problem.

## Actions

* `autojump` default action

## Configuration