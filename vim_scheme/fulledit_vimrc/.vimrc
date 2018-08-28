filetype plugin indent on
set tabstop=4
set shiftwidth=4
set expandtab

set t_Co=256
colorscheme PaperColor
set cursorline
set cursorcolumn
set background=dark
set number
set laststatus=2
syntax on
set hlsearch
set mouse=a
set bs=2
set ruler
"set nu
set incsearch
set nowrap
set ignorecase
set smartcase
highlight Search cterm=none ctermbg=11 ctermfg=9
"highlight CursorColumn cterm=none ctermbg=110
highlight DiffText cterm=bold ctermbg=202 ctermfg=12
highlight Pmenu cterm=none ctermbg=11
highlight Cursor guifg=white guibg=black
highlight iCursor guifg=white guibg=steelblue
set guicursor=n-v-c:block-Cursor
set guicursor+=i:ver100-iCursor
set guicursor+=n-v-c:blinkon0
set guicursor+=i:blinkwait10
map <F11> :set invpaste<CR>
set pastetoggle=<F11>
set mousemodel=extend
set paste
set nopaste
