
entry backup {
    if {
        day-of-week thursday
        time-of-day 13:50
    } then {
        run script backup_sw.py
    }
}
