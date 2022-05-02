
import sys

HELP = """
usage: eigen <model> [num-modes] [outfile]
"""


eigenvalue_analysis = r"""
proc write_modes {mode_file nmodes} {
  if {$mode_file == 1} {
    proc print {str} {puts $str}
  } else {
    set fid_modes [open $mode_file w+]
    proc print {str} "puts $fid_modes \$str"
  }

  #print "{"
  for {set m 1} {$m <= $nmodes} {incr m} {
    print "$m:"
    foreach n [getNodeTags] {
      print "  $n: \[[join [nodeEigenvector $n $m] {, }]\]";
    }
  }
  if {$mode_file != 1} {
    close $fid_modes
  }
  # print "}"
}

::oo::class create EigenvalueAnalysis {
  #============================================================
  # Eigenvalue analysis
  # This class orchestrates an eigenvalue analysis using OpenSees 
  #
  # Claudio Perez
  # Summer 2021
  # OpenSees version 3.3.0
  #============================================================
  constructor { } {
  }

  method analyze {args} {
    array set options {-numModes 1 -file 1 -system {} -verbose 0}
    while {[llength $args]} {
        switch -glob -- [lindex "$args" 0] {
            -file   {set args [lassign $args - options(-file)]}
            -v*     {set options(-verbose) 1 ; set args [lrange $args 1 end]}
            --      {set args [lrange $args 1 end] ; break}
            -*      {error "unknown option [lindex $args 0]"}
            *       {set args [lassign $args options(-numModes)]}
            default break
        }
    }

    # Constant parameters.
    set verbose  1
    set PI       3.1415159
    set DOFs     {1 2 3 4 5 6}
    set nodeList [getNodeTags]
    # Initialize variables `omega`, `f` and `T` to
    # empty lists.
    foreach {omega f T recorders} {{} {} {} {}} {} 

    for {set k 1} {$k <= $options(-numModes)} {incr k} {
      lappend recorders [recorder Node -node {*}$nodeList -dof {*}$DOFs "eigen $k";]
    }

    set eigenvals [eigen $options(-numModes)];

    set T_scale 1.0
    foreach eig $eigenvals {
      lappend omega [expr sqrt($eig)];
      lappend f     [expr sqrt($eig)/(2.0*$PI)];
      lappend T     [expr $T_scale*(2.0*$PI)/sqrt($eig)];
    }

    # print info to `stdout`.
    if {$options(-verbose)} {
      puts "Angular frequency (rad/s): $omega\n";
      puts "Frequency (Hz):            $f\n";
      puts "Periods (sec):             $T\n";
    }


    write_modes $options(-file) $options(-numModes)

    foreach recorder $recorders {
      remove recorder $recorder
    }
  }
}
"""

def modes(*argv):
    args = []
    argi = iter(argv)
    #next(argi)

    script = sys.stdin.read() + eigenvalue_analysis + f"""
    EigenvalueAnalysis create ea; 
    """
    op = None
    for arg in argi:
        if arg == "-S": # script-generation mode
            op = print
        elif arg in ["-h", "--help"]:
            print(HELP)
            sys.exit()
        else:
            args.append(arg)

    args = [*args, *argi]

    if op is None: # default to execution mode
        import opensees.tcl
        op = opensees.tcl.eval

    op(script + f"ea analyze {' '.join(args)}")

def eigen(num):
    import opensees.tcl
    opensees.tcl.eval(sys.stdin.read() + f"""
    set PI       3.1415159
    set eigenvals [eigen {num}];

    set T_scale 1.0
    foreach eig $eigenvals {{
      lappend omega [expr sqrt($eig)];
      lappend f     [expr sqrt($eig)/(2.0*$PI)];
      lappend T     [expr $T_scale*(2.0*$PI)/sqrt($eig)];
    }}

    puts "Angular frequency (rad/s): $omega\n";
    puts "Frequency (Hz):            $f\n";
    puts "Periods (sec):             $T\n";
    """)

if __name__ == "__main__":

    modes(*sys.argv)

