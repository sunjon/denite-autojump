# Denite-autojump

[![](http://img.shields.io/github/issues/sunjon/denite-autojump.svg)](https://github.com/sunjon/denite-autojump/issues)
[![](http://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![](https://img.shields.io/badge/doc-%3Ah%20denite--autojump.txt-red.svg)](doc/denite-autojump.txt)

An [autojump](https://github.com/wting/autojump) source for [denite.nvim](https://github.com/Shougo/denite.nvim).

## Install

For [vim-plug](https://github.com/junegunn/vim-plug), add:

```vim
Plug 'shougo/denite.nvim'
Plug 'sunjon/denite-autojump'
```

to your `.vimrc` and run `:PlugInstall` and `:UpdateRemotePlugins` after
a restart.

**Note:** [denite.nvim](https://github.com/Shougo/denite.nvim) requires python3+.
Make sure `has('python3')` returns true, and run:

`pip3 install neovim`

before you install any neovim remote plugin.

Run `:CheckHealth` if you encounter any issues.

## Key Binds

Create a key bind in your .vimrc. eg:

`nnoremap <silent> <Leader>p :Denite autojump<Cr>`

## Actions

- `autojump` - `cd` to selected path. Default action

## Configuration Options

- `g:autojump_command`

  Path to the autojump binary. (string)

  default: /usr/local/bin/autojump

- `g:autojump_database`

  Path to the autojump.txt db. (string)

  default: ~/Library/autojump/autojump.txt

- `g:autojump_register`

  Register the cd event with autojump. (bool)

  default: 1

- `g:autojump_echo`

  Echo the cd event to the cmdline. (bool)

  default: 1
