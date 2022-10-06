syntax on                       "syntax highlighting, see :help syntax
syntax on                       "syntax highlighting, see :help syntax
filetype plugin indent on       "file type detection, see :help filetype
set number                      "display line number
"set relativenumber              "display relative line numbers
set path+=**                    "improves searching, see :help path
set noswapfile                  "disable use of swap files
set wildmenu                    "completion menu
set backspace=indent,eol,start  "ensure proper backspace functionality
"set undodir=~/.cache/nvim/undo  "undo ability will persist after exiting file
"set undofile                    "see :help undodir and :help undofile
set incsearch         
set smartindent                 "auto indent on new lines, see :help smartindent
set ic                          "ignore case when searching
set colorcolumn=80              "display color when line reaches pep8 standards
set expandtab                   "expanding tab to spaces
set tabstop=4                   "setting tab to 4 columns
set shiftwidth=4                "setting tab to 4 columns
set softtabstop=4               "setting tab to 4 columns
set showmatch                   "display matching bracket or parenthesis
set hlsearch incsearch          "highlight all pervious search pattern with incsearch
set mouse=nvi                   "suporte mouse modos normal visual insert
set history=1000                " remember more commands and search history
set scrolloff=4                 " keep three lines between the cursor and the edge of the screen
set laststatus=2                " always slow statusline
set splitright                  "i prefer splitting right and below
set termguicolors " para usar colorschemes
set nowrap
hi ColorColumn ctermbg=9 " display ugly bright red bar at color column number
inoremap jk <ESC>
let g:mapleader="\<Space>"
set timeoutlen=250
nnoremap <leader>1 :tabnext 1<CR>
nnoremap <leader>2 :tabnext 2<CR>
nnoremap <leader>3 :tabnext 3<CR>
nnoremap <leader>4 :tabnext 4<CR>
nnoremap <leader><leader> :

" vim-plug.....................................................................
call plug#begin('~/.config/nvim/plugged') 
" colorschemes
Plug 'josegamez82/starrynight'
Plug 'savq/melange'
" A fuzzy file finder
Plug 'kien/ctrlp.vim'
" mapping hints
Plug 'liuchengxu/vim-which-key'
call plug#end()

" post VimPlug
colorscheme starrynight
" which key
nnoremap <silent> <leader> :WhichKey '<Space>'<CR>

" CtrlP fuzzy finder
nnoremap <leader>p :CtrlP<cr>

" permite abbrs comecando com backslash
set iskeyword+=\

" insert mode abbreviations
" unabbreviate \union
abbreviate \union ∪

" unabbreviate \in
abbreviate \in ∈

" unabbreviate \notin
abbreviate \notin ∉

" unabbreviate \neq
abbreviate \neq ≠

" unabbreviate \wedge
abbreviate \wedge ∧

" unabbreviate \vee
abbreviate \vee ∨

" unabbreviate \comp
abbreviate \comp ∘

" unabbreviate \geq
abbreviate \geq ≥

" unabbreviate \leq
abbreviate \leq ≤

" unabbreviate \alpha
abbreviate \alpha α

" unabbreviate \Alpha
abbreviate \Alpha Α

" unabbreviate \beta
abbreviate \beta β

" unabbreviate \Beta
abbreviate \Beta Β

" unabbreviate \rarrow
abbreviate \rarrow →

" unabbreviate \not
abbreviate \not ¬

" unabbreviate \forall
abbreviate \forall ∀

" unabbreviate \exists
abbreviate \exists ∃

" unabbreviate \implies
abbreviate \implies ⇒

" unabbreviate \cross
abbreviate \cross ⨯
