dootdoorlock
============

The new doorlock at DSL - William Liang's DOOT from BOOT

On the pi, copy "doord" to /etc/init.d/

To enable at boot:
```
sudo update-rc.d doord defaults
```
For some reason this does not work. Neither does starting in ```/etc/rc.local```.

daemon control:
```
sudo /etc/init.d/doord {start, stop, restart}
```

to add users:
```
./door add
```

To announce entrances to Twitter, save the oauth credentials to `./api.cfg`

dependencies: pyserial, zdaemon
