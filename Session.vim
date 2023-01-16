let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd /mnt/c/projects/TP_GenieLog/projet_GL
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +25 /mnt/c/projects/TP_GenieLog/projet_GL/app/routes/calendar_router.py
badd +0 /mnt/c/projects/TP_GenieLog/projet_GL/app/routes/auth.py
argglobal
%argdel
$argadd .
edit /mnt/c/projects/TP_GenieLog/projet_GL/app/routes/calendar_router.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
2wincmd h
wincmd w
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 30 + 118) / 236)
exe 'vert 2resize ' . ((&columns * 86 + 118) / 236)
exe 'vert 3resize ' . ((&columns * 118 + 118) / 236)
argglobal
enew
file neo-tree\ filesystem\ \[1]
balt /mnt/c/projects/TP_GenieLog/projet_GL/app/routes/calendar_router.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
wincmd w
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 35 - ((34 * winheight(0) + 28) / 57)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 35
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("/mnt/c/projects/TP_GenieLog/projet_GL/app/routes/auth.py", ":p")) | buffer /mnt/c/projects/TP_GenieLog/projet_GL/app/routes/auth.py | else | edit /mnt/c/projects/TP_GenieLog/projet_GL/app/routes/auth.py | endif
if &buftype ==# 'terminal'
  silent file /mnt/c/projects/TP_GenieLog/projet_GL/app/routes/auth.py
endif
balt /mnt/c/projects/TP_GenieLog/projet_GL/app/routes/calendar_router.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 30 - ((29 * winheight(0) + 28) / 57)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 30
normal! 020|
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 30 + 118) / 236)
exe 'vert 2resize ' . ((&columns * 86 + 118) / 236)
exe 'vert 3resize ' . ((&columns * 118 + 118) / 236)
tabnext 1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
