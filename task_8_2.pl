#!/usr/bin/perl 
#===============================================================================
#
#         FILE: task_8_2.pl
#
#        USAGE: ./task_8_2.pl
#
#  DESCRIPTION: https://adventofcode.com/2018/day/8
#               second part
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Lubos Kolouch
# ORGANIZATION:
#      VERSION: 1.0
#      CREATED: 12/08/2018 12:36:27 PM
#     REVISION: ---
#===============================================================================

use strict;
use warnings;
use autodie;
use 5.026;
use Data::Dumper;

my @all_data;

sub process_node {

    my $child_count = shift @all_data;
    my $metadata = shift @all_data;

    my @child_total;
    my $child_value = 0;

    for (1 .. $child_count) {
        push @child_total, &process_node;
    }

    # no children nodes
    
    if ($child_count == 0) {
        $child_value += shift @all_data for (1 ..  $metadata);
    } else {
        # children nodes
        for (1..$metadata) {
            my $child = shift @all_data;
            # skip if does not exist
            next if $child > scalar @child_total;

            $child_value += $child_total[ $child - 1 ];
        }

    }
    
    return $child_value;
}

sub main {

    open my $file, '<', 'input8.txt';
    my $str = <$file>;
    close $file;

    @all_data = split / /, $str;

    say &process_node();
    return 1;
}

main;

