from .ast import Tag, Num, Int

series = LibCmd("timeSeries")

Linear = series("Linear"
    # timeSeries Linear $tag <-factor $cFactor>
    about="This command is used to construct a `TimeSeries` object" \
          "in which the load factor applied is linearly proportional " \
          r"to the time in the domain, i.e. \n\n$$\lambda(t) = C*t$$\n"
    args = [
        Tag(about="unique tag among TimeSeries objects."),
        Num("fact", about="the linear factor (optional)", default=1.0)
    ]
)
