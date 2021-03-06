# To the extent possible under law, the author(s) have dedicated all
# copyright and related and neighboring rights to this software to the
# public domain worldwide. This software is distributed without any warranty.
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software.
# If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.

# ~/.bashrc: executed by bash(1) for interactive shells.

# The copy in your home directory (~/.bashrc) is yours, please
# feel free to customise it to create a shell
# environment to your liking.  If you feel a change
# would be benifitial to all, please feel free to send
# a patch to the msys2 mailing list.

# User dependent .bashrc file

# If not running interactively, don't do anything
[[ "$-" != *i* ]] && return

# Shell Options
#
# See man bash for more options...
#
# Don't wait for job termination notification
# set -o notify
#
# Don't use ^D to exit
# set -o ignoreeof
#
# Use case-insensitive filename globbing
# shopt -s nocaseglob
#
# Make bash append rather than overwrite the history on disk
# shopt -s histappend
#
# When changing directory small typos can be ignored by bash
# for example, cd /vr/lgo/apaache would find /var/log/apache
# shopt -s cdspell

# Completion options
#
# These completion tuning parameters change the default behavior of bash_completion:
#
# Define to access remotely checked-out files over passwordless ssh for CVS
# COMP_CVS_REMOTE=1
#
# Define to avoid stripping description in --option=description of './configure --help'
# COMP_CONFIGURE_HINTS=1
#
# Define to avoid flattening internal contents of tar files
# COMP_TAR_INTERNAL_PATHS=1
#
# Uncomment to turn on programmable completion enhancements.
# Any completions you add in ~/.bash_completion are sourced last.
# [[ -f /etc/bash_completion ]] && . /etc/bash_completion

# History Options
#
# Don't put duplicate lines in the history.
# export HISTCONTROL=$HISTCONTROL${HISTCONTROL+,}ignoredups
#
# Ignore some controlling instructions
# HISTIGNORE is a colon-delimited list of patterns which should be excluded.
# The '&' is a special pattern which suppresses duplicate entries.
# export HISTIGNORE=$'[ \t]*:&:[fb]g:exit'
# export HISTIGNORE=$'[ \t]*:&:[fb]g:exit:ls' # Ignore the ls command as well
#
# Whenever displaying the prompt, write the previous line to disk
# export PROMPT_COMMAND="history -a"

# Aliases
#
# Some people use a different file for aliases
# if [ -f "${HOME}/.bash_aliases" ]; then
#   source "${HOME}/.bash_aliases"
# fi
#
# Some example alias instructions
# If these are enabled they will be used instead of any instructions
# they may mask.  For example, alias rm='rm -i' will mask the rm
# application.  To override the alias instruction use a \ before, ie
# \rm will call the real rm not the alias.
#
# Interactive operation...
# alias rm='rm -i'
# alias cp='cp -i'
# alias mv='mv -i'
#
# Default to human readable figures
# alias df='df -h'
# alias du='du -h'
#
# Misc :)
alias less='less -r'                          # raw control characters
alias whence='type -a'                        # where, of a sort
alias grep='grep --color'                     # show differences in colour
alias egrep='egrep --color=auto'              # show differences in colour
alias fgrep='fgrep --color=auto'              # show differences in colour
#
# Some shortcuts for different directory listings
alias ls='ls -h --color=tty'                 # classify files in colour
#alias ls='ls -hF'                 # classify files in colour
alias dir='ls --color=auto --format=vertical'
alias dirs='dirs -v'
alias vdir='ls --color=auto --format=long'
alias ll='ls -l'                              # long list
alias la='ls -la'                              # all but . and ..
alias l='ls -CF'                              #
alias us='export LANG=en_US.UTF-8'
alias jp='export LANG=ja_JP.UTF-8'
alias euc='export LANG=ja_JP.eucJP'
alias sjis='export LANG=ja_JP.sjis'

alias wget='wget -e HTTPS_PROXY=http://goproxy.micron.com:8080'

# alias for git
alias gs='git status'
alias gls='git ls-files'
alias gcommit='git commit -a'
alias gupload='git push origin master'


#alias e="${primary_dir}/Editor/sakura/sakura.exe"
alias e="micro"
alias kate="${primary_dir}/Editor/sakura/sakura.exe"
alias edit="${primary_dir}/Editor/sakura/sakura.exe"
alias ee="${base_dir}/Program/Atom/atom.exe"
alias e1="${base_dir}/Program/Atom/atom.exe"
alias eee="${base_dir}/Program/SublimeText3/sublime_text.exe"
alias e2="${base_dir}/Program/SublimeText3/sublime_text.exe"
alias e3="${base_dir}/Program/VSCode/Code.exe"
#alias open='explorer.exe `cygpath -a -m $PWD` &'
#alias open="explorer.exe $PWD &"
alias mklink="cmd.exe /c mklink"
alias ..='cd ..'
#alias path='echo -e ${PATH//:/\\n}'
alias path='echo $PATH | tr ":" "\n"'
alias grep='grep --color'
alias bindkey="bind -p | egrep -v '^#|self-insert|do-lowercase-version|digit-argument'"

alias j=". j"

bind '"\C-o": history-search-forward'
bind '"\C-p": history-search-backward'
bind '"\C-w": backward-kill-word'  # default: unix-word-rubout


export conemu_dir=`cygpath -u $ConEmuWorkDir`
export base_dir="$CMDER_ROOT/../../"
export primary_dir="$CMDER_ROOT/../../Primary"


#
# set path
#
export PATH=.:$PATH
export PATH=$CMDER_ROOT/tool/bin:~/bin:$PATH
export PATH=$CMDER_ROOT/../msys64/usr/bin:$PATH
export PATH=$primary_dir/Tool/7zip/App/7-Zip64:$PATH
if [ -d "/C/MTApps" ]; then
  export PATH=/C/MTApps/PERL/5.10.0/Prod/Bin:$PATH
else
  export PATH=$base_dirs/PERL/Bin:$PATH
fi

export PATH=$base_dir/Program/python3:$base_dir/Program/python3/Scripts:$PATH
#export PATH=$base_dir/Program/python27:$base_dir/Program/python27/Scripts:$PATH
export MSYS=winsymlinks:nativestrict   # use symbolic link (need to be admin)


#
# Prompt setting
#

# http://tm.root-n.com/unix:command:git:bash_prompt
#
#if [ -f ~/bin/git-completion.bash ]; then
#    source ~/bin/git-completion.bash
#fi
#if [ -f ~/bin/git-prompt.sh ]; then
#    source ~/bin/git-prompt.sh
#fi
#GIT_PS1_SHOWDIRTYSTATE=true
#GIT_PS1_SHOWUNTRACKEDFILES=true
#GIT_PS1_SHOWSTASHSTATE=true
#GIT_PS1_SHOWUPSTREAM=auto

#PS1="\[\e[1;34m\][\W/] \$ \[\e[0;37m"
PS1="\[\e[1;34m\][\w/] \$ \[\e[0;37m"
#PS1="\[\033[1;32m\]\$(date +%Y/%m/%d_%H:%M:%S)\[\033[0m\] \[\033[33m\]\H:\w\n\[\033[0m\][\u@ \W]\[\033[36m\]\$(__git_ps1)\[\033[00m\]\$ "

#promps



# if not defined $USERDNSDOMAIN - micron environment
if [ ! -z "${USERDNSDOMAIN+x}" ]; then # VARが定義済み(nullを含む)の場合 x が返るので、-z でテストすれば OK
  export HTTP_PROXY='http://goproxy.micron.com:8080'
  export HTTPS_PROXY='http://goproxy.micron.com:8080'
  export FTP_PROXY='http://goproxy.micron.com:8080'
fi


#export common_dir="C:\\Utility"
#export conemu_dir=${ConEmuWorkDir//\\/\/}    # replace "\" -> "/"
#export conemu_dir=/c${conemu_dir#*:}            # remove ":"


#
# pathの重複を削除
# http://qiita.com/key-amb/items/ce39b0c85b30888e1e3b
#
_path=""
for _p in $(echo $PATH | tr ':' ' '); do
  case ":${_path}:" in
    *:"${_p}":* )
      ;;
    * )
      if [ "$_path" ]; then
        _path="$_path:$_p"
      else
        _path=$_p
      fi
      ;;
  esac
done
PATH=$_path
unset _p
unset _path


#
# prompt for git
#
function parse_git_branch {
    git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

function promps {
    # 色は気分で変えたいかもしれないので変数宣言しておく
    local  BLUE="\[\e[1;34m\]"
    local  RED="\[\e[1;31m\]"
    local  GREEN="\[\e[1;32m\]"
    local  WHITE="\[\e[00m\]"
    local  GRAY="\[\e[1;37m\]"

    case $TERM in
        xterm*) TITLEBAR='\[\e]0;\W\007\]';;
        *)      TITLEBAR="";;
    esac
    local BASE="\u@\h"
    #PS1="${TITLEBAR}${GREEN}${BASE}${WHITE}:${BLUE}\W${GREEN}\$(parse_git_branch)${BLUE}\$${WHITE} "
    PS1="${BLUE}[\w/]${GREEN}\$(parse_git_branch)${BLUE}\$ ${GRAY}"
}




# Umask
#
# /etc/profile sets 022, removing write perms to group + others.
# Set a more restrictive umask: i.e. no exec perms for others:
# umask 027
# Paranoid: neither group nor others have any perms:
# umask 077

# Functions
#
# Some people use a different file for functions
# if [ -f "${HOME}/.bash_functions" ]; then
#   source "${HOME}/.bash_functions"
# fi
#
# Some example functions:
#
# a) function settitle
# settitle ()
# {
#   echo -ne "\e]2;$@\a\e]1;$@\a";
# }
#
# b) function cd_func
# This function defines a 'cd' replacement function capable of keeping,
# displaying and accessing history of visited directories, up to 10 entries.
# To use it, uncomment it, source this file and try 'cd --'.
# acd_func 1.0.5, 10-nov-2004
# Petar Marinov, http:/geocities.com/h2428, this is public domain
# cd_func ()
# {
#   local x2 the_new_dir adir index
#   local -i cnt
#
#   if [[ $1 ==  "--" ]]; then
#     dirs -v
#     return 0
#   fi
#
#   the_new_dir=$1
#   [[ -z $1 ]] && the_new_dir=$HOME
#
#   if [[ ${the_new_dir:0:1} == '-' ]]; then
#     #
#     # Extract dir N from dirs
#     index=${the_new_dir:1}
#     [[ -z $index ]] && index=1
#     adir=$(dirs +$index)
#     [[ -z $adir ]] && return 1
#     the_new_dir=$adir
#   fi
#
#   #
#   # '~' has to be substituted by ${HOME}
#   [[ ${the_new_dir:0:1} == '~' ]] && the_new_dir="${HOME}${the_new_dir:1}"
#
#   #
#   # Now change to the new dir and add to the top of the stack
#   pushd "${the_new_dir}" > /dev/null
#   [[ $? -ne 0 ]] && return 1
#   the_new_dir=$(pwd)
#
#   #
#   # Trim down everything beyond 11th entry
#   popd -n +11 2>/dev/null 1>/dev/null
#
#   #
#   # Remove any other occurence of this dir, skipping the top of the stack
#   for ((cnt=1; cnt <= 10; cnt++)); do
#     x2=$(dirs +${cnt} 2>/dev/null)
#     [[ $? -ne 0 ]] && return 0
#     [[ ${x2:0:1} == '~' ]] && x2="${HOME}${x2:1}"
#     if [[ "${x2}" == "${the_new_dir}" ]]; then
#       popd -n +$cnt 2>/dev/null 1>/dev/null
#       cnt=cnt-1
#     fi
#   done
#
#   return 0
# }
#
# alias cd=cd_func



#
# 下記でシンボリックリンクがネットワークドライブに使えるか調べられる。(admin権限必要)
#
# > fsutil behavior query symlinkevaluation
# ローカルからローカルへのシンボリック リンクは有効です。
# ローカルからリモートへのシンボリック リンクは有効です。
# リモートからローカルへのシンボリック リンクは無効です。
# リモートからリモートへのシンボリック リンクは無効です。
#
# 上記で下記２つが無効の場合は下記コマンドで有効にできる。
# fsutil behavior set symlinkevaluation r2r:1 r2l:1
#
