---
title: "Restoring manual changes overwritten by a Puppet run"
product: "Red Hat Satellite"
version: "6.19"
guide: "installing_satellite_server_in_a_disconnected_network_environment"
guide_title: "Installing Satellite Server in a disconnected network environment"
chapter_number: "A"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#restoring-manual-changes-overwritten-by-a-puppet-run_satellite"
---
# Appendix A. Restoring manual changes overwritten by a Puppet run

If your manual configuration has been overwritten by a Puppet run, you can restore the files to the previous state.

For example, when you install and configure Satellite for the first time by using `satellite-installer`, you can use the `--foreman-proxy-dns-managed false` and `--foreman-proxy-dhcp-managed false` options to specify that the DNS and DHCP configuration files are not to be managed by Puppet. If you do not use these options during the initial `satellite-installer` run, rerunning `satellite-installer` overwrites all manual changes. The following example shows you how to restore a DHCP configuration file overwritten by a Puppet run.

**Procedure**

1. Copy the file you intend to restore. This allows you to compare the files to check for any mandatory changes required by the upgrade. This is not common for DNS or DHCP services.

   ```
   # cp /etc/dhcp/dhcpd.conf /etc/dhcp/dhcpd.backup
   ```
2. Check the log files to note down the md5sum of the overwritten file. For example:

   ```
   # journalctl -xe
   ...
   /Stage[main]/Dhcp/File[/etc/dhcp/dhcpd.conf]: Filebucketed /etc/dhcp/dhcpd.conf to puppet with sum 622d9820b8e764ab124367c68f5fa3a1
   ...
   ```
3. Restore the overwritten file:

   ```
   # puppet filebucket restore --local --bucket \
   /var/lib/puppet/clientbucket /etc/dhcp/dhcpd.conf \ 622d9820b8e764ab124367c68f5fa3a1
   ```
4. Compare the backup file and the restored file, and edit the restored file to include any mandatory changes required by the upgrade.
