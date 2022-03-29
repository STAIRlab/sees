package provide opensees 0.1
package require Tcl 8.6

# Create the namespace
namespace eval ops {
  namespace export lib ResponseHistory quakeSeries
  namespace eval lib {
    # Export commands
    namespace export ResponseHistory quakeSeries

    source ResponseHistoryLib.tcl
  }

}

