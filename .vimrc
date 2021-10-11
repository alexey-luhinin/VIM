"=====================================================
"" GENERAL SETTINGS
"=====================================================

set nocompatible 			" Be IMPROVED
set ttyfast                 " terminal acceleration

" enable syntax and plugins
syntax enable
filetype plugin on

" Display line numbers and relative numbers
set nu
set rnu

" set 256 colors, needs for tmux support
set t_Co=256                                

" Search options
set incsearch	  			" incremental search
set hlsearch	  			" highlight search results
set ignorecase    			" ignorecase search

" Cursorline
set cursorline

" Swapfiles off
set noswapfile 	  			" no swap files

" Undo file
set undofile
set undodir=~/.vim/undodir

" Open splits down
set splitbelow

" Save buffer is changed but is not saved
set autowriteall

" Shows matching part of bracket pairs (), [], {}
set showmatch                               

" Tab shortcut configs
set tabstop=4                           " 4 whitespaces for tabs visual presentation
set shiftwidth=4                        " shift lines by 4 spaces
set smarttab                            " set tabs for a shifttabs logic
set expandtab                           " expand tabs into spaces
set autoindent                          " indent when moving to the next line while

"=====================================================
"" PLUGINS
"=====================================================

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" PUT PLUGINS DOWN

Plugin 'python-mode/python-mode' 	" Vim python-mode. PyLint, Rope, Pydoc, breakpoints from box
Plugin 'ervandew/supertab'       	" Perform all your vim insert mode completions with Tab
Plugin 'morhetz/gruvbox'         	" Retro groove color scheme for Vim
Plugin 'vim-airline/vim-airline' 	" Lean & mean status/tabline for vim that's light as air
Plugin 'scrooloose/nerdcommenter'	" Vim plugin for intensely nerdy commenting powers
Plugin 'tpope/vim-surround'      	" Quoting/parenthesizing made simple
Plugin 'airblade/vim-gitgutter'  	" A Vim plugin which shows git diff markers in the sign column and stages/previews/undoes hunks
Plugin 'edkolev/tmuxline.vim'    	" Simple tmux statusline generator with support for powerline symbols and statusline / airline
Plugin 'scrooloose/nerdtree'     	" A tree explorer plugin for vim
Plugin 'kien/ctrlp.vim'    	 	    " Fuzzy file, buffer, mru, tag, etc finder
Plugin 'majutsushi/tagbar' 		    " Vim plugin that displays tags in a window, ordered by scope
Plugin 'tpope/vim-fugitive' 		" Fugitive.vim: A Git wrapper so awesome, it should be illegal
Plugin 'davidhalter/jedi-vim' 		" Using the jedi autocompletion library for VIM


" PUT PLUGINS UP

call vundle#end()            		" required
filetype plugin indent on    		" required

"=====================================================
"" PLUGINS CONFIGURATION
"=====================================================

" NERDTREE
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>

" Ignore files in NERDTree
let NERDTreeIgnore=['\.pyc$', '\.pyo$', '__pycache__$', 'requirements.txt', 'venv']     

" TAGBAR
nmap <F7> :TagbarToggle<CR>
nmap <F8> :TagbarOpenAutoClose<CR>

" Pymode
let g:pymode_doc = 0
let g:pymode_rope_completion = 0
let g:pymode_rope_complete_on_dot = 0
let g:pymode_breakpoint = 1

"=====================================================
"" THEME
"=====================================================

colorscheme gruvbox
set bg=dark

"=====================================================
"" MAPS
"=====================================================

" leader
let mapleader = ","

" tree
nmap <Leader>/ :!clear;tree -I "__pycache__\|venv"<CR>

" find
nmap <Leader>f :find 

" Buffers
nmap <Right> :bn<CR>
nmap <Left> :bp<CR>
nmap <Down> :bd<CR>
nmap <UP> :buffers<CR>

" Open new buffer with VIMRC configuration
nmap <F12> :e ~/.vimrc<CR>

" Map for switching windows
nnoremap <c-h> <c-w>h
nnoremap <c-l> <c-w>l
nnoremap <c-j> <c-w>j
nnoremap <c-k> <c-w>k

" Terminal
nnoremap <Leader>t :term<CR>

" Run in PDB
nnoremap <Leader>pdb :term python -m pdb %

" Clear highlights after search
nnoremap // :nohl<CR>

" Move to next/previous method
map <leader>] ]m
map <leader>[ [m

"=====================================================
"" FINDING FILES
"=====================================================

" Search down into subfolders
" Provides tab-completion for all file-related tasks
set path+=**

" Display all matching files when we tab complete
set wildmenu
set wildmode=longest:full,full

" Wild Ignores
set wildignore+=**/venv/**
set wildignore+=**/__pycache__/**

" HOW WE CAN:
" - Hit tab to :find by partial match
" - Use * to make it fuzzy

" - :b lets you autocomplete any open buffer

"=====================================================
"" TAG JUMPING
"=====================================================

" Create the 'tags' file (may need to install ctags first)
command! MakeTags !ctags -R .

" HOW WE CAN:
" - Use ^] to jump to tag under cursor
" - Use g^] for ambiguous tags
" - Use ^t to jump back up the tag stack
"
"
"=====================================================
"" AUTOCOMPLETION
"=====================================================

" Completion can be done for:

" 1. Whole lines						                |i_CTRL-X_CTRL-L|
" 2. keywords in the current file				        |i_CTRL-X_CTRL-N|
" 3. keywords in 'dictionary'					        |i_CTRL-X_CTRL-K|
" 4. keywords in 'thesaurus', thesaurus-style			|i_CTRL-X_CTRL-T|
" 5. keywords in the current and included files			|i_CTRL-X_CTRL-I|
" 6. tags							                    |i_CTRL-X_CTRL-]|
" 7. file names							                |i_CTRL-X_CTRL-F|
" 8. definitions or macros					            |i_CTRL-X_CTRL-D|
" 9. Vim command-line						            |i_CTRL-X_CTRL-V|
" 10. User defined completion				            |i_CTRL-X_CTRL-U|
" 11. omni completion						            |i_CTRL-X_CTRL-O|
" 12. Spelling suggestions					            |i_CTRL-X_s|
" 13. keywords in 'complete'				            |i_CTRL-N| |i_CTRL-P|		
"

"=====================================================
"" FILE BROWSING
"=====================================================

" Tweak for browsing
let g:netrw_banner=0 			" disable annoying banner
let g:netrw_browse_split=4		" open in prior window
let g:netrw_altv=1			" open splits to the right
let g:netrw_liststyle=3			" tree view
let g:netrw_list_hide=netrw_gitignore#Hide()
let g:netrw_list_hide.=',\(^\|\s\s\)\zs\.\S\+'

" NOW WE CAN
" - :edit a folder to open a file browser
" - <CR>/v/t to open in an h-split/v-split/tab
" - check |netrw-browse_maps| for more mappings


"=====================================================
"" SNIPPETS
"=====================================================
