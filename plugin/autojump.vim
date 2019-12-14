" ============================================================================
" Description: denite-autojump commands
" Author: Senghan Bright <sunjon at gmail.com>
" Licence: MIT licence
" Version: 0.1
" Last Modified:  Dec 14, 2019
" ============================================================================


if exists('g:loaded_autojump')
  finish
endif
let g:loaded_autojump = 1

let g:autojump_command  = get(g:, 'autojump_command', '/usr/local/bin/autojump')
let g:autojump_database = get(g:, 'autojump_database', '~/Library/autojump/autojump.txt')
let g:autojump_register = get(g:, 'autojump_register', v:true)
let g:autojump_echo     = get(g:, 'autojump_echo', v:true)

highlight link AutojumpMsg ModeMsg

if filereadable(g:autojump_command)
  call denite#custom#action('directory', 'autojump', function('autojump#do_action'))
else
  call denite#util#print_error("Unable to locate autojump binary: " . g:autojump_command)
endif
