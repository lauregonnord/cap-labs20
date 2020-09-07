Remote work on ENSL machines
Laure Gonnord, Sept 2020


# SSH on ENSL machines, Linux version (with your ENSL Account)


* Edit your `.ssh/config` and add the following lines:
```
Host !ssh.ens-lyon.fr *.ens-lyon.fr
ProxyCommand ssh -N -W %h:%p %r@ssh.ens-lyon.fr
```

* now `ssh` on one of the ENSL machines: 

```
ssh mylogin@slsu0-02.dsi-ext.ens-lyon.fr
```
(`slsu0` or `slsu1`, `01` to `20` at least, use `-X` if you want to use a graphical interface remotely).


# Windows version.

* adapt the `mobaxterm` howto from [this page](https://nlouvet.gitlabpages.inria.fr/lifasr5/connec.html) The ssh gateway is `ssh.ens-lyon.fr` and the machine to log on is `slsu[0-1]-...` 

# Mount your ENS account on your laptop (Linux) with SSHFS. 

* I give you in `scripts/mountsinfoens` a script I wrote many years ago, use with caution.
