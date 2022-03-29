# Claudio Perez
# To install dependencies, run
#
#   pip install quakeio
#

proc quakeSeries {tag file channel args} {
    # Parse options
    array set options {-scale {} -scale 1.0 -quxwoo 1}
    while {[llength $args]} {
        switch -glob -- [lindex "$args" 0] {
            -bar*   {set args [lassign $args - options(-bargle)]}
            -s*     {set args [lassign $args - options(-scale)]}
            -c*     {set args [lassign $args - options(-channel)]}
            -qux*   {set options(-quxwoo) 1 ; set args [lrange $args 1 end]}
            --      {set args [lrange $args 1 end] ; break}
            -*      {error "unknown option [lindex $args 0]"}
            default break
        }
    }
    # Call parser
    array set series [
      exec quakeio -t tcl $file -m station_channel:l=$channel
    ]

	  timeSeries Path $tag -dt $series(dt) -values $series(values)
    return [list $series(shape) $series(dt)]
}

::oo::class create ResponseHistory {
    variable dt 
    variable algorithm
    variable current_series_tag
    variable current_pattern_tag
    variable num_steps
    variable dt

    constructor {args} {
        set current_pattern_tag 1
        set current_series_tag 1
        set num_steps 0
        set dt 0

        set algorithm Newton
        
        set Tol				  1.0e-8;
        set maxNumIter	100;
        set printFlag		0;
        set TestType		EnergyIncr;
        test $TestType $Tol $maxNumIter $printFlag;
        
        numberer RCM;

        #                  gamma  beta
        integrator Newmark 0.50   0.25 
    }

    method pattern {args} {
        switch -glob -- [lindex "$args" 0] {
            UniformQuake  {
              set args [lassign $args - dof]
              lassign [opensees::lib::quakeSeries $current_series_tag {*}$args] num_steps dt
              pattern UniformExcitation $current_pattern_tag $dof -accel $current_series_tag
              incr current_pattern_tag
              incr current_series_tag
            }
            "#*" {}
            "" {}
            * {puts "unknown option [lindex $args 0]"}
            default break
      }
    }

    method patterns {pats} {
      foreach pat [split $pats "\n"] {my pattern {*}$pat}
    }

    method analyze {{n 0}} {
      if {!$n} {set n $num_steps}
      puts "analyzing $n steps"
      analysis Transient;
      for {set ik 1} {$ik <= $n} {incr ik 1} {
          if {[my step] != 0} {return $ik}
      }
    }

    method step {} {
      foreach alg "
        $algorithm
        {NewtonLineSearch -type Bisection}
        {NewtonLineSearch -type Secant}
        {NewtonLineSearch -type RegulaFalsi}
        KrylovNewton
        Broyden
        BFGS
      " {
        algorithm {*}$alg
        if {[set ok [analyze 1 $dt]] == 0} {
          algorithm $algorithm; break
        }
      }
        return $ok
    }
}


