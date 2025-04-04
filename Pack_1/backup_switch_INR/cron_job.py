entry backup {
    if {
        day-of-week friday
        time-of-day 14:30
    } then {
        run script backup_sw.py
    }
}
print()