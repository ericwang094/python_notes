# usr/bin/bash

# https://linuxize.com/post/bash-heredoc/

: '
Here document (Heredoc) is a type of redirection
that allows you to pass multiple lines of input to a command.

* The first line starts with an optional command followed by
  the special redirection operator << and the delimiting identifier.
    * You can use any string as a delimiting identifier,
      the most commonly used are EOF or END.
    * If the delimiting identifier is unquoted,
      the shell will substitute all variables,
      commands and special characters before passing
      the here-document lines to the command.
    * Appending a minus sign to the redirection operator <<-,
      will cause all leading tab characters to be ignored.
      This allows you to use indentation when writing here-documents
      in shell scripts. Leading whitespace characters are not allowed,
      only tab.
'

# param will be substituted
cat << EOF
The current working directory is $PWD
You are logged in as :$(whoami)
EOF

# param will NOT be substituted
cat <<- "EOF"
  The current working directory is $PWD
  You are logged in as :$(whoami)
EOF

