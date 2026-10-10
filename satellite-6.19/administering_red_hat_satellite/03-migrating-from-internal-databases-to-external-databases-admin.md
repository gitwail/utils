---
title: "Migrating from internal Satellite databases to external databases"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Migrating_from_Internal_Databases_to_External_Databases_admin"
---
# Chapter 3. Migrating from internal Satellite databases to external databases

When you install Red Hat Satellite, the **satellite-installer** command installs PostgreSQL databases on the same server as Satellite. If you are using the default internal databases but want to start using external databases to help with the server load, you can migrate your internal databases to external databases.

> **Important**
>
> Red Hat does not provide support or tools for external database maintenance. This includes backups, upgrades, and database tuning. You must have your own database administrator to support and maintain external databases.

## 3.1. Determining whether your Satellite Server uses internal or external databases

You can confirm whether your Satellite Server uses internal or external databases by checking the status of the PostgreSQL database service.

**Procedure**

- On Satellite Server, query the status of your databases:

  ```
  # satellite-maintain service status --only postgresql
  ```

## 3.2. PostgreSQL as an external database considerations

Foreman, Katello, and Candlepin use the PostgreSQL database. If you want to use PostgreSQL as an external database, the following information can help you decide if this option is right for your Satellite configuration. Satellite supports PostgreSQL version 13.

Advantages of external PostgreSQL
:   - Increase in free memory and free CPU on Satellite
    - Flexibility to set `shared_buffers` on the PostgreSQL database to a high number without the risk of interfering with other services on Satellite
    - Flexibility to tune the PostgreSQL server’s system without adversely affecting Satellite operations

Disadvantages of external PostgreSQL
:   - Increase in deployment complexity that can make troubleshooting more difficult
    - The external PostgreSQL server is an additional system to patch and maintain
    - If either Satellite or the PostgreSQL database server suffers a hardware or storage failure, Satellite is not operational
    - If there is latency between the Satellite server and database server, performance can suffer

If you suspect that the PostgreSQL database on your Satellite is causing performance problems, use the information in [Satellite 6: How to enable postgres query logging to detect slow running queries](https://access.redhat.com/solutions/2780871) to determine if you have slow queries.

Queries that take longer than one second are typically caused by performance issues with large installations, and moving to an external database might not help. If you have slow queries, contact Red Hat Support.

## 3.3. Installing PostgreSQL as an external database

Install and configure PostgreSQL on a dedicated host if you want to use an external database with your Satellite Server.

Satellite supports PostgreSQL version 13.

**Prerequisites**

- The prepared host has base operating system repositories enabled.
- The prepared host has sufficient disk space available for the `/var/lib/pgsql` directory. The expected installation size is 100 MB and the expected runtime size is 20 GB.

**Procedure**

1. On your new database server, install PostgreSQL:

   ```
   # dnf install postgresql-server postgresql-contrib
   ```
2. Initialize the PostgreSQL database:

   ```
   # postgresql-setup --initdb
   ```
3. Edit the `/var/lib/pgsql/data/postgresql.conf` file:

   ```
   # vi /var/lib/pgsql/data/postgresql.conf
   ```

   Note that the default configuration of external PostgreSQL needs to be adjusted to work with Satellite. The base recommended external database configuration adjustments are as follows:

   - checkpoint_completion_target: 0.9
   - max_connections: 500
   - shared_buffers: 512MB
   - work_mem: 4MB
4. Remove the `#` and edit to listen to inbound connections:

   ```
   listen_addresses = '*'
   ```
5. Add the following line to the end of the file to use SCRAM for authentication:

   ```
   password_encryption=scram-sha-256
   ```
6. Edit the `/var/lib/pgsql/data/pg_hba.conf` file:

   ```
   # vi /var/lib/pgsql/data/pg_hba.conf
   ```
7. Add the following line to the file:

   ```
     host  all   all   Satellite_ip/32   scram-sha-256
   ```
8. Start and enable the PostgreSQL service:

   ```
   # systemctl enable --now postgresql
   ```
9. Update the firewall configuration. For example, using the `firewall-cmd` command:

   1. Open the **postgresql** port:

      ```
      # firewall-cmd --add-service=postgresql
      ```
   2. Make the changes persistent:

      ```
      # firewall-cmd --runtime-to-permanent
      ```
10. Switch to the `postgres` user and start the PostgreSQL client:

    ```
    $ su - postgres -c psql
    ```
11. Create three databases and dedicated roles: one for Foreman, one for Candlepin, and one for Pulp:

    ```
    CREATE USER "foreman" WITH PASSWORD 'Foreman_Password';
    CREATE DATABASE foreman OWNER foreman;
    CREATE USER "candlepin" WITH PASSWORD 'Candlepin_Password';
    CREATE DATABASE candlepin OWNER candlepin;
    CREATE USER "pulp" WITH PASSWORD 'Pulpcore_Password';
    CREATE DATABASE pulpcore OWNER pulp;
    ```
12. Exit the `postgres` user:

    ```
    # \q
    ```

**Verification**

- From Satellite Server, test that you can access the database:

  ```
  # PGPASSWORD='Foreman_Password' pg_isready --host=postgres.example.com --port=5432 --username=foreman --dbname=foreman
  # PGPASSWORD='Candlepin_Password' pg_isready --host=postgres.example.com --port=5432 --username=candlepin --dbname=candlepin
  # PGPASSWORD='Pulpcore_Password' pg_isready --host=postgres.example.com --port=5432 --username=pulp --dbname=pulpcore
  ```

  If the connection succeeded, this displays an `accepting connections` message.

## 3.4. Migrating to external databases

Back up and transfer existing data, then use the `satellite-installer` command to configure Satellite to connect to an external PostgreSQL database server.

**Prerequisites**

- You have installed and configured a PostgreSQL server on an external server.

**Procedure**

1. On Satellite Server, stop all Satellite services except for PostgreSQL:

   ```
   # satellite-maintain service stop --exclude postgresql
   ```
2. Create your target directory for the Satellite backup:

   ```
   # mkdir /var/My_Migration_Backup_Directory
   ```
3. Back up the internal databases:

   ```
   # satellite-maintain backup online \
   --preserve-directory \
   --skip-pulp-content \
   /var/My_Migration_Backup_Directory
   ```
4. Transfer the data to the new external databases:

   ```
   PGPASSWORD='Foreman_Password' pg_restore --host=postgres.example.com --username=foreman --dbname=foreman < /var/My_Migration_Backup_Directory/foreman.dump
   PGPASSWORD='Candlepin_Password' pg_restore --host=postgres.example.com --username=candlepin --dbname=candlepin < /var/My_Migration_Backup_Directory/candlepin.dump
   PGPASSWORD='Pulpcore_Password' pg_restore --host=postgres.example.com --username=pulp --dbname=pulpcore < /var/My_Migration_Backup_Directory/pulpcore.dump
   ```
5. Use the `satellite-installer` command to update Satellite to point to the new databases:

   ```
   # satellite-installer \
   --katello-candlepin-manage-db false \
   --katello-candlepin-db-host postgres.example.com \
   --katello-candlepin-db-name candlepin \
   --katello-candlepin-db-user candlepin \
   --katello-candlepin-db-password Candlepin_Password \
   --foreman-proxy-content-pulpcore-manage-postgresql false \
   --foreman-proxy-content-pulpcore-postgresql-host postgres.example.com \
   --foreman-proxy-content-pulpcore-postgresql-db-name pulpcore \
   --foreman-proxy-content-pulpcore-postgresql-user pulp \
   --foreman-proxy-content-pulpcore-postgresql-password Pulpcore_Password \
   --foreman-db-manage false \
   --foreman-db-host postgres.example.com \
   --foreman-db-database foreman \
   --foreman-db-username foreman \
   --foreman-db-password Foreman_Password
   ```
6. Remove the PostgreSQL package on Satellite Server:

   ```
   # dnf remove postgresql-server
   ```
7. Remove the PostgreSQL data directory:

   ```
   # rm -fr /var/lib/pgsql/data
   ```
