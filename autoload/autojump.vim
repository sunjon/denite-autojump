function! autojump#do_action(context)
    let l:path = a:context['targets'][0]['action__path']
    call denite#util#cd(l:path)

    if g:autojump_register
      silent execute '!' . g:autojump_command . ' --add ' . l:path . ' &'
    endif

    if g:autojump_echo
      call denite#util#echo('AutojumpMsg', '[autojump] ' . l:path)
    endif
endfunction

