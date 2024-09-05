#!/bin/bash

# プロジェクトディレクトリを取得
DIR="$(cd "$(dirname "$0")" && pwd)/pygpt"  # pygptディレクトリを含む

# シェルの初期化ファイルを検出
if [ -n "$BASH_VERSION" ]; then
    PROFILE_FILE="$HOME/.bash_profile"
elif [ -n "$ZSH_VERSION" ]; then
    PROFILE_FILE="$HOME/.zshrc"
else
    echo "Unsupported shell. Please manually add $DIR/bin to your PATH."
    exit 1
fi

# PATH を追加
if ! grep -q "$DIR/bin" "$PROFILE_FILE"; then
    echo 'export PATH="'"$DIR"'/bin:$PATH"' >> "$PROFILE_FILE"
fi

# 変更を反映
source "$PROFILE_FILE"

echo "Installation complete. Please restart your terminal or run 'source $PROFILE_FILE' to apply changes."
