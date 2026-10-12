# Confluence exporter: environment variables

`scripts/confluence_to_md.py` reads its settings from environment variables. Fill them in in the
`.env` file in the repo root (see [Keep `.env` private](#keep-env-private) first) and run:

```bash
uv run --env-file .env scripts/confluence_to_md.py --space LINUX --out confluence/LINUX
```

You need **`CONFLUENCE_URL` plus one way to log in**. A Personal Access Token is the best choice.
If several are set, the script uses the first one in this order: `CONFLUENCE_PAT`,
`CONFLUENCE_USER` + `CONFLUENCE_PASSWORD`, `CONFLUENCE_COOKIE`. Blank values count as not set.

## `CONFLUENCE_URL`

The address of your Confluence site. Open any page in your browser and copy the part before
`/display/...`, `/pages/...` or `/spaces/...`:

- `https://confluence.example.com/display/LINUX/Home` → `https://confluence.example.com`
- `https://intranet.example.com/confluence/pages/viewpage.action?pageId=123` → `https://intranet.example.com/confluence`

Keep the context path, such as `/confluence`, if your site has one. Leave off the trailing slash.

## `CONFLUENCE_PAT` (recommended)

Works on Confluence Data Center or Server 7.9 and later.

1. In Confluence, click your **avatar (top right)** → **Settings**.
2. Open **Personal Access Tokens** in the left menu, then click **Create token**.
3. Give it a name. You can also set it to expire automatically, for example after 90 days.
4. Copy the token right away. Confluence only shows it once.

The token has the same read access as your account, so it can export any space you can see.

If you don't see **Personal Access Tokens**, either your Confluence is older than 7.9 or an admin
has turned tokens off. Ask IT, or use one of the options below.

## `CONFLUENCE_USER` + `CONFLUENCE_PASSWORD`

Your normal Confluence username (not always your email) and password. This only works if your site
allows basic auth on the REST API. It often won't work if you sign in through SSO, such as SAML or
Azure AD, or if two-factor login is required.

## `CONFLUENCE_COOKIE` (last resort)

Reuses the login session from your browser.

1. Log in to Confluence in your browser.
2. Open developer tools (**F12**) → **Application** tab in Chrome or Edge, or **Storage** tab in
   Firefox → **Cookies** → your Confluence domain.
3. Copy the value of `JSESSIONID` and set `CONFLUENCE_COOKIE=JSESSIONID=<value>`. If your site also
   sets `seraph.confluence`, add it after a semicolon: `JSESSIONID=...; seraph.confluence=...`

The session stops working when you log out or it times out, often after a few hours. Check your IT
policy first, because some companies don't allow reusing browser sessions in scripts.

## `REQUESTS_CA_BUNDLE` (optional)

Leave this empty unless the script fails with `SSL: CERTIFICATE_VERIFY_FAILED`. That error usually
means your company signs its internal sites with its own certificate authority. Point this variable
at a PEM file that contains your company's root certificate. You can get one of these ways:

- Ask IT for the root CA file in PEM format.
- Use your system's bundle if the company CA is already installed: `/etc/pki/tls/certs/ca-bundle.crt`
  on RHEL or Fedora, `/etc/ssl/certs/ca-certificates.crt` on Debian or Ubuntu.
- Export it from your browser: click the **padlock** → certificate details → select the **top
  (root) certificate** → export as Base64/PEM.

The script's `--ca-bundle` flag does the same thing.

## Keep `.env` private

`.env` is committed to the repo as an empty template, so git sees your token as a change once you
fill it in. Before adding any values, tell git on your machine to ignore your local edits:

```bash
git update-index --skip-worktree .env
chmod 600 .env    # readable only by your user
```

Never commit a filled-in `.env` or paste its contents anywhere. To undo the skip later, run
`git update-index --no-skip-worktree .env`.
