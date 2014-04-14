#!/bin/bash
set -e

CHAP=$1

if (($CHAP < 10)); then
    CHAP="chapter_0$CHAP"
else
    CHAP="chapter_$CHAP"
fi

cd $CHAP/superlists
git push -f local $CHAP
if (($# == 2)); then
    git push -f origin $CHAP
fi

cd ../..