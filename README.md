dootdoorlock
============

The new doorlock at DSL 2.0


Install init scripts as root
```
cp init/doord /etc/init.d/
cp init/octopusd /etc/init.d/
chown root:root /etc/init.d/doord
chown root:root /etc/init.d/octopusd
update-rc.d doord defaults
update-rc.d octopusd defaults
```

to add users:
```
Not yet implemented, use web interface for now
```
