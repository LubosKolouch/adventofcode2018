#!/usr/bin/perl
#===============================================================================
#
#         FILE: task_13_1.pl
#
#        USAGE: ./task_13_1.pl
#
#  DESCRIPTION: www.adventofcode.com/2018/day/13 part 1
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: YOUR NAME (),
# ORGANIZATION:
#      VERSION: 1.0
#      CREATED: 12/13/2018 06:35:28 PM
#     REVISION: ---
#===============================================================================

use strict;
use warnings;
use 5.026;
use autodie;

use Data::Dumper;

my $input = shift;
my %field;

# load initial field

my $x = -1;
my $v_count;
my %vehs;
my $maxx = 0;
my $maxy = 0;

sub detect_collisions {

    my %coord;

    for ( keys %vehs ) {
        my $c = $vehs{$_}{y} . ' ' . $vehs{$_}{x};
        if ( defined $coord{$c} ) {
            delete $vehs{$coord{$c}};
            delete $vehs{$_};
        } else {
           $coord{$c} = $_;
        }

    }

    return 1;
}

sub is_vehicle {
    my ( $x, $y ) = @_;

    for ( keys %vehs ) {
        return $_ if $vehs{$_}{x} == $x and $vehs{$_}{y} == $y;
    }

    return 0;
}

sub print_field {

    for my $x ( 0 .. $maxx ) {
        for my $y ( 0 .. $maxy ) {
            if ( my $v = is_vehicle( $x, $y ) ) {

                # print $vehs{$v}{shape};
                print $v;
            }
            else {
                print $field{$x}{$y};
            }
        }
        #say '';
    }
}

open my $file, '<', $input;

# load field
while (<$file>) {
    chomp;

    my $str = $_;
    $x++;
    for my $y ( 0 .. length($str) - 1 ) {
        $field{$x}{$y} = substr $str, $y, 1;
        $maxx = $x if $x > $maxx;
        $maxy = $y if $y > $maxy;

        if ( $field{$x}{$y} =~ /[><\^v]/ ) {
            $v_count++;
            $vehs{$v_count}{x}     = $x;
            $vehs{$v_count}{y}     = $y;
            $vehs{$v_count}{shape} = $field{$x}{$y};
            $vehs{$v_count}{turns} = 0;
        }
    }
}

warn Dumper \%vehs;
my $steps = 0;

while (1) {

    if (scalar keys %vehs == 1) {
        say 'last vehicle remaining';
        for (keys %vehs) {
            say "vehicle $_ x ".$vehs{$_}{x}." y ".$vehs{$_}{y};
            say "solution $y $x";
            die;
        }
    }

    #say scalar keys %vehs;
    $steps++;
    #say "step $steps";
    my %moved;

    for my $x ( 0 .. $maxx ) {
        for my $y ( 0 .. $maxy ) {

            my $v = is_vehicle( $x, $y );
            next unless $v;
            next if $moved{$v};
            $moved{$v} = 1;

            #say "vehicle $v shape " . $vehs{$v}{shape} . " x " . $vehs{$v}{x} . " y " . $vehs{$v}{y};

            if ( $vehs{$v}{shape} eq '>' ) {
                #say "to >";

                # >\
                if ( $field{ $vehs{$v}{x} }{ $vehs{$v}{y} } eq '\\' ) {
                    $vehs{$v}{x}++;
                    $vehs{$v}{shape} = 'v';
                }

                # >/
                elsif ( $field{ $vehs{$v}{x} }{ $vehs{$v}{y} } eq '/' ) {
                    $vehs{$v}{x}--;
                    $vehs{$v}{shape} = '^';
                }

                # >+
                elsif ( $field{ $vehs{$v}{x} }{ $vehs{$v}{y} } eq '+' ) {
                    $vehs{$v}{turns}++;

                    if ( $vehs{$v}{turns} % 3 == 1 ) {

                        # >+ left
                        $vehs{$v}{x}--;
                        $vehs{$v}{shape} = '^';
                    }
                    elsif ( $vehs{$v}{turns} % 3 == 0 ) {

                        # >+ right
                        $vehs{$v}{x}++;
                        $vehs{$v}{shape} = 'v';
                    } else {
                        $vehs{$v}{y}++;
                    }

                }

                else {
                    $vehs{$v}{y}++;
                }

            }

            elsif ( $vehs{$v}{shape} eq '<' ) {
                #say "to <";
                if ( $field{ $vehs{$v}{x} }{ $vehs{$v}{y} } eq '\\' ) {

                    # \<
                    $vehs{$v}{x}--;
                    $vehs{$v}{shape} = '^';
                }
                elsif ( $field{ $vehs{$v}{x} }{ $vehs{$v}{y} } eq '/' ) {

                    # /<
                    $vehs{$v}{x}++;
                    $vehs{$v}{shape} = 'v';
                }
                elsif ( $field{ $vehs{$v}{x} }{ $vehs{$v}{y} } eq '+' ) {
                    $vehs{$v}{turns}++;

                    # +<

                    if ( $vehs{$v}{turns} % 3 == 1 ) {

                        # +< left
                        $vehs{$v}{x}++;
                        $vehs{$v}{shape} = 'v';
                    }
                    elsif ( $vehs{$v}{turns} % 3 == 0 ) {

                        # +< right
                        $vehs{$v}{x}--;
                        $vehs{$v}{shape} = '^';
                    } else {
                        $vehs{$v}{y}--;
                    }
                }
                else {
                    $vehs{$v}{y}--;
                }

            }

            elsif ( $vehs{$v}{shape} eq '^' ) {
                #say "to ^";
                if ( $field{ $vehs{$v}{x} }{ $vehs{$v}{y} } eq '\\' ) {

                    # \
                    # ^
                    #say "found \\";
                    $vehs{$v}{y}--;
                    $vehs{$v}{shape} = '<';
                }
                elsif ( $field{ $vehs{$v}{x} }{ $vehs{$v}{y} } eq '/' ) {

                    # /
                    # ^
                    #say "found /";
                    $vehs{$v}{y}++;
                    $vehs{$v}{shape} = '>';
                }
                elsif ( $field{ $vehs{$v}{x} }{ $vehs{$v}{y} } eq '+' ) {
                    $vehs{$v}{turns}++;
                    #say "found +";

                    if ( $vehs{$v}{turns} % 3 == 1 ) {

                        # + left
                        # ^
                        $vehs{$v}{y}--;
                        $vehs{$v}{shape} = '<';
                    }
                    elsif ( $vehs{$v}{turns} % 3 == 0 ) {

                        # + right
                        # ^
                        $vehs{$v}{y}++;
                        $vehs{$v}{shape} = '>';
                    } else {
                        $vehs{$v}{x}--;
                    }
                }

                else {
                    #say "moving up";
                    $vehs{$v}{x}--;
                }

            }
            elsif ( $vehs{$v}{shape} =~ /v/msx ) {
                #say "to v";
                if ( $field{ $vehs{$v}{x} }{ $vehs{$v}{y} } eq '\\' ) {

                    # v
                    # \
                    $vehs{$v}{y}++;
                    $vehs{$v}{shape} = '>';
                }
                elsif ( $field{ $vehs{$v}{x} }{ $vehs{$v}{y} } eq '/' ) {

                    # v
                    # /
                    $vehs{$v}{y}--;
                    $vehs{$v}{shape} = '<';
                }
                elsif ( $field{ $vehs{$v}{x} }{ $vehs{$v}{y} } eq '+' ) {
                    $vehs{$v}{turns}++;

                    if ( $vehs{$v}{turns} % 3 == 1 ) {

                        # v
                        # + left
                        $vehs{$v}{y}++;
                        $vehs{$v}{shape} = '>';
                    }
                    elsif ( $vehs{$v}{turns} % 3 == 0 ) {

                        # v
                        # + right
                        $vehs{$v}{y}--;
                        $vehs{$v}{shape} = '<';
                    } else {
                        $vehs{$v}{x}++;
                    }

                }

                else {
                    $vehs{$v}{x}++;
                }

            }
            detect_collisions();

        }

    }

    #    print_field;

    #            warn Dumper \%vehs;
}
