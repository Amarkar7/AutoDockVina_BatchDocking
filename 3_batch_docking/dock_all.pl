### `3_batch_docking/dock_all.pl`

```perl
#!/usr/bin/perl
use strict;
use warnings;

my $receptor = "receptor.pdbqt";  # change as needed
my $config = "config.txt";        # must include gridbox parameters

my @ligands = glob("*.pdbqt");
my $step = 1;

foreach my $ligand (@ligands) {
    print "[", scalar(localtime), "] Step $step: Docking $ligand...\n";
    system("vina --receptor $receptor --ligand $ligand --config $config --log ${ligand}.log");
    print "[", scalar(localtime), "] Step $step DONE: $ligand\n";
    $step++;
}
