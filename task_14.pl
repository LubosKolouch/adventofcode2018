#!/usr/bin/perl 
#===============================================================================
#
#         FILE: task_14_3.pl
#
#        USAGE: ./task_14_3.pl  
#
#  DESCRIPTION: 
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: YOUR NAME (), 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: 12/15/2018 06:01:16 PM
#     REVISION: ---
#===============================================================================

use strict;
use warnings;
use 5.026;
use autodie;


my $goal = shift;

#part 1
my $recipes = '37';
my ($elf1, $elf2) = (0, 1);
while (length $recipes < $goal + 10) {
    my ($value1, $value2) = (substr($recipes, $elf1, 1), substr($recipes, $elf2, 1));
    $recipes .= $value1 + $value2;
    $elf1 = ($elf1 + 1 + $value1) % length $recipes;
    $elf2 = ($elf2 + 1 + $value2) % length $recipes;
}
say 'Part1 :'.substr($recipes, $goal, 10);

#part 2
while (1) {
    if (length($recipes) - length($goal) > 1) {
        pos($recipes) = length($recipes) - length($goal) - 2;
    } else {
        pos($recipes) = 0;
    }

    if ($recipes =~ /$goal/g) {
        say 'Part2: '.$-[0];
        last;
    }

    my ($value1, $value2) = (substr($recipes, $elf1, 1), substr($recipes, $elf2, 1));
    $recipes .= $value1 + $value2;

    $elf1 = ($elf1 + 1 + $value1) % length $recipes;
    $elf2 = ($elf2 + 1 + $value2) % length $recipes;
}

