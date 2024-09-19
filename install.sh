#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)/pygpt"  

if [ -n "$BASH_VERSION" ]; then
    PROFILE_FILE="$HOME/.bash_profile"
elif [ -n "$ZSH_VERSION" ]; then
    PROFILE_FILE="$HOME/.zshrc"
else
    echo "Unsupported shell. Please manually add $DIR/bin to your PATH."
    exit 1
fi

if ! grep -q "$DIR/bin" "$PROFILE_FILE"; then
    echo 'export PATH="'"$DIR"'program/bin:$PATH"' >> "$PROFILE_FILE"
fi

source "$PROFILE_FILE"

echo "インストールが完了しました。"
