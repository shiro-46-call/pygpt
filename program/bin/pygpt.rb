# coding: utf-8
HOMEBREW_NULETE_VERSION = "0.1.0"

class Pygpt < Formula
    desc "A tool that executes the input Python program and when an error occurs, ChatGPT will tell you the error analysis results and how to fix it."
    homepage "https://github.com/tamadalab/pygpt"
    license "MIT License"
    url "https://github.com/tamadalab/pygpt/releases/download/v#{HOMEBREW_NULETE_VERSION}/pygpt-#{HOMEBREW_NULETE_VERSION}-darwin-amd64.tar.gz"
    version HOMEBREW_NULETE_VERSION
    sha256 "7d7ade1cb4cf9ce6ce45593e5ad1089af09c375f30ccf17e40bd80cb3c4de893"

    def install
    prefix.install "README.md"
    prefix.install "LICENSE"
    prefix.install "doc"
    bin.install "bin/pygpt"
    end
end
