#! /bin/bash
# Michael Stergianis 100568134

cat $3 | tail -n +$1 | head -n -$2
